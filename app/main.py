import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.config import settings
from app.database import Base, engine
from app.controllers import channel_controller, message_controller, websocket_controller
from app.exceptions.custom_exceptions import HTTPExceptionRFC7807, rfc7807_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.ENVIRONMENT != "testing":
        Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Chat Service API",
    version="1.0.0",
    lifespan=lifespan
)

# Registrar manejador de errores RFC 7807
app.add_exception_handler(HTTPExceptionRFC7807, rfc7807_exception_handler)

# Incluir Routers API y WS
app.include_router(channel_controller.router)
app.include_router(message_controller.router)
app.include_router(websocket_controller.router)

# Montar archivos estáticos
public_dir = os.path.join(os.path.dirname(__file__), "..", "public")
if os.path.exists(public_dir):
    app.mount("/static", StaticFiles(directory=public_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def get_index():
    index_path = os.path.join(public_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Chat Service API</h1>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=(settings.ENVIRONMENT == "development")
    )