# UDAO API Platform

A minimal FastAPI project providing three small services used by the U-DAO community.

## Features

- **Timestamped** – create signed timestamps for arbitrary text
- **HashCache** – submit hashes with metadata and query them later
- **ASIX** – simple lockers for storing JSON objects with optional access keys

All endpoints require an `Authorization: Bearer supersecret` header in this demo setup.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   ./run.sh        # or run.bat on Windows
   ```
3. Browse the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

## Running Tests

```bash
pytest
```

## License

See the [LICENSE](LICENSE) file for details.
