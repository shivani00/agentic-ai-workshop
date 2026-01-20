from llm import llm

def confidence_agent(state):
    prompt = f"""
Inputs:
Compliance: {state['compliance']}
Fraud: {state['fraud']}

Decide APPROVE or REJECT.
Return JSON:
- decision
- confidence (0-1)
- explanation
"""
    state["final"] = llm.invoke(prompt)
    return state
