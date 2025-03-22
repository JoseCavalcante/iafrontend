from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="public")


@router.get("/image", response_class=HTMLResponse)
async def image(request: Request):
    return templates.TemplateResponse("/views/image2.html", {"request":request})

'''
@router.get("/image", response_class=HTMLResponse)
async def image(request: Request):

    #abrir o html
    with open("public/views/image.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
'''
