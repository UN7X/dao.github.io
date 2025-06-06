from fastapi import FastAPI
from app.core.router import api_router
from app.core.middleware import setup_middleware

app = FastAPI(title="UDAO API PLATFORM", version="1.0.0")
setup_middleware(app)
app.include_router(api_router, prefix="/api", tags=["api"])
