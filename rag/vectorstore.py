from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory="./chroma",
    embedding_function=embeddings
)
