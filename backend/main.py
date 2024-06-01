from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend import utils
from backend.routes import chat_router
from backend.settings.settings import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(router: FastAPI):
    tokenizer, model = utils.load_models(settings.embedding_model)
    chatbot = utils.load_chatbot(settings.chatbot_model)
    router.state.tokenizer = tokenizer
    router.state.model = model
    router.state.chatbot = chatbot
    print("ML model loaded")
    yield
    del router.state.tokenizer
    del router.state.model
    del router.state.chatbot
    print("ML model unloaded")


app = FastAPI(
    title="Assistant API",
    description="Tinkoff Business Helper",
    version="0.1.0",
    redoc_url=None,
    docs_url='/',
    lifespan=lifespan
)

app.include_router(
    chat_router,
)
