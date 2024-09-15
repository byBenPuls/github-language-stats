# GitHub profile language statistics

![](https://i.imgur.com/Tb0vwS4.gif)

Link:

`![](https://<YOUR DOMAIN>/?username=<YOUR USERNAME>&theme=<THEME>)`

Example:

`![](https://example.com/?username=byBenPuls&theme=ambient_gradient)`

## Available themes:

|            Name            | Preview                                         |
|:--------------------------:|-------------------------------------------------|
|            Main            | ![](docs/assets/main.svg)                       |
|            Dark            | ![](docs/assets/dark.svg)                       |
|          Monokai           | ![](docs/assets/monokai.svg)                    |
|          Gradient          | ![](docs/assets/gradient.svg)                   |
|      Ambient Gradient      | ![](docs/assets/ambient_gradient.svg)           |
|     Vice City Gradient     | ![](docs/assets/vice_city_gradient.svg)         |
|    Ocean Blue Gradient     | ![](docs/assets/ocean_blue_gradient.svg)        |
| Eternal Constance Gradient | ![](docs/assets/eternal_constance_gradient.svg) |
|      Purpink Gradient      | ![](docs/assets/purpink_gradient.svg)           |


## Installation

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

> [!TIP]
> Full documentation available in the docs folder
