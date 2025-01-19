import asyncio
from services.crawler_service import *
from services.nats_broker import NatsBroker
from services.pubsub_service import PubSubService


async def main():
    servers = ["nats://localhost:4222"]
    broker = NatsBroker()

    pubsub = PubSubService(broker)

    await pubsub.connect(servers)
    
    await asyncio.sleep(1)

    services = {
        "JeW": ["SP"],
        "ItFox": ["MG", "DF", "RJ"]
    }

    uf = "MG"
    subject = next(service for service, ufs in services.items() if uf in ufs)

    if not subject:
        print(f"Service not found for state: {uf}")
        return
    
    await pubsub.publish(subject, "Hello, World!")
    
    await pubsub.close()



if __name__ == "__main__":
    asyncio.run(main())
