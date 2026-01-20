from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="qwen2.5")

vectorstore = Chroma(
    persist_directory="./chroma",
    embedding_function=embeddings
)
