import uvicorn

from fastapi import FastAPI

from app.routes import base_route

app = FastAPI()

app.include_router(base_route)


@app.get("/")
async def root():
    return {"message": "Welcome to OmniLens"}


if __name__ == "__main__": 
    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level="info", 
                reload=True
                )