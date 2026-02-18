from fastapi import APIRouter
from chattermate.api.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(tags=["chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    # we'll invoke the LangGraph agent here later
    assistant_text = f"(stub) You said: {req.text}"
    return ChatResponse(
        conversation_id=req.conversation_id,
        assistant_text=assistant_text,
        corrections=[],
    )