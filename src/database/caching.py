from dataclasses import dataclass

from src.database.redis import Redis
from src.github.repos import ProgramLangRepo


@dataclass
class CachedProgramLangRepo(ProgramLangRepo):
    cache: Redis
    repository: ProgramLangRepo

    def _key_builder(self, username: str) -> str:
        return username

    async def fetch_lang(self, username: str, limit: int) -> dict[str, int | float]:
        if data := await self.cache.get_from_cache(self._key_builder(username)):
            return data

        data = await self.repository.get_languages(limit, username)

        await self.cache.record_in_cache(self._key_builder(username), data)
        return data
