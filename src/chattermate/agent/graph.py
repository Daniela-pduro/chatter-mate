from langgraph.graph import StateGraph, END
from chattermate.agent.state import AgentState
from chattermate.agent.nodes import detect_language, detect_errors, generate_response

builder = StateGraph(AgentState)

builder.add_node("detect_language", detect_language)
builder.add_node("detect_errors", detect_errors)
builder.add_node("generate_response", generate_response)

builder.set_entry_point("detect_language")

builder.add_conditional_edges(
    "detect_language",
    lambda state: "detect_errors" if state.get("contains_target_language") else "generate_response",
)

builder.add_edge("detect_errors", "generate_response")
builder.add_edge("generate_response", END)

graph = builder.compile()
