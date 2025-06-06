# HashCache

POST `/api/v1/hashcache/submit`
```json
{ "hash": "abc123", "filename": "optional.txt", "malware_score": 0 }
```

Registers a file hash with metadata. Repeat calls update the entry.

GET `/api/v1/hashcache/{hash}` retrieves stored information or `404` if missing.
