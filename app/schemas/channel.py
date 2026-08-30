from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class CreateChannelRequest(BaseModel):
    name: str

class ChannelResponse(BaseModel):
    id: int
    name: str
    created_at: datetime = Field(..., serialization_alias="createdAt")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class ChannelListResponse(BaseModel):
    data: list[ChannelResponse]