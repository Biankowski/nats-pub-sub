from abc import ABC, abstractmethod
from nats.aio.client import Client as NATS
from typing import List, Callable, Any

class MessageBroker(ABC):
    @abstractmethod
    async def connect(self, servers: List[str]) -> None:
        pass

    @abstractmethod
    async def publish(self, subject: str, message: str | bytes) -> None:
        pass

    @abstractmethod
    async def subscribe(self, subject: str, callback: Callable) -> None:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass

