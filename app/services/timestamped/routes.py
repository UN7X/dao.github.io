from fastapi import APIRouter, Request
from app.core.auth import verify_api_key
from app.services.timestamped.models import TimestampRequest, TimestampResponse
from app.services.timestamped.utils import generate_timestamp

router = APIRouter()

@router.post("/timestamp", response_model=TimestampResponse)
async def create_timestamp(req: TimestampRequest, request: Request):
    verify_api_key(request)
    result = generate_timestamp(req.content)
    return {"timestamp": result}

@router.get("/health")
async def health_check():
    return {"status": "ok"}