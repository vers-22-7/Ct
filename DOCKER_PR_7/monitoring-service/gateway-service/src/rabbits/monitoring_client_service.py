from typing import List
import httpx
from rabbits.model import Rabbit
from settings import settings

class MonitoringClientService:
    async def find_rabbits(self) -> List[Rabbit]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.counting_service_url}/monitor/")
            data = response.json()
            return [Rabbit(**item) for item in data]
