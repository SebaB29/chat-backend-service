from fastapi import Request
from fastapi.responses import JSONResponse
from app.schemas.error import ErrorResponse

class HTTPExceptionRFC7807(Exception):
    def __init__(self, status_code: int, title: str, detail: str):
        self.status_code = status_code
        self.title = title
        self.detail = detail

async def rfc7807_exception_handler(request: Request, exc: HTTPExceptionRFC7807):
    error_payload = ErrorResponse(
        type="about:blank",
        title=exc.title,
        status=exc.status_code,
        detail=exc.detail,
        instance=request.url.path
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_payload.model_dump(),
        media_type="application/problem+json"
    )