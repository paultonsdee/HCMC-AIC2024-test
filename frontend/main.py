import uvicorn

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
def get_landing_page(request: Request): 
    return templates.TemplateResponse(
        name="index.html", request=request, 
    )

@app.get("/search",  response_class=HTMLResponse)
def get_search_page(request: Request): 
    return templates.TemplateResponse(
        name="search-page.html", request=request, 
    )



@app.post("/search/text")
def post_search_text(): 
    ...

@app.post("/search/image")
def post_search_image(): 
    ...



# @app.post("/search/text")
# def post_search_text(): 
#     ...


if __name__ == "__main__": 
    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=8000, 
                reload=True)