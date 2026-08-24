from pydantic import BaseModel, Field
from datetime import datetime

class CreateChannelRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class ChannelResponse(BaseModel):
    id: int
    name: str
    createdAt: datetime = Field(..., alias="created_at")

    class Config:
        from_attributes = True
        populate_by_name = True

class ChannelListResponse(BaseModel):
    data: list[ChannelResponse]