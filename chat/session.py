from abc import ABC, abstractmethod
import time

class Session(ABC):
    @abstractmethod
    def get_sessions(self):
        pass

    @abstractmethod
    def initialize(self, session_id, username):
        pass

    @abstractmethod
    def has(self, session_id):
        pass

    @abstractmethod
    def delete(self, session_id):
        pass

    @abstractmethod
    def get_username(self, session_id):
        pass

    @abstractmethod
    def append_unread_message(self, session_id, message):
        pass

    @abstractmethod
    def pop_unread_messages(self, session_id):
        pass


class Memory(Session):
    UNREAD_MESSAGE_LIMIT = 50

    def __init__(self):
        self._sessions = {}

    def initialize(self, session_id, username):
        self._sessions[session_id] = {
            'active': time.time(),
            'username': username,
            'unread': []
        }

    def get_sessions(self):
        return list(self._sessions.keys())

    def has(self, session_id):
        return session_id in self._sessions

    def delete(self, session_id):
        self._sessions.pop(session_id)

    def get_username(self, session_id):
        if session_id not in self._sessions:
            raise ValueError("invalid session")

        return self._sessions[session_id]['username']

    def append_unread_message(self, session_id, message):
        if session_id not in self._sessions:
            raise ValueError("invalid session")

        self._sessions[session_id]['unread'].append(message)

        # TODO: Could replace this with a data structure which utilizes a
        # circular list?  Saving on these kinds of ops against the list.
        self._sessions[session_id]['unread'] = self._sessions[session_id]['unread'][-self.UNREAD_MESSAGE_LIMIT:]

    def pop_unread_messages(self, session_id):
        while len(self._sessions[session_id]['unread']) > 0:
            message = self._sessions[session_id]['unread'][0]
            del self._sessions[session_id]['unread'][0]
            yield message
