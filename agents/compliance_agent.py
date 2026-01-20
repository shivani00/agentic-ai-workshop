from logger import logger
from rag.vectorstore import vectorstore
from llm import llm

def compliance_agent(state):
    logger.info("🟩 Compliance Agent started")

    docs = vectorstore.similarity_search("auto accident coverage", k=2)
    logger.info(f"Retrieved {len(docs)} policy documents")

    context = "\n".join(d.page_content for d in docs)

    logger.info("Calling LLM for compliance decision")
    result = llm.invoke(
        f"""
Policy rules:
{context}

Claim:
{state['intake']}

Return JSON:
- compliant
- reason
"""
    )

    logger.info(f"Compliance result: {result}")
    state["compliance"] = result
    return state
