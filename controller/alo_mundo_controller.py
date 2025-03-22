from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/api/alo-mundo", response_class=HTMLResponse)
async def alo_mundo(request: Request):

    #abrir o html
    with open("public/views/alo-mundo.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
