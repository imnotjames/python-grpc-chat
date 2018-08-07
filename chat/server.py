from concurrent import futures
import time
from uuid import uuid4
import re

import grpc
from google.protobuf.empty_pb2 import Empty
from google.protobuf.timestamp_pb2 import Timestamp

from chat.session import Session, Memory as MemorySession
from chat.authentication import Authentication, Memory as MemoryAuthentication
from chat.stock import get_stock

import chat_pb2
import chat_pb2_grpc


class ChatServicer(chat_pb2_grpc.ChatServicer):
    PLAYBACK_LIMIT = 50

    def __init__(self, session_impl, authentication_impl):
        assert isinstance(session_impl, Session)
        assert isinstance(authentication_impl, Authentication)

        self._playback = []

        self._session = session_impl
        self._authentication = authentication_impl

    def Login(self, request, context):
        username = request.username
        password = request.password

        if not self._authentication.authenticate(username, password):
            raise ValueError('invalid credentials')

        session_id = str(uuid4())

        self._session.initialize(session_id, username)

        for message in self._playback:
            self._session.append_unread_message(session_id, message)

        return chat_pb2.LoginResponse(session=chat_pb2.Session(id=session_id))

    def Logout(self, request, context):
        session_id = request.session.id

        self._session.delete(session_id)

        return chat_pb2.LogoutResponse()

    def SendMessage(self, request, context):
        session_id = request.session.id

        if not self._session.has(session_id):
            raise ValueError('invalid session')

        username = self._session.get_username(session_id)
        text = request.text

        # Pull stock information if found..
        symbols = re.findall('(?<=\$)([A-Z]+)', text)

        # Fetch the first 3 symbols max
        stocks = [get_stock(symbol) for symbol in symbols[0:4]]
        stocks = filter(None, stocks)

        message = {
            'timestamp': time.time(),
            'username': username,
            'text': text,
            'stocks': stocks
        }

        # Store on "global" playback.
        self._playback.append(message)

        # TODO: Use a better data structure for this - something
        #       to do a simpler size limit.
        self._playback = self._playback[-self.PLAYBACK_LIMIT:]

        # Find all open sessions, store on their playback too..
        # This could also be done by utilizing a pub/sub as well?
        for other_session_id in self._session.get_sessions():
            self._session.append_unread_message(other_session_id, message)

        return Empty()

    def Stream(self, request, context):
        session_id = request.session.id

        if not self._session.has(session_id):
            raise ValueError('invalid session')

        for message in self._session.pop_unread_messages(session_id):
            yield chat_pb2.StreamResponse(
                timestamp=Timestamp(seconds=int(message['timestamp'])),
                username=message['username'],
                text=message['text'],
                stock=[chat_pb2.Stock(**s) for s in message['stocks']]
            )


def serve():
    servicer = ChatServicer(
        MemorySession(),
        MemoryAuthentication({'hello': 'world'})
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(servicer, server)

    server.add_insecure_port('[::]:8081')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
