import json

import aiohttp
from src.config import settings


async def embed(sequence: str):
    url = settings.embeddings_url + "/embed"
    data = {"text": sequence}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(data)) as response:
            data = await response.json()
            vector = data.get("vector")
            
            return vector
