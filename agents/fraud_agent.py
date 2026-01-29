from logger import logger
from mcp_server.tools import get_claim_history, fraud_score


def fraud_agent(state):
    logger.info("🟥 Fraud Agent started")

    claimant_name = state.get("claimant_name", "unknown")
    logger.info(f"Fraud check for claimant: {claimant_name}")

    history = get_claim_history(claimant_name)
    score = fraud_score(history)

    is_high_risk = score >= 0.7

    state["fraud"] = {
        "history": history,
        "score": score,
        "is_high_risk": is_high_risk
    }

    state["needs_human_fraud"] = is_high_risk

    logger.info(f"Fraud history: {history}")
    logger.info(f"Fraud score: {score}")
    logger.info(f"High risk fraud: {is_high_risk}")

    return state
