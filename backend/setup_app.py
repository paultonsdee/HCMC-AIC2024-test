__version__ = "0.0.0"
__author__ = "MinLee0210"

from fastapi import FastAPI

from backend.routes import base_route

def setup_app() -> FastAPI: 
    app = FastAPI()
    app.include_router(base_route)

    return app
