from typing import List
from sqlalchemy.orm import Session
from app.repositories.message_repository import MessageRepository
from app.services.channel_service import ChannelService
from app.models.message import Message

class MessageService:
    @staticmethod
    def get_messages_by_channel(db: Session, channel_id: int) -> List[Message]:
        # Lanza HTTPExceptionRFC7807 (404) si el canal no existe
        ChannelService.get_channel_by_id(db, channel_id)
        return MessageRepository.get_by_channel_id_ordered(db, channel_id)