from fastapi import FastAPI
from .api.routes.health import router as health_router
from .api.routes.chat import router as chat_router

def create_app() -> FastAPI:
    app = FastAPI(title="ChatterMate")
    app.include_router(health_router)
    app.include_router(chat_router)
    return app

app = create_app()
