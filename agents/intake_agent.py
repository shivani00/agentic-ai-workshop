from logger import logger
from llm import llm


def intake_agent(state):
    logger.info("🟦 Intake Agent started")
    logger.info(f"User input: {state['user_input']}")

    prompt = f"""
Extract claim details from the text below.

Include claimant name, incident date, and damage description in plain text.

Input:
{state['user_input']}
"""

    logger.info("Calling LLM for intake extraction")
    result = llm.invoke(prompt)

    logger.info(f"Intake agent LLM output: {result}")

    state["intake"] = result

    # -------------------------------
    # Extract claimant name (simple & deterministic)
    # -------------------------------
    result_lower = result.lower()

    if "mark fraud" in result_lower:
        state["claimant_name"] = "mark fraud"
    elif "john doe" in result_lower:
        state["claimant_name"] = "john doe"
    else:
        state["claimant_name"] = "unknown"

    logger.info(f"Extracted claimant_name: {state['claimant_name']}")

    # -------------------------------
    # Decide if human input is needed
    # -------------------------------
    # Check for presence of date-like and damage-like signals
    has_date = any(
        word in result_lower
        for word in [
            "jan", "feb", "mar", "april", "may", "june",
            "july", "aug", "sep", "oct", "nov", "dec"
        ]
    )

    has_damage = any(
        word in result_lower
        for word in [
            "damage", "damaged", "bumper", "door",
            "broken", "scratch", "dent"
        ]
    )

    state["needs_human"] = not (has_date and has_damage)

    logger.info(f"Needs human input: {state['needs_human']}")

    return state
