from fastapi import FastAPI

from .routes import chat_router

app = FastAPI(
    title="Assistant API",
    description="Tinkoff Business Helper",
    version="0.1.0",
    redoc_url=None,
    docs_url='/'
)


app.include_router(
    chat_router,
)
