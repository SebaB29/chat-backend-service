import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.websockets.connection_manager import manager
from app.repositories.channel_repository import ChannelRepository
from app.repositories.message_repository import MessageRepository
from app.schemas.message import MessageResponse

router = APIRouter(prefix="/ws", tags=["websockets"])

@router.websocket("/channels/{channel_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: int, db: Session = Depends(get_db)):
    # Validar que el canal exista antes de conectar
    channel = ChannelRepository.get_by_id(db, channel_id)
    if not channel:
        await websocket.close(code=4004, reason="Channel not found")
        return

    await manager.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            event_type = payload.get("action") or payload.get("type")
            event_data = payload.get("data", {})

            if event_type == "SEND_MESSAGE":
                author_id = event_data.get("authorId")
                content = event_data.get("content", "").strip()

                if author_id and content:
                    msg = MessageRepository.create(db, channel_id, author_id, content)
                    msg_dto = MessageResponse.model_validate(msg).model_dump(mode="json", by_alias=True)
                    
                    broadcast_payload = {
                        "event": "MESSAGE_CREATED",
                        "data": msg_dto
                    }
                    await manager.broadcast_to_channel(channel_id, broadcast_payload)

            elif event_type == "EDIT_MESSAGE":
                message_id = event_data.get("id")
                content = event_data.get("content", "").strip()

                if message_id and content:
                    msg = MessageRepository.get_by_id(db, message_id)
                    if msg and msg.channel_id == channel_id:
                        updated_msg = MessageRepository.update_content(db, msg, content)
                        msg_dto = MessageResponse.model_validate(updated_msg).model_dump(mode="json", by_alias=True)
                        
                        broadcast_payload = {
                            "event": "MESSAGE_UPDATED",
                            "data": msg_dto
                        }
                        await manager.broadcast_to_channel(channel_id, broadcast_payload)

    except WebSocketDisconnect:
        manager.disconnect(websocket, channel_id)
    except Exception:
        manager.disconnect(websocket, channel_id)