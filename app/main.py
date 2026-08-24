from contextlib import asynccontextmanager
from fastapi import FastAPI
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

app.add_exception_handler(HTTPExceptionRFC7807, rfc7807_exception_handler)

app.include_router(channel_controller.router)
app.include_router(message_controller.router)
app.include_router(websocket_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=(settings.ENVIRONMENT == "development")
    )