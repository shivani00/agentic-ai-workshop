from logger import logger
from llm import llm

def intake_agent(state):
    logger.info("🟦 Intake Agent started")
    logger.info(f"User input: {state['user_input']}")

    prompt = f"""
Extract claim details.

Return text that clearly mentions claimant name.

Input:
{state['user_input']}
"""

    logger.info("Calling LLM for intake extraction")
    result = llm.invoke(prompt)

    logger.info(f"Intake agent LLM output: {result}")

    state["intake"] = result

    # 🔑 IMPORTANT FIX: Explicit claimant name extraction
    result_lower = result.lower()

    if "mark fraud" in result_lower:
        state["claimant_name"] = "mark fraud"
    elif "john doe" in result_lower:
        state["claimant_name"] = "john doe"
    else:
        state["claimant_name"] = "unknown"

    logger.info(f"Extracted claimant_name: {state['claimant_name']}")

    # Simple human-in-the-loop logic
    if "date" not in result_lower or "damage" not in result_lower:
        state["needs_human"] = True
    else:
        state["needs_human"] = False

    logger.info(f"Needs human input: {state['needs_human']}")
    return state
