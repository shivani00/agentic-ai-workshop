from llm import llm

def intake_agent(state):
    prompt = f"""
Extract JSON fields:
- claimant_name
- incident_type
- incident_date
- damage_type

If any missing, set complete=false.

Input:
{state["user_input"]}
"""
    result = llm.invoke(prompt)
    state["intake"] = result
    state["needs_human"] = "complete\": false" in result.lower()
    return state
