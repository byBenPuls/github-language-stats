import asyncio
from collections import defaultdict, Counter

from src.github.requests import GitHubHTTPClient


class ProgramLangRepo:
    def __init__(self) -> None:
        self.github = GitHubHTTPClient()

    def lang_sorter(self, langs: list, count: int = 6) -> dict[str, int]:
        result = defaultdict(int)

        for language_response in langs:
            for language, count in language_response.items():
                result[language] += count
        return dict(Counter(dict(result)).most_common(count))

    async def get_languages(self, username: str) -> dict[str, int]:
        repos = await self.github.get_repos(username)

        languages_list = await asyncio.gather(
            *[self.github.get_languages_from_repo(repo['languages_url']) for repo in repos]
        )

        return self.lang_sorter(list(languages_list))
