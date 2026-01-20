import streamlit as st
from graph.claim_graph import claim_graph

st.title("🧠 Agentic Claims Workshop")

user_input = st.text_area("Enter claim:")

if st.button("Submit"):
    state = {"user_input": user_input}
    result = claim_graph.invoke(state)
    st.json(result["final"])
