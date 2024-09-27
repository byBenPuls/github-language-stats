.PHONY: all

SHELL=/bin/bash -e

install:
	poetry install --no-dev

install-dev:
	poetry install --dev

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

test:
	poetry run pytest . -p no:logging -p no:warnings

run:
	sudo docker-compose build
	sudo docker-compose up