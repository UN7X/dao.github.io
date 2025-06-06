from datetime import datetime, timezone
from typing import Dict, Optional
from pydantic import BaseModel, Field

class LockerCreate(BaseModel):
    password: Optional[str] = None

class ObjectData(BaseModel):
    data: Dict

class KeyRequest(BaseModel):
    expires_in: Optional[int] = Field(None, description="Seconds until expiry")
    one_time: bool = False
    access_type: str = "read"  # read/update/delete

class LockerInfo(BaseModel):
    id: str
    created: datetime

