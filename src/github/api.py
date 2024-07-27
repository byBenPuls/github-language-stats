import asyncio
import logging
from collections import defaultdict
from typing import Dict, List

from src.github.requests import HTTPClient
from src.database.caching import in_cache, record_in_cache, get_from_cache
from src.exceptions import *

request_client = HTTPClient()

logger = logging.getLogger("uvicorn.info")


async def fetch_repos(user: str) -> Dict:
    request = await request_client.get(f'https://api.github.com/users/{user}/repos')
    if 'status' in request:
        raise error_codes[request['status']]['exception']()
    return request


async def get_languages_stats_from_repos(user: str) -> List:
    if await in_cache(user):
        return await get_from_cache(user)

    all_repos = await fetch_repos(user)

    async def get_languages_url(repo: Dict) -> Dict:
        logger.info(f'Getting languages stats from {repo["name"]}')
        response = await request_client.get(repo['languages_url'])
        return response

    languages_list = await asyncio.gather(*[get_languages_url(repo) for repo in all_repos])

    result_list = defaultdict(int)

    for language_response in languages_list:
        for language, count in language_response.items():
            result_list[language] += count

    result = dict(sorted(result_list.items(), key=lambda item: item[1], reverse=True))
    response_list = [language for language, _ in result.items()][:6]

    if response_list and not await in_cache(user):
        await record_in_cache(user, *response_list)

    return response_list
