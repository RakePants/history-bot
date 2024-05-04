import asyncio
from abc import ABC, abstractmethod

from src.config import settings
from src.database.client import index


class AbstractRepository(ABC):
    @abstractmethod
    def query(self, entity_id):
        raise NotImplementedError


class InformationRepository(AbstractRepository):
    def __init__(self):
        self.index = index
        self.namespace = settings.pinecone_namespace

    async def query(self, vector, top_k: int = 4) -> list:
        response = await asyncio.to_thread(
            self.index.query,
            namespace=self.namespace,
            vector=vector,
            top_k=top_k,
            include_values=False,
            include_metadata=True,
        )

        return response
