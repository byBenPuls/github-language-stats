from typing import Any

import httpx

from src.exceptions import NotFoundUserError, RequestLimitError, TokenInvalidError
from src.settings import settings


class GitHubHTTPClient:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()
        self.api_token = settings.GITHUB_API_TOKEN

    @staticmethod
    def raise_for_status(response: httpx.Response) -> None:
        match response.status_code:
            case 200:
                return
            case 404:
                raise NotFoundUserError("Username not found :(")
            case 403 | 429:
                raise RequestLimitError("Request limit exceeded :(")
            case 401:
                raise TokenInvalidError("Token invalid :(")

    async def get(self, url: str) -> Any:
        response = await self.client.get(
            url, headers={"Authorization": f"Bearer {self.api_token}"}
        )
        self.raise_for_status(response)
        return response.json()

    async def get_all_repos_of_user(self, username: str) -> list[dict]:
        return await self.get(f"https://api.github.com/users/{username}/repos")

    async def get_languages_from_repo(self, repo_url: str) -> dict:
        return await self.get(repo_url)
