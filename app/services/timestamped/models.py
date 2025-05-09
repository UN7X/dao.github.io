from pydantic import BaseModel

class TimestampRequest(BaseModel):
    content: str

class TimestampResponse(BaseModel):
    timestamp: str
