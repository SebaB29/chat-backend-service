from pydantic import BaseModel, Field

class ErrorResponse(BaseModel):
    type: str = Field(default="about:blank")
    title: str
    status: int
    detail: str
    instance: str