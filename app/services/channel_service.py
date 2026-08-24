from typing import List
from sqlalchemy.orm import Session
from app.repositories.channel_repository import ChannelRepository
from app.models.channel import Channel
from app.schemas.channel import CreateChannelRequest
from app.exceptions.custom_exceptions import HTTPExceptionRFC7807

class ChannelService:
    @staticmethod
    def create_channel(db: Session, request: CreateChannelRequest) -> Channel:
        name = request.name.strip()
        if not name:
            raise HTTPExceptionRFC7807(
                status_code=400,
                title="Bad Request",
                detail="Channel name cannot be empty."
            )
        
        existing_channel = ChannelRepository.get_by_name_case_insensitive(db, name)
        if existing_channel:
            raise HTTPExceptionRFC7807(
                status_code=400,
                title="Bad Request",
                detail=f"A channel with the name '{name}' already exists."
            )

        return ChannelRepository.create(db, name)

    @staticmethod
    def list_channels(db: Session) -> List[Channel]:
        return ChannelRepository.get_all_ordered_by_creation(db)

    @staticmethod
    def get_channel_by_id(db: Session, channel_id: int) -> Channel:
        channel = ChannelRepository.get_by_id(db, channel_id)
        if not channel:
            raise HTTPExceptionRFC7807(
                status_code=404,
                title="Channel Not Found",
                detail=f"The channel with ID {channel_id} was not found."
            )
        return channel