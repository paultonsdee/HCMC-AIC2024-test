from fastapi import FastAPI

from app.routes import base_route

app = FastAPI()

app.include_router(base_route)
