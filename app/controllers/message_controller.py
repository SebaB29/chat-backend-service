from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.message import MessageListResponse, MessageResponse
from app.services.message_service import MessageService

router = APIRouter(prefix="/channels", tags=["messages"])

@router.get(
    "/{channel_id}/messages",
    response_model=MessageListResponse,
    status_code=status.HTTP_200_OK
)
def get_channel_messages(channel_id: int, db: Session = Depends(get_db)):
    messages = MessageService.get_messages_by_channel(db, channel_id)
    return MessageListResponse(
        data=[MessageResponse.model_validate(m) for m in messages]
    )