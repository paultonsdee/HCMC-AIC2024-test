from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates", response_class=HTMLResponse)


@app.get("/")
def get_landing_page(request: Request): 
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/search")
def get_search_page(): 
    ...


@app.post("/search/text")
def post_search_text(): 
    ...

@app.post("/search/image")
def post_search_image(): 
    ...



# @app.post("/search/text")
# def post_search_text(): 
#     ...