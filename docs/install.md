# Installation

1. Copy `example.env` file in `.env`

```shell
cp example.env .env
```
2. Setup docker containers

With make:

```make
make run
```

Without make:

```
docker-compose build && docker-compose up
```