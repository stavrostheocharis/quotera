from fastapi import APIRouter
from .health import health_router
from .paraphrase_analytics import paraphrase_analytics_router

v1_router = APIRouter()
v1 = "/v1"

v1_router.include_router(health_router, prefix=v1)
v1_router.include_router(paraphrase_analytics_router, prefix=v1)
