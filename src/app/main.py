from fastapi import FastAPI
from src.app.api.v1.router import api_router as api_router_v1
from src.app.infrastructure.database.session import engine
from src.app.infrastructure.database.base import Base

Base.metadata.create_all(engine)

app = FastAPI()

# add auth route
app.include_router(api_router_v1, prefix="/api/v1")
