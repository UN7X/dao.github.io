from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

class SubmitRequest(BaseModel):
    hash: str = Field(..., description="File hash")
    filename: Optional[str] = Field(None, description="Known filename")
    malware_score: int = 0
    tag: Optional[str] = None

class HashInfo(BaseModel):
    hash: str
    filenames: List[str]
    malware_score: int
    first_seen: datetime
    last_seen: datetime
    tag: Optional[str] = None
