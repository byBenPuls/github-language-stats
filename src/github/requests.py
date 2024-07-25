import os

import httpx

api_token = os.getenv('GITHUB_API_KEY')


class HTTPClient:

    def __init__(self) -> None:
        self.client = httpx.AsyncClient()

    async def get(self, endpoint):
        response = await self.client.get(
            f'{endpoint}',
            headers={'Authorization': f'Bearer {api_token}'}
        )
        return response.json()
