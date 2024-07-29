import os

import aiohttp

# TODO сделать нормальные .env
api_token = os.getenv('GITHUB_API_KEY')


class HTTPClient:
    def __init__(self) -> None:
        # TODO: используй httpx, aiohttp много под собой лишнего тянет (вкусовщина)
        self.session = aiohttp.ClientSession()

    async def get(self, url: str):
        async with self.session.get(
            url,
            headers={'Authorization': f'Bearer {api_token}'}
        ) as response:
            json = await response.json()
            return json