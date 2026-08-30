from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.channel import CreateChannelRequest, ChannelResponse, ChannelListResponse
from app.services.channel_service import ChannelService

router = APIRouter(prefix="/channels", tags=["channels"])

@router.post(
    "",
    response_model=dict[str, ChannelResponse],
    status_code=status.HTTP_201_CREATED
)
def create_channel(request: CreateChannelRequest, db: Session = Depends(get_db)):
    channel = ChannelService.create_channel(db, request)
    return {"data": ChannelResponse.model_validate(channel)}

@router.get(
    "",
    response_model=ChannelListResponse,
    status_code=status.HTTP_200_OK
)
def list_channels(db: Session = Depends(get_db)):
    channels = ChannelService.list_channels(db)
    return ChannelListResponse(
        data=[ChannelResponse.model_validate(c) for c in channels]
    )