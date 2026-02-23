from fastapi import APIRouter
from chattermate.api.schemas.chat import ChatRequest, ChatResponse
from chattermate.agent.graph import graph

router = APIRouter(tags=["chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    state = await graph.ainvoke({
        "user_id": req.user_id,
        "conversation_id": req.conversation_id,
        "target_language": req.target_language,
        "mode": req.mode,
        "text": req.text,
        "corrections": [],
        "contains_target_language": None,
        "assistant_text": None,
    })

    return ChatResponse(
        conversation_id=state["conversation_id"],
        assistant_text=state["assistant_text"],
        corrections=state["corrections"],
    )
