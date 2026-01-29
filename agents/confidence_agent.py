from logger import logger
from llm import llm
import json


def confidence_agent(state):
    logger.info("🟨 Confidence Agent started")

    fraud = state["fraud"]
    compliance = state["compliance"]
    human_fraud = state.get("human_fraud_decision", "not provided")

    # -------------------------------
    # HARD RULE ENFORCEMENT (NO LLM)
    # -------------------------------
    if human_fraud == "no":
        final = {
            "decision": "REJECTED",
            "confidence": 1.0,
            "explanation": "Claim rejected due to human fraud reviewer marking the claim as illegitimate."
        }
        state["final"] = final
        return state

    if fraud["is_high_risk"]:
        final = {
            "decision": "REJECTED",
            "confidence": 0.95,
            "explanation": "Claim rejected due to high fraud risk score."
        }
        state["final"] = final
        return state

    # -------------------------------
    # LLM ONLY FOR LOW-RISK CASES
    # -------------------------------
    prompt = f"""
You are a claim decision explanation agent.

The decision is already APPROVED.

Explain the approval clearly and consistently.

Inputs:
- Claim details: {state['intake']}
- Compliance: {compliance}
- Fraud score: {fraud["score"]}

Return ONLY valid JSON:
{{
  "decision": "APPROVED",
  "confidence": 0.0–1.0,
  "explanation": "clear justification"
}}
"""

    result = llm.invoke(prompt)
    logger.info(f"LLM approval explanation: {result}")

    try:
        state["final"] = json.loads(result)
    except Exception:
        state["final"] = {
            "decision": "APPROVED",
            "confidence": 0.9,
            "explanation": "Claim approved based on low fraud risk and policy compliance."
        }

    return state
