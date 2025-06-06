from fastapi import APIRouter, Request, HTTPException

from app.core.auth import verify_api_key

from .models import SubmitRequest, HashInfo
from . import storage

router = APIRouter()

@router.post("/submit", response_model=HashInfo)
async def submit_hash(req: SubmitRequest, request: Request):
    verify_api_key(request)
    entry = storage.submit(req)
    return entry

@router.get("/{hash_value}", response_model=HashInfo)
async def get_hash(hash_value: str, request: Request):
    verify_api_key(request)
    entry = storage.get(hash_value)
    if not entry:
        raise HTTPException(status_code=404, detail="Hash not found")
    return entry

@router.get("/health")
async def health_check():
    return {"status": "ok"}
