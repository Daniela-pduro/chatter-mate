from chattermate.agent.state import AgentState


def detect_language(state: AgentState) -> dict:
    # mock: assumes the message always contains target language
    # real: 1 LLM call — detects if message contains target_language
    # if not, also generates the encouragement response directly
    return {"contains_target_language": True}


def detect_errors(state: AgentState) -> dict:
    # mock: no errors detected, fixed response
    # real: 1 LLM call — detects errors + generates conversational response
    return {
        "corrections": [],
        "assistant_text": f"(mock) You said: {state['text']}",
    }


def generate_response(state: AgentState) -> dict:
    # no LLM call — assembles the final response from state
    # if contains_target_language: assistant_text already set by detect_errors
    # if not: assistant_text already set by detect_language
    return {}
