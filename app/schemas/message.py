from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MessageResponse(BaseModel):
    id: int
    channelId: int = Field(..., alias="channel_id")
    authorId: int = Field(..., alias="author_id")
    content: str = Field(..., min_length=1, max_length=2000)
    createdAt: datetime = Field(..., alias="created_at")
    editedAt: Optional[datetime] = Field(None, alias="edited_at")

    class Config:
        from_attributes = True
        populate_by_name = True

class MessageListResponse(BaseModel):
    data: list[MessageResponse]

class SendOrEditMessageEvent(BaseModel):
    id: Optional[int] = None
    authorId: int = Field(..., alias="author_id")
    content: str = Field(..., min_length=1, max_length=2000)

    class Config:
        populate_by_name = True