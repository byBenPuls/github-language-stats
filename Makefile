.PHONY: all

SHELL=/bin/bash -e

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

run:
	sudo docker-compose build
	sudo docker-compose up