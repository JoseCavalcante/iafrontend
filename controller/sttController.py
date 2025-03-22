from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="public")

@router.get("/stt", response_class=HTMLResponse)
async def chat_completion(request: Request):
    return templates.TemplateResponse("/views/stt2.html", {"request":request})

'''
@router.get("/stt", response_class=HTMLResponse)
async def stt(request: Request):

    #abrir o html
    with open("public/views/stt.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
'''
