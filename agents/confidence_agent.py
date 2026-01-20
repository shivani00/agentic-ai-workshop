from logger import logger
from llm import llm

def confidence_agent(state):
    logger.info("🟨 Confidence Agent started")

    logger.info("Calling LLM for final decision")
    result = llm.invoke(
        f"""
Compliance: {state['compliance']}
Fraud: {state['fraud']}

Return JSON:
- decision
- confidence
- explanation
"""
    )

    logger.info(f"Final decision: {result}")
    state["final"] = result
    return state
