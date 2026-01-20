from langchain_community.llms import Ollama

llm = Ollama(
    model="qwen3:0.6b",
    temperature=0
)
