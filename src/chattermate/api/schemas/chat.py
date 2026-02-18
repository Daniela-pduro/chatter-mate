from pydantic import BaseModel, Field
from typing import Literal, Optional
from uuid import uuid4


Mode = Literal["casual", "professional"]


class ChatRequest(BaseModel):
    user_id: str = Field(default="anon")
    conversation_id: str = Field(default_factory=lambda: str(uuid4()))
    target_language: str = Field(default="en", description="BCP-47-ish code like 'en', 'fr', 'de'")
    mode: Mode = Field(default="casual")
    text: str = Field(..., min_length=1)


class Correction(BaseModel):
    original: str
    corrected: str
    explanation: Optional[str] = None


class ChatResponse(BaseModel):
    conversation_id: str
    assistant_text: str
    corrections: list[Correction] = Field(default_factory=list)
