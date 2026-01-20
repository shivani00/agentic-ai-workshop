from logger import logger
from llm import llm

def intake_agent(state):
    logger.info("🟦 Intake Agent started")
    logger.info(f"User input: {state['user_input']}")

    logger.info("Calling LLM for intake extraction")
    result = llm.invoke(
        f"""
Extract JSON fields:
- claimant_name
- incident_type
- incident_date
- damage_type
If any missing, set complete=false.

Input:
{state['user_input']}
"""
    )

    logger.info(f"Intake agent LLM output: {result}")

    state["intake"] = result
    state["needs_human"] = "complete\": false" in result.lower()

    logger.info(f"Needs human input: {state['needs_human']}")
    return state
