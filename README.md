Python 3 GRPC server to do basic chat, with requests to pull in stock information.

## Installation

```
poetry install
```

Alternatively, ensure the following are installed for runtime:

```
pip install grpcio googleapis-common-protos requests
```

## Usage

Start up the server with

```
poetry run serve
```

Produce messages with 

```
poetry run produce
```

and consume them with

```
poetry run consume
```

Alternatively, without poetry:

Start up the server with

```
python chat/server.py
```

produce messages with

```
python chat/client.py produce
```

and consume them with

```
python chat/client.py
```
