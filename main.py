from logger import logger
from graph.claim_graph import claim_graph

logger.info("Starting Agentic Claims System")

state = {
    "user_input": "Initiate claim for Mark Fraud. Car accident on 3 Jan.Vehicle completely damaged."
}

logger.info("Invoking claim graph with user input")
result = claim_graph.invoke(state)

logger.info("Claim graph execution finished")
logger.info(f"Final result: {result.get('final')}")
