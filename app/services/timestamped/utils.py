import hashlib
import hmac
import os
from datetime import datetime, timezone

SECRET = os.environ.get("TIMESTAMP_SECRET", "changeme")


def generate_timestamp(content: str) -> str:
    hashed = hashlib.sha256(content.encode()).hexdigest()
    timestamp = datetime.now(timezone.utc).isoformat()
    message = f"{hashed}:{timestamp}"
    signature = hmac.new(SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()
    return f"{message}:{signature}"
