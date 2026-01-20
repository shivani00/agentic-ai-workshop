from mcp_server.tools import get_claim_history, fraud_score

def fraud_agent(state):
    name = state["intake"]
    history = get_claim_history(name)
    score = fraud_score(history)

    state["fraud"] = {
        "history": history,
        "score": score
    }
    state["unclear"] = score > 0.7
    return state
