__version__ = "0.0.0"
__author__ = "MinLee0210"

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import base_route

def setup_app() -> FastAPI: 
    app = FastAPI()
    app.include_router(base_route)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app
