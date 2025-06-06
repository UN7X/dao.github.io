# UDAO API Platform

Welcome to the documentation for the UDAO API Platform. This project exposes a few
small services built with [FastAPI](https://fastapi.tiangolo.com/) that are used
by the U-DAO community. Use the guides below to get up and running quickly.

## Available Services

- **Timestamped** – sign content with a server timestamp
- **HashCache** – record file hashes with optional metadata
- **ASIX** – store JSON objects in ephemeral lockers

Each service has a dedicated API endpoint under `/api/v1/` and simple health
checks for monitoring.

For a live, interactive view of the API, start the server and open `/docs` in
your browser.
