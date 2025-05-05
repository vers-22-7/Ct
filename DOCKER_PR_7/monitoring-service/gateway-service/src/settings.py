from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    counting_service_url: str = "http://localhost:8001"

settings = Settings()
