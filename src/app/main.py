from fastapi import FastAPI
from src.app.api.v1.router import api_router as api_router_v1

app = FastAPI()

app.include_router(api_router_v1, prefix="/api/v1")
