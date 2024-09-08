import asyncio
import logging
from collections import defaultdict, Counter

import httpx

from src.github.requests import GitHubHTTPClient

logger = logging.getLogger("uvicorn.info")


class ProgramLangRepo:
    def __init__(self) -> None:
        self.github_http_client = GitHubHTTPClient()

    @staticmethod
    def lang_sorter(
        langs: list | tuple, numbers_of_languages_limiter: int | None = 6
    ) -> dict[str, int | float]:
        """
        :param langs: languages list
        :param numbers_of_languages_limiter: Languages on the number of languages returned.
        If the limit is `None`, all user languages will be returned.
        """
        result = defaultdict(int)

        for language_response in langs:
            for name, count in language_response.items():
                result[name] += count
        result_value = dict(
            Counter(dict(result)).most_common(numbers_of_languages_limiter)
        )
        logger.info(result_value)
        return result_value

    async def get_languages(self, limit: int, username: str) -> dict[str, int | float]:
        try:
            repos = await self.github_http_client.get_all_repos_of_user(username)

            languages_list = await asyncio.gather(
                *(
                    self.github_http_client.get_languages_from_repo(
                        repo["languages_url"]
                    )
                    for repo in repos
                )
            )
        except (httpx.HTTPStatusError, httpx.ConnectError) as e:
            logger.info(e)
            return {}
        langs = self.lang_sorter(tuple(languages_list), limit)
        return langs
