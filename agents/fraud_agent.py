from logger import logger
from mcp_server.tools import get_claim_history, fraud_score

def fraud_agent(state):
    logger.info("🟥 Fraud Agent started")

    claimant_name = state.get("claimant_name", "unknown")
    logger.info(f"Fraud check for claimant: {claimant_name}")

    history = get_claim_history(claimant_name)
    score = fraud_score(history)

    logger.info(f"Claim history: {history}")
    logger.info(f"Fraud score: {score}")

    state["fraud"] = {
        "history": history,
        "score": score
    }

    # human-in-the-loop for fraud
    if score > 0.7:
        state["needs_human_fraud"] = True
        logger.info("Fraud unclear → needs human review")
    else:
        state["needs_human_fraud"] = False

    return state
