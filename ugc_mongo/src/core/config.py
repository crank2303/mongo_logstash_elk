from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_name: str = Field("movies", env="PROJECT_NAME")

    redis_host: str = Field("127.0.0.1", env="REDIS_HOST")
    redis_port: int = Field(6379, env="REDIS_PORT")

    mongo_host: str = Field("127.0.0.1", env="MONGO_HOST")
    mongo_port: int = Field(27017, env="MONGO_PORT")

    sentry_dsn: str = Field(..., env="SENTRY_DSN")

    logstash_host: str = Field("127.0.0.1", env="SENTRY_DSN")
    logstash_port: int = Field(5044, env="LOGSTASH_PORT")

    jwt_secret: str = Field("qwerty", env="JWT_SECRET")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")


settings = Settings()
