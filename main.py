from graph.claim_graph import claim_graph

state = {
    "user_input": "Initiate claim for John Doe. Car accident."
}

result = claim_graph.invoke(state)

print("\n✅ FINAL RESULT")
print(result["final_decision"])
