import json

import aiohttp
from src.config import settings

import logging
async def embed(sequence: str):
    url = settings.embeddings_url + "/embed"
    data = {"text": sequence}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            data = await response.json()
            
            logging.info(data)
            
            vector = data.get("vector")
        
            return vector
