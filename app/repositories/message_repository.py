from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.message import Message

class MessageRepository:
    @staticmethod
    def get_by_id(db: Session, message_id: int) -> Optional[Message]:
        return db.query(Message).filter(Message.id == message_id).first()

    @staticmethod
    def get_by_channel_id_ordered(db: Session, channel_id: int) -> List[Message]:
        return db.query(Message).filter(Message.channel_id == channel_id).order_by(Message.created_at.asc()).all()

    @staticmethod
    def create(db: Session, channel_id: int, author_id: int, content: str) -> Message:
        message = Message(
            channel_id=channel_id,
            author_id=author_id,
            content=content
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    @staticmethod
    def update_content(db: Session, message: Message, new_content: str) -> Message:
        message.content = new_content
        message.edited_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(message)
        return message