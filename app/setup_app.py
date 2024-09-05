from fastapi import FastAPI

from app.routes import base_route



def setup_app() -> FastAPI: 
    app = FastAPI()

    app.include_router(base_route)


    return app
