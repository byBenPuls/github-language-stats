from typing import Any

import httpx

from src.settings import settings


class GitHubHTTPClient:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()
        self.api_token = settings.GITHUB_API_TOKEN

    async def get(self, url: str) -> Any:
        response = await self.client.get(
            url, headers={"Authorization": f"Bearer {self.api_token}"}
        )
        response.raise_for_status()
        return response.json()

    async def get_repos(self, username: str) -> list[dict]:
        return await self.get(f"https://api.github.com/users/{username}/repos")

    async def get_languages_from_repo(self, repo_url: str) -> dict:
        return await self.get(repo_url)
