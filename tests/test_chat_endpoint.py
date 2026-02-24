import pytest
from fastapi.testclient import TestClient
from chattermate.main import app

client = TestClient(app)


def test_chat_returns_200():
    response = client.post("/chat", json={"text": "Hello"})
    assert response.status_code == 200


def test_chat_response_has_required_fields():
    body = client.post("/chat", json={"text": "Hello"}).json()
    assert "conversation_id" in body
    assert "assistant_text" in body
    assert "corrections" in body


def test_chat_corrections_is_list():
    body = client.post("/chat", json={"text": "Hello"}).json()
    assert isinstance(body["corrections"], list)


def test_chat_preserves_conversation_id():
    conv_id = "test-conv-123"
    body = client.post("/chat", json={"text": "Hello", "conversation_id": conv_id}).json()
    assert body["conversation_id"] == conv_id


def test_chat_missing_text_returns_422():
    response = client.post("/chat", json={})
    assert response.status_code == 422


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
