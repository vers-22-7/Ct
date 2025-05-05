from typing import Annotated
from fastapi import APIRouter, Depends
from .dependencies import get_monitoring_service
from .monitoring_client_service import MonitoringClientService

router = APIRouter()

@router.get("/rabbits/", tags=["rabbits"])
async def get_rabbits(service: Annotated[MonitoringClientService, Depends(get_monitoring_service)]):
    rabbits = await service.find_rabbits()
    return {"items": [r for r in rabbits if "a" not in r.name.lower()]}
