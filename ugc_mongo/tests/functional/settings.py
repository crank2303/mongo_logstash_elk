from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    mongo_host: str = Field(..., env="MONGO_HOST") 
    mongo_port: int = Field(..., env="MONGO_PORT")
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: int = Field(..., env="REDIS_PORT")
    service_protocol: str = Field(..., env="SERVICE_PROTOCOL")
    service_host: str = Field(..., env="SERVICE_HOST")
    service_port: str = Field(..., env="SERVICE_PORT")
    service_api_version: int = Field(..., env="SERVICE_API_VERSION")


config = TestSettings()
