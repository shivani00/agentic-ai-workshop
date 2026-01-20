from langgraph.graph import StateGraph
from agents.intake_agent import intake_agent
from agents.compliance_agent import compliance_agent
from agents.fraud_agent import fraud_agent
from agents.confidence_agent import confidence_agent
from graph.human_fraud_node import human_fraud_input

graph = StateGraph(dict)

graph.add_node("intake", intake_agent)
graph.add_node("compliance", compliance_agent)
graph.add_node("fraud", fraud_agent)
graph.add_node("human_fraud", human_fraud_input)
graph.add_node("final", confidence_agent)

graph.set_entry_point("intake")

graph.add_edge("intake", "compliance")
graph.add_edge("compliance", "fraud")

graph.add_conditional_edges(
    "fraud",
    lambda s: "human_fraud" if s["needs_human_fraud"] else "final"
)

graph.add_edge("human_fraud", "final")

graph.set_finish_point("final")

claim_graph = graph.compile()
