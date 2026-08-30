def test_create_channel_success(client):
    response = client.post("/channels", json={"name": "General"})
    assert response.status_code == 201
    data = response.json()["data"]
    assert data["name"] == "General"
    assert "id" in data
    assert "createdAt" in data

def test_create_channel_duplicate_name_case_insensitive(client):
    client.post("/channels", json={"name": "General"})
    
    # Intento de crear con minuscula debe fallar
    response = client.post("/channels", json={"name": "general"})
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/problem+json"
    
    body = response.json()
    assert body["type"] == "about:blank"
    assert body["status"] == 400
    assert body["title"] == "Bad Request"

def test_create_channel_empty_name_fails(client):
    response = client.post("/channels", json={"name": "   "})
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/problem+json"

def test_list_channels_ordered_by_creation(client):
    client.post("/channels", json={"name": "Channel 1"})
    client.post("/channels", json={"name": "Channel 2"})

    response = client.get("/channels")
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) == 2
    assert data[0]["name"] == "Channel 1"
    assert data[1]["name"] == "Channel 2"