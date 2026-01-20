from langgraph.graph import StateGraph
from agents.intake_agent import intake_agent
from agents.compliance_agent import compliance_agent
from agents.fraud_agent import fraud_agent
from agents.confidence_agent import confidence_agent

graph = StateGraph(dict)

graph.add_node("intake", intake_agent)
graph.add_node("compliance", compliance_agent)
graph.add_node("fraud", fraud_agent)
graph.add_node("final", confidence_agent)

graph.set_entry_point("intake")

graph.add_conditional_edges(
    "intake",
    lambda s: "intake" if s["needs_human"] else "compliance"
)

graph.add_edge("compliance", "fraud")

graph.add_conditional_edges(
    "fraud",
    lambda s: "fraud" if s["unclear"] else "final"
)

graph.set_finish_point("final")

claim_graph = graph.compile()
