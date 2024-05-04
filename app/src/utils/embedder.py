import json

import aiohttp

from src.config import settings


async def embed(sequence: str):
    url = settings.remote_url + "/embed"
    data = {"text": sequence}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(data)) as response:
            response_text = await response.text()
            return response_text
