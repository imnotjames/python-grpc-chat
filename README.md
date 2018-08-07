Python 3 GRPC server to do basic chat, with requests to pull in stock information.

## Installation

Install [Poetry](https://github.com/sdispater/poetry) with

```
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Then install the dependencies using poetry

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

## Example Output

```
[1533651810] <hello> Hello $MSFT, are you doing better than $FB
[1533651810] ($MSFT) Microsoft Corp. $108.69 0.56 (0.52%) | Day Range: $108.17 - $109.10
[1533651810] ($FB) Facebook, Inc. $186.46 0.77 (0.42%) | Day Range: $186.01 - $188.30
[1533651844] <hello> $FB $GOOG
[1533651844] ($FB) Facebook, Inc. $186.60 0.91 (0.49%) | Day Range: $186.01 - $188.30
[1533651844] ($GOOG) Alphabet, Inc. $1,246.94 22.17 (1.81%) | Day Range: $1,236.78 - $1,247.16
```
