from app.repositories.message_repository import MessageRepository

def test_get_messages_non_existent_channel_fails(client):
    response = client.get("/channels/999/messages")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/problem+json"
    
    body = response.json()
    assert body["status"] == 404
    assert body["title"] == "Channel Not Found"

def test_get_messages_empty_channel_success(client):
    channel_resp = client.post("/channels", json={"name": "General"})
    channel_id = channel_resp.json()["data"]["id"]

    response = client.get(f"/channels/{channel_id}/messages")
    assert response.status_code == 200
    assert response.json()["data"] == []

def test_get_messages_ordered_by_creation(db_session, client):
    channel_resp = client.post("/channels", json={"name": "General"})
    channel_id = channel_resp.json()["data"]["id"]

    # Creamos mensajes directamente en la BD
    MessageRepository.create(db_session, channel_id=channel_id, author_id=1, content="Primer mensaje")
    MessageRepository.create(db_session, channel_id=channel_id, author_id=2, content="Segundo mensaje")

    response = client.get(f"/channels/{channel_id}/messages")
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 2
    assert data[0]["content"] == "Primer mensaje"
    assert data[0]["channelId"] == channel_id
    assert data[1]["content"] == "Segundo mensaje"