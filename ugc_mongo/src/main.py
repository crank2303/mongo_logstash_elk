import logging

import aioredis
import logstash
import sentry_sdk
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from api.v1 import film, user
from core.config import settings as config
from core.logger import LOGGING
from db import mongo, redis

app = FastAPI(
    title=config.project_name,
    version="1.0.0",
    description="Asychronus API for UGC database",
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/redoc",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    redis.redis = aioredis.from_url(
        f"redis://{config.redis_host}:{config.redis_port}",
        encoding="utf-8",
        decode_responses=True,
    )

    mongo.mongo = AsyncIOMotorClient(
        "mongodb://{host}:{port}".format(
            host=config.mongo_host,
            port=config.mongo_port,
        )
    )

    sentry_sdk.init(
        config.sentry_dsn,
        traces_sample_rate=1.0,
    )

    logger = logging.getLogger("uvicorn.access")
    logger.setLevel(logging.INFO)
    logger.addHandler(
        logstash.LogstashHandler(
            config.logstash_host,
            config.logstash_port,
            version=1,
        )
    )


@app.on_event("shutdown")
async def shutdown():
    await mongo.mongo.close()
    await redis.redis.close()


@app.middleware("http")
async def loggin(request: Request, call_next):
    response = await call_next(request)
    request_id = request.headers.get("X-Request-Id")
    logger = logging.getLogger("uvicorn.access")
    custom_logger = logging.LoggerAdapter(
        logger, extra={"tag": "ugcmongo_api", "request_id": request_id}
    )
    custom_logger.info(request)
    return response


app.include_router(film.router, prefix="/api/v1/film", tags=["film"])
app.include_router(user.router, prefix="/api/v1/user", tags=["user"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8888,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
