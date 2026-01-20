from rag.vectorstore import vectorstore
from llm import llm

def compliance_agent(state):
    docs = vectorstore.similarity_search("auto accident coverage", k=3)
    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
Policy rules:
{context}

Claim:
{state['intake']}

Return JSON:
- compliant (true/false)
- reason
"""
    state["compliance"] = llm.invoke(prompt)
    return state
