import os

import aiohttp

api_token = os.getenv('GITHUB_API_KEY')


class HTTPClient:
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession()

    async def get(self, url: str):
        async with self.session.get(
            url,
            headers={'Authorization': f'Bearer {api_token}'}
        ) as response:
            json = await response.json()
            return json
