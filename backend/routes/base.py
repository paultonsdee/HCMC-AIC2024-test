
from fastapi import APIRouter, HTTPException

from backend.api.base import translate_to_en, talk_to_llm

base_route = APIRouter(
    prefix="/base"
)

@base_route.get("/")
async def get_opening_line():
    return {"msg": "Hello world"}


@base_route.get("/translate/{input}")
async def translate(input:str): 
    try: 
        result = translate_to_en(input=input)
        print(result)
        return {"msg": result}
    except HTTPException as httpe: 
        raise HTTPException(status_code=404, 
                            detail="Get something wrong from the function") from httpe

@base_route.get('/llm/{prompt}')
async def llm_complete(prompt:str): 
    try: 
        result = talk_to_llm(prompt=prompt)
        return {"msg": result}
    except HTTPException as httpe: 
        raise HTTPException(status_code=404, 
                            detail="Get something wrong from the function") from httpe