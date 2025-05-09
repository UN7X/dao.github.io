from fastapi import APIRouter
from app.services.timestamped.routes import router as timestamped_router

api_router = APIRouter(prefix="/v1")
api_router.include_router(timestamped_router, prefix="/timestamped", tags=["timestamped"])
