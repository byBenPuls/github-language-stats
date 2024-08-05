import asyncio
import logging
from collections import defaultdict, Counter

import httpx

from src.github.requests import GitHubHTTPClient

logger = logging.getLogger("uvicorn.info")


class ProgramLangRepo:
    def __init__(self) -> None:
        self.github = GitHubHTTPClient()

    @staticmethod
    def lang_sorter(langs: list, limit: int = 6) -> dict[str, int | float]:
        result = defaultdict(int)

        for language_response in langs:
            for language, count in language_response.items():
                result[language] += count
        return dict(Counter(dict(result)).most_common(limit))

    async def get_languages(self, limit: int, username: str) -> dict[str, int | float]:
        try:
            repos = await self.github.get_repos(username)

            languages_list = await asyncio.gather(
                *[
                    self.github.get_languages_from_repo(repo["languages_url"])
                    for repo in repos
                ]
            )
        except (httpx.HTTPStatusError, httpx.ConnectError) as e:
            logger.info(e)
            return {}
        langs = self.lang_sorter(list(languages_list), limit=limit)
        logger.info(langs)
        return langs
