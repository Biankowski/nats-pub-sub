from services.message_broker import MessageBroker
from typing import List, Callable, Any

class PubSubService:
    def __init__(self, message_broker: MessageBroker):
        self.broker = message_broker

    async def connect(self, servers: List[str]) -> None:
        await self.broker.connect(servers)
    
    async def close(self) -> None:
        await self.broker.close()
    
    async def publish(self, subject: str, message: str | bytes) -> None:
        await self.broker.publish(subject, message)
    
    async def subscribe(self, subject: str, callback: Callable) -> None:
        await self.broker.subscribe(subject, callback)