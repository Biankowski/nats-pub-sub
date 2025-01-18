from nats.aio.client import Client as NATS
from typing import List, Callable, Any
from services.message_broker import MessageBroker

class NatsBroker(MessageBroker):
    def __init__(self):
        self.nc = NATS()
    
    async def connect(self, servers: List[str]) -> None:
        try:
            await self.nc.connect(servers=servers)
            
            print("Connected to NATS server")
        except Exception as e:
            print(f"Failed to connect to NATS server: {e}")
            raise e
    
    async def close(self) -> None:
        try:
            await self.nc.close()
            
            print("Disconnected from NATS server")
        except Exception as e:
            print(f"Failed to disconnect from NATS server: {e}")
            raise e
    

    async def publish(self, subject: str, message: str | bytes) -> None:
        try:
            if isinstance(message, str):
                message = message.encode()

            await self.nc.publish(subject, message)

            print(f"Published message to subject {subject}")
        except Exception as e:
            print(f"Failed to publish message to subject {subject}: {e}")
            raise e

    async def subscribe(self, subject: str, callback: Callable) -> None:
        try:
            await self.nc.subscribe(subject, cb=callback)

            print(f"Subscribed to subject {subject}")
        except Exception as e:
            print(f"Failed to subscribe to subject {subject}: {e}")
            raise e
