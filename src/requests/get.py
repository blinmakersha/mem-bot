from aiohttp import ClientResponseError

from src.utils.request import do_request

from conf.config import settings


async def fetch_mem(endpoint: str) -> dict:
    try:
        data = await do_request(
            f'{settings.MEM_BACKEND_HOST}{endpoint}',
            method='GET',
        )
        return data
    except ClientResponseError:
        return None
