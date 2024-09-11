import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def get_landing_page(request: Request): 
    try: 
        quote = requests.get("http://localhost:8000/base/").json()
        quote = quote['msg']

    except: 
        quote = """"He who would learn to fly one day must first learn to stand and walk and run and climb and dance; one cannot fly into flying." — Nietzsche"""
    return templates.TemplateResponse(
        name="index.html", request=request, 
        context={
            "quote": quote
        } 
    )

@app.get("/search",  response_class=HTMLResponse)
async def get_search_page(request: Request): 
    return templates.TemplateResponse(
        name="search-page.html", 
        request=request,

    )



@app.post("/search/text")
async def post_search_text(): 
    ...

@app.post("/search/image")
async def post_search_image(): 
    ...



# @app.post("/search/text")
# def post_search_text(): 
#     ...


# if __name__ == "__main__": 
#     uvicorn.run("main:app", 
#                 host="0.0.0.0", 
#                 port=5000, 
#                 reload=True)