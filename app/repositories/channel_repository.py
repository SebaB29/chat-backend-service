from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.channel import Channel

class ChannelRepository:
    @staticmethod
    def get_by_id(db: Session, channel_id: int) -> Optional[Channel]:
        return db.query(Channel).filter(Channel.id == channel_id).first()

    @staticmethod
    def get_by_name_case_insensitive(db: Session, name: str) -> Optional[Channel]:
        return db.query(Channel).filter(func.lower(Channel.name) == func.lower(name)).first()

    @staticmethod
    def get_all_ordered_by_creation(db: Session) -> List[Channel]:
        return db.query(Channel).order_by(Channel.created_at.asc()).all()

    @staticmethod
    def create(db: Session, name: str) -> Channel:
        channel = Channel(name=name)
        db.add(channel)
        db.commit()
        db.refresh(channel)
        return channel