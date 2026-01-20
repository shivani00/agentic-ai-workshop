from logger import logger
from mcp_server.tools import get_claim_history, fraud_score

def fraud_agent(state):
    logger.info("🟥 Fraud Agent started")

    name = state["intake"]
    history = get_claim_history(name)
    score = fraud_score(history)

    logger.info(f"Claim history: {history}")
    logger.info(f"Fraud score: {score}")

    state["fraud"] = {"history": history, "score": score}
    state["unclear"] = score > 0.7

    logger.info(f"Is fraud unclear: {state['unclear']}")
    return state
