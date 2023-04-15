from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    mongo_host: str = Field("mongors1n1", env="MONGO_HOST")
    mongo_port: int = Field(27017, env="MONGO_PORT")
    redis_host: str = Field("cs_redis", env="REDIS_HOST")
    redis_port: int = Field(6379, env="REDIS_PORT")
    service_protocol: str = Field("http", env="SERVICE_PROTOCOL")
    service_host: str = Field("cs_fastapi", env="SERVICE_HOST")
    service_port: str = Field(8000, env="SERVICE_PORT")
    service_api_version: int = Field(1, env="SERVICE_API_VERSION")


config = TestSettings()
