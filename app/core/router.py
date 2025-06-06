from fastapi import APIRouter
from app.services.timestamped.routes import router as timestamped_router
from app.services.hashcache.routes import router as hashcache_router
from app.services.asix.routes import router as asix_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(timestamped_router, prefix="/timestamped", tags=["timestamped"])
api_router.include_router(hashcache_router, prefix="/hashcache", tags=["hashcache"])
api_router.include_router(asix_router, prefix="/asix", tags=["asix"])
