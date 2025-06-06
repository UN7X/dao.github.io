import uuid
from datetime import datetime, timedelta, timezone
from typing import Dict

from .models import LockerInfo, LockerCreate, ObjectData, KeyRequest

_lockers: Dict[str, Dict] = {}
_keys: Dict[str, Dict] = {}


def create_locker(req: LockerCreate) -> LockerInfo:
    locker_id = str(uuid.uuid4())
    _lockers[locker_id] = {
        'created': datetime.now(timezone.utc),
        'password': req.password,
        'objects': {},
    }
    return LockerInfo(id=locker_id, created=_lockers[locker_id]['created'])


def add_object(locker_id: str, obj: ObjectData) -> str:
    locker = _lockers[locker_id]
    obj_id = str(uuid.uuid4())
    locker['objects'][obj_id] = obj.data
    return obj_id


def get_object(locker_id: str, obj_id: str):
    return _lockers[locker_id]['objects'].get(obj_id)


def update_object(locker_id: str, obj_id: str, obj: ObjectData):
    _lockers[locker_id]['objects'][obj_id] = obj.data


def delete_object(locker_id: str, obj_id: str):
    _lockers[locker_id]['objects'].pop(obj_id, None)


def generate_key(locker_id: str, req: KeyRequest) -> str:
    key = str(uuid.uuid4())
    expires = None
    if req.expires_in:
        expires = datetime.now(timezone.utc) + timedelta(seconds=req.expires_in)
    _keys[key] = {
        'locker_id': locker_id,
        'access_type': req.access_type,
        'expires': expires,
        'one_time': req.one_time,
        'used': False,
    }
    return key


def validate_key(locker_id: str, key: str, access_type: str) -> bool:
    info = _keys.get(key)
    if not info or info['locker_id'] != locker_id:
        return False
    if info['access_type'] != access_type:
        return False
    if info['expires'] and datetime.now(timezone.utc) > info['expires']:
        return False
    if info['one_time'] and info['used']:
        return False
    info['used'] = True
    return True
