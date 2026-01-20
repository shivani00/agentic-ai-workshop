from logger import logger
from llm import llm

def confidence_agent(state):
    logger.info("🟨 Confidence Agent started")

    prompt = f"""
You are an insurance claim decision agent.

Your task is to decide APPROVED or REJECTED.

IMPORTANT RULES (MUST FOLLOW):
1. If fraud score is LOW (< 0.5) and policy is compliant, the claim should normally be APPROVED.
2. If fraud score is HIGH (> 0.7), the claim should normally be REJECTED unless there is a strong justification.
3. Human fraud input (if present) should strongly influence the decision.
4. The decision label MUST match the explanation.
5. Do NOT contradict yourself.

Inputs:
- Claim details: {state['intake']}
- Compliance result: {state['compliance']}
- Fraud analysis: {state['fraud']}
- Human fraud review: {state.get('human_fraud_decision', 'not provided')}

Decision instructions:
- Choose exactly one: APPROVED or REJECTED
- Provide confidence between 0 and 1
- Explanation must clearly justify the decision

Return ONLY valid JSON in this format:
{{
  "decision": "APPROVED or REJECTED",
  "confidence": 0.0–1.0,
  "explanation": "..."
}}
"""

    logger.info("Calling LLM for final decision")
    result = llm.invoke(prompt)

    logger.info(f"Final decision: {result}")
    state["final"] = result
    return state
