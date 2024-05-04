from abc import ABC, abstractmethod
from src.database.client import index
from src.config import settings


class AbstractRepository(ABC):
    @abstractmethod
    def query(self, entity_id):
        raise NotImplementedError


class InformationRepository(AbstractRepository):
    def __init__(self):
        self.index = index
        self.namespace = settings.pinecone_namespace

    def query(self, vector, top_k: int = 4) -> None:
        with self.index as index:
            with self.namespace as namespace:
                response = index.query(
                    namespace=namespace,
                    vector=vector,
                    top_k=top_k,
                    include_values=False,
                    include_metadata=True,
                )

        return response
