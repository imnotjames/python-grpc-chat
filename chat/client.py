import time

import grpc

import chat_pb2
import chat_pb2_grpc


def format_stock_message(message, stock):

    return (
        '[{timestamp}] (${symbol}) '
        '{name} ${price:,.2f} '
        '{change:,.2f} ({percent_change:,.2f}%) | '
        'Day Range: ${low:,.2f} - ${high:,.2f}'
    ).format(
        timestamp=message.timestamp.seconds,
        symbol=stock.symbol,
        name=stock.name,
        price=stock.price,
        change=stock.change,
        percent_change=stock.percent_change,
        low=stock.low,
        high=stock.high
    )


def format_message(message):
    return '[{timestamp}] <{username}> {text}'.format(
        timestamp=message.timestamp.seconds,
        username=message.username,
        text=message.text
    )


def produce():
    username = 'hello'
    password = 'world'

    with grpc.insecure_channel('localhost:8081') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)

        session = stub.Login(chat_pb2.LoginRequest(username=username, password=password)).session

        try:
            while True:
                text = input('{} > '.format(username))

                stub.SendMessage(chat_pb2.SendMessageRequest(session=session, text=text))
        except KeyboardInterrupt:
            stub.Logout(chat_pb2.LogoutRequest(session=session))


def consume():
    username = 'hello'
    password = 'world'

    with grpc.insecure_channel('localhost:8081') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)

        session = stub.Login(chat_pb2.LoginRequest(username=username, password=password)).session

        try:
            while True:
                for message in stub.Stream(chat_pb2.StreamRequest(session=session)):
                    print(format_message(message))

                    for stock in message.stock:
                        print(format_stock_message(message, stock))

                time.sleep(0.5)
        except KeyboardInterrupt:
            stub.Logout(chat_pb2.LogoutRequest(session=session))


if __name__ == '__main__':
    if sys.argv[1] == 'produce':
        produce()
    else:
        consume()
