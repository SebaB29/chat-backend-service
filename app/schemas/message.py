from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class MessageResponse(BaseModel):
    id: int
    channel_id: int = Field(..., serialization_alias="channelId")
    author_id: int = Field(..., serialization_alias="authorId")
    content: str = Field(..., min_length=1, max_length=2000)
    created_at: datetime = Field(..., serialization_alias="createdAt")
    edited_at: Optional[datetime] = Field(None, serialization_alias="editedAt")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class MessageListResponse(BaseModel):
    data: list[MessageResponse]

class SendOrEditMessageEvent(BaseModel):
    id: Optional[int] = None
    author_id: int = Field(..., alias="authorId")
    content: str = Field(..., min_length=1, max_length=2000)

    model_config = ConfigDict(
        populate_by_name=True
    )