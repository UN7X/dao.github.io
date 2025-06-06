# Timestamped

POST `/api/v1/timestamped/timestamp`

Request body:
```json
{ "content": "string" }
```

Returns a SHA-256 hash of the content with a UTC timestamp and signature.

GET `/api/v1/timestamped/health` returns `{"status": "ok"}`.
