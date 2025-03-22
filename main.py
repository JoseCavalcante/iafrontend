from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # importando para preparar a montagem
from controller.home_page_controller import router as api_homepage
from controller.chatController import router as api_chat_completion
from controller.moderationsController import router as api_moderations
from controller.ttsController import router as api_tts
from controller.sttController import router as api_stt
from controller.imageController import router as api_image
from controller.studyjscontroller import router as api_studyjs

app = FastAPI()

app.include_router(api_homepage)
app.include_router(api_chat_completion)
app.include_router(api_moderations)
app.include_router(api_tts)
app.include_router(api_stt)
app.include_router(api_image)
app.include_router(api_studyjs)

# a montagem dos arquivos estaticos (arquivos html, css, js, imagens, audiso etc)
app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")