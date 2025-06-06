# ASIX

`/api/v1/asix` provides simple lockers for JSON objects.

- **POST `/lockers`** – create a new locker and receive its ID
- **POST `/lockers/{id}/objects`** – store an object and get an object ID
- **GET `/lockers/{id}/objects/{obj}`** – retrieve stored object
- **PUT `/lockers/{id}/objects/{obj}`** – replace stored object
- **DELETE `/lockers/{id}/objects/{obj}`** – remove object
- **POST `/lockers/{id}/keys`** – generate an optional access key

Health checks are available at `/lockers/health`.
