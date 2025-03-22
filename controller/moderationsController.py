from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="public")

@router.get("/moderations", response_class=HTMLResponse)
async def chat_moderations(request: Request):
    return templates.TemplateResponse("/views/moderations2.html", {"request":request})

'''
@router.get("/moderations", response_class=HTMLResponse)
async def chat_moderations(request: Request):

    #abrir o html
    with open("public/views/moderations.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
'''
