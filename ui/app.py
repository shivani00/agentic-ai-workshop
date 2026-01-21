import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from graph.claim_graph import claim_graph

st.set_page_config(page_title="Agentic Claims Demo", layout="centered")
st.title("🧠 Agentic Insurance Claims Demo")

# -------------------------
# Initialize session state
# -------------------------
if "state" not in st.session_state:
    st.session_state.state = {}

if "result" not in st.session_state:
    st.session_state.result = None

# -------------------------
# Claim input
# -------------------------
st.subheader("Enter Claim")

user_input = st.text_area(
    "Claim description",
    placeholder="Initiate claim for John Doe. Car accident on 5 Jan. Front bumper damaged."
)

if st.button("Submit Claim"):
    st.session_state.state = {
        "user_input": user_input
    }
    st.session_state.result = claim_graph.invoke(st.session_state.state)

# -------------------------
# Human-in-the-loop (Fraud)
# -------------------------
if st.session_state.result and st.session_state.result.get("needs_human_fraud"):

    st.warning("⚠️ Fraud detected. Human review required.")

    human_decision = st.radio(
        "Is this claim legitimate?",
        options=["yes", "no"]
    )

    if st.button("Submit Human Review"):
        st.session_state.state["human_fraud_decision"] = human_decision
        st.session_state.state["needs_human_fraud"] = False

        # Resume graph
        st.session_state.result = claim_graph.invoke(st.session_state.state)

# -------------------------
# Final result
# -------------------------
if st.session_state.result and "final" in st.session_state.result:

    st.subheader("Final Decision")

    final = st.session_state.result["final"]

    st.json(final)
