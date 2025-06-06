from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, List

from .models import HashInfo, SubmitRequest

_storage: Dict[str, HashInfo] = {}


def submit(req: SubmitRequest) -> HashInfo:
    now = datetime.now(timezone.utc)
    if req.hash in _storage:
        entry = _storage[req.hash]
        if req.filename and req.filename not in entry.filenames:
            entry.filenames.append(req.filename)
        entry.malware_score = max(entry.malware_score, req.malware_score)
        entry.last_seen = now
        if req.tag:
            entry.tag = req.tag
    else:
        entry = HashInfo(
            hash=req.hash,
            filenames=[req.filename] if req.filename else [],
            malware_score=req.malware_score,
            first_seen=now,
            last_seen=now,
            tag=req.tag,
        )
        _storage[req.hash] = entry
    return entry


def get(hash_value: str) -> HashInfo | None:
    return _storage.get(hash_value)
