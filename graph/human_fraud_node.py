from logger import logger

def human_fraud_input(state):
    logger.info("🧑 Human fraud review requested")

    print("\n⚠️ Fraud detected. Please confirm:")
    print("Is this claim legitimate? (yes/no)")

    answer = input(">> ").strip().lower()

    state["human_fraud_decision"] = answer
    state["needs_human_fraud"] = False

    logger.info(f"Human fraud decision: {answer}")
    return state
