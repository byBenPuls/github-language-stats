from functools import lru_cache

import punq

from src.database.redis import Redis


@lru_cache(1)
def get_container() -> punq.Container:
    return init_container()


def init_container() -> punq.Container:
    container = punq.Container()
    container.register(Redis, scope=punq.Scope.singleton)

    return container
