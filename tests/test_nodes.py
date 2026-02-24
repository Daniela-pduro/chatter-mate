import pytest
from chattermate.agent.nodes import detect_language, detect_errors, generate_response


@pytest.fixture
def base_state():
    return {
        "user_id": "test_user",
        "conversation_id": "test-conv-id",
        "target_language": "en",
        "mode": "casual",
        "text": "Hello, how are you?",
        "corrections": [],
        "contains_target_language": None,
        "assistant_text": None,
    }


def test_detect_language_sets_contains_target_language(base_state):
    result = detect_language(base_state)
    assert "contains_target_language" in result
    assert isinstance(result["contains_target_language"], bool)


def test_detect_errors_returns_corrections_and_response(base_state):
    result = detect_errors(base_state)
    assert "corrections" in result
    assert isinstance(result["corrections"], list)
    assert "assistant_text" in result
    assert isinstance(result["assistant_text"], str)


def test_detect_errors_response_contains_user_text(base_state):
    result = detect_errors(base_state)
    assert base_state["text"] in result["assistant_text"]


def test_generate_response_returns_empty_dict(base_state):
    result = generate_response(base_state)
    assert result == {}
