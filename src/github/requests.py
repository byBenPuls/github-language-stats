import os

import httpx

# TODO сделать нормальные .env
api_token = os.getenv('GITHUB_API_KEY')


class HTTPClient:
    def __init__(self) -> None:
        # TODO: используй httpx, aiohttp много под собой лишнего тянет (вкусовщина)
        self.client = httpx.AsyncClient()

    async def get(self, url: str):
        response = await self.client.get(url, headers={'Authorization': f'token {api_token}'})
        return response.json()
