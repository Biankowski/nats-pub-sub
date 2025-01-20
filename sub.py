import json
import asyncio
from services.pubsub_service import PubSubService
from services.nats_broker import NatsBroker

async def message_callback(msg: str | bytes):
    if isinstance(msg, bytes):
        msg = msg.data.decode()
    
    msg = json.loads(msg.data)

    print("Received message:", msg)

async def main():
    servers = ["nats://localhost:4222"]
    broker  = NatsBroker()
    pubsub = PubSubService(broker)

    await pubsub.connect(servers)
    await pubsub.subscribe("Nacional", message_callback)
    await pubsub.subscribe("SP", message_callback)
    await pubsub.subscribe("MG", message_callback)
    await pubsub.subscribe("DF", message_callback)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        await pubsub.close()


if __name__ == "__main__":
    asyncio.run(main())
