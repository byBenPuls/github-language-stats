import asyncio
import logging
from collections import defaultdict
from typing import Dict, List

from src.github.requests import HTTPClient
from src.database.caching import in_cache, record_in_cache, get_from_cache
from src.exceptions import error_codes

request_client = HTTPClient()

logger = logging.getLogger("uvicorn.info")

# TODO если использушь свой клиент, то напиши свой репозиторий для гитхаба с запросом всех нужных вещей 
# TODO typehint используй новую версию и пиши дженерики полноценные
async def fetch_repos(user: str) -> Dict:
    # TODO лучше через класс + зависимость от клиента
    request = await request_client.get(f'https://api.github.com/users/{user}/repos')
    if 'status' in request:
        # TODO тебе это реально нужно? request.raise_for_status() обычно этого достаточно
        raise error_codes[request['status']]['exception']()
    return request

# TODO typehint используй новую версию и пиши дженерики полноценные
async def get_languages_stats_from_repos(user: str) -> List:
    # TODO сделай лучше композитным репозиторием. у тебя перемешиваются 2 хранилища
    if await in_cache(user):
        return await get_from_cache(user)

    all_repos = await fetch_repos(user)

    # TODO зачем это тут? общий класс с репозиторием для гитхаба
    # TODO зачем ему знать про все репо если нужна только ссылка?
    async def get_languages_url(repo: Dict) -> Dict:
        logger.info(f'Getting languages stats from {repo["name"]}')
        response = await request_client.get(repo['languages_url'])
        return response

    # TODO туда же в общий класс
    languages_list = await asyncio.gather(*[get_languages_url(repo) for repo in all_repos])

    result_list = defaultdict(int)

    # TODO в питоне есть `from collections import Counter`
    for language_response in languages_list:
        for language, count in language_response.items():
            result_list[language] += count
    
    # TODO counter.most_common(6)
    result = dict(sorted(result_list.items(), key=lambda item: item[1], reverse=True))
    response_list = [language for language, _ in result.items()][:6]

    # TODO сделай лучше композитным репозиторием. у тебя перемешиваются 2 хранилища
    if response_list and not await in_cache(user):
        await record_in_cache(user, *response_list)

    return response_list
