from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self, entity_id):
        raise NotImplementedError

    @abstractmethod
    async def get(self, entity_id):
        raise NotImplementedError
