import pytest

def test_websocket_send_and_receive_message(client):
    # 1. Crear canal
    channel_resp = client.post("/channels", json={"name": "General WS"})
    channel_id = channel_resp.json()["data"]["id"]

    # 2. Conectar cliente WS
    with client.websocket_connect(f"/ws/channels/{channel_id}") as websocket:
        # Enviar mensaje
        send_payload = {
            "action": "SEND_MESSAGE",
            "data": {
                "authorId": 10,
                "content": "Hola por WebSocket"
            }
        }
        websocket.send_json(send_payload)

        # Recibir broadcast
        response = websocket.receive_json()
        assert response["event"] == "MESSAGE_CREATED"
        assert response["data"]["content"] == "Hola por WebSocket"
        assert response["data"]["authorId"] == 10
        assert response["data"]["channelId"] == channel_id

def test_websocket_edit_message(client):
    channel_resp = client.post("/channels", json={"name": "Edit WS"})
    channel_id = channel_resp.json()["data"]["id"]

    with client.websocket_connect(f"/ws/channels/{channel_id}") as websocket:
        # Crear mensaje
        websocket.send_json({
            "action": "SEND_MESSAGE",
            "data": {"authorId": 10, "content": "Mensaje Original"}
        })
        created_event = websocket.receive_json()
        msg_id = created_event["data"]["id"]

        # Editar mensaje
        websocket.send_json({
            "action": "EDIT_MESSAGE",
            "data": {"id": msg_id, "content": "Mensaje Editado"}
        })
        updated_event = websocket.receive_json()
        assert updated_event["event"] == "MESSAGE_UPDATED"
        assert updated_event["data"]["content"] == "Mensaje Editado"
        assert updated_event["data"]["editedAt"] is not None