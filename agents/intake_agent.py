from logger import logger
from llm import llm
import json


def intake_agent(state):
    logger.info("🟦 Intake Agent started")
    logger.info(f"User input: {state['user_input']}")

    prompt = f"""
Extract claim details from the text below.

Return ONLY valid JSON in this format:
{{
  "claimant_name": "full name exactly as written",
  "incident_date": "date",
  "damage_description": "description",
  "severity": "LOW | MEDIUM | HIGH"
}}

Rules:
- Severity is HIGH if damage is total, complete, severe, destroyed, or vehicle is not drivable
- Severity is MEDIUM for partial damage such as bumper, door, scratches
- Severity is LOW for cosmetic or very minor issues
- Preserve the full claimant name exactly

Input:
{state['user_input']}
"""

    result = llm.invoke(prompt)
    logger.info(f"Intake raw output: {result}")

    try:
        parsed = json.loads(result)
    except Exception as e:
        logger.error(f"Intake JSON parse failed: {e}")
        parsed = {
            "claimant_name": "unknown",
            "incident_date": "unknown",
            "damage_description": "unknown",
            "severity": "UNKNOWN"
        }

    state["intake"] = parsed
    state["claimant_name"] = parsed["claimant_name"].lower().strip()

    logger.info(f"Claimant: {state['claimant_name']}")
    logger.info(f"Severity: {parsed['severity']}")

    return state
