from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/study_js", response_class=HTMLResponse)
async def home_page(request: Request):

    #abrir o html
    with open("public/views/study-js.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

