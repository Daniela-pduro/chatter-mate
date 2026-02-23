from typing import Optional
from typing_extensions import TypedDict
from chattermate.api.schemas.chat import Correction


class AgentState(TypedDict):
    # -- input (populated from ChatRequest) --
    user_id: str
    conversation_id: str
    target_language: str
    mode: str
    text: str

    # -- detect_language --
    contains_target_language: Optional[bool]

    # -- detect_errors --
    corrections: list[Correction]

    # -- generate_response / encourage --
    assistant_text: Optional[str]
