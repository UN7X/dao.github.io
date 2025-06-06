from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi import Body
from app.core.auth import verify_api_key

from .models import LockerCreate, LockerInfo, ObjectData, KeyRequest
from . import storage

router = APIRouter()

@router.post("/lockers", response_model=LockerInfo)
async def create_locker(req: LockerCreate, request: Request):
    verify_api_key(request)
    return storage.create_locker(req)

@router.post("/lockers/{locker_id}/objects")
async def add_object(locker_id: str, obj: ObjectData, request: Request):
    verify_api_key(request)
    obj_id = storage.add_object(locker_id, obj)
    return {"id": obj_id}

@router.get("/lockers/{locker_id}/objects/{obj_id}")
async def get_object(locker_id: str, obj_id: str, request: Request, access_key: str | None = None):
    verify_api_key(request)
    if access_key and not storage.validate_key(locker_id, access_key, "read"):
        raise HTTPException(status_code=403, detail="Invalid access key")
    data = storage.get_object(locker_id, obj_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Not found")
    return {"data": data}

@router.put("/lockers/{locker_id}/objects/{obj_id}")
async def update_object(locker_id: str, obj_id: str, obj: ObjectData, request: Request):
    verify_api_key(request)
    storage.update_object(locker_id, obj_id, obj)
    return {"status": "updated"}

@router.delete("/lockers/{locker_id}/objects/{obj_id}")
async def delete_object(locker_id: str, obj_id: str, request: Request):
    verify_api_key(request)
    storage.delete_object(locker_id, obj_id)
    return {"status": "deleted"}

@router.post("/lockers/{locker_id}/keys")
async def create_key(locker_id: str, req: KeyRequest, request: Request):
    verify_api_key(request)
    key = storage.generate_key(locker_id, req)
    return {"key": key}

@router.get("/health")
async def health_check():
    return {"status": "ok"}
