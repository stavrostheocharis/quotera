from starlette.responses import Response
from src.schemas.errors import BadRequestError, NotFoundError
from fastapi import FastAPI, Request
from src.core.settings import get_settings
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import v1_router
from fastapi.responses import JSONResponse
import traceback
from fastapi.openapi.utils import get_openapi
import json
import logging

logging.basicConfig(level=logging.NOTSET)
settings = get_settings()
quotera = FastAPI(title=settings.APP_NAME)


def log_environment():
    settings = get_settings()
    logging.info(f"LOG INFO: Environment: {settings.ENV}")


quotera.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotera.add_event_handler("startup", log_environment)


def quotera_openapi():
    if quotera.openapi_schema:
        return quotera.openapi_schema
    openapi_schema = get_openapi(
        title="Quotera API",
        version="",
        routes=quotera.routes,
    )

    quotera.openapi_schema = openapi_schema
    return quotera.openapi_schema


@quotera.exception_handler(NotFoundError)
async def unicorn_exception_handler_not_found(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.detail})


@quotera.exception_handler(BadRequestError)
async def unicorn_exception_handler(request: Request, exc: BadRequestError):
    return JSONResponse(status_code=400, content={"detail": exc.detail})


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        tb = traceback.format_exc()
        logging.info("Error information: ", e)
        return JSONResponse(
            status_code=500, content={"detail": str(e), "meta": "Internal server error"}
        )


quotera.middleware("http")(catch_exceptions_middleware)


quotera.include_router(v1_router)
quotera.openapi = quotera_openapi
