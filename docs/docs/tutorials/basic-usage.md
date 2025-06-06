# Basic Usage

Use the timestamp service to sign any string:

```bash
curl -X POST \
  -H "Authorization: Bearer supersecret" \
  -H "Content-Type: application/json" \
  -d '{"content":"hello"}' \
  http://localhost:8000/api/v1/timestamped/timestamp
```
