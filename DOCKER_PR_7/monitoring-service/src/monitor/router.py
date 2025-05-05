from fastapi import APIRouter
from .model import Rabbit

router = APIRouter()

@router.get("/monitor/", tags=["search"])
def find_rabbits():
    return [
        Rabbit("Rabbit A"),
        Rabbit("Rabbit B"),
        Rabbit("Rabbit C"),
        Rabbit("Rabbit D"),
    ]
