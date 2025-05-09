import hashlib
from datetime import datetime, timezone

def generate_timestamp(content: str) -> str:
    hashed = hashlib.sha256(content.encode()).hexdigest()
    time = datetime.now(timezone.utc).isoformat()
    return f"{hashed} @ {time}Z"
