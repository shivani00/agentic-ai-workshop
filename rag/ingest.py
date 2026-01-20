from langchain_community.document_loaders import TextLoader
from vectorstore import vectorstore

docs = []
for file in [
    "rag/docs/auto_policy.txt",
    "rag/docs/exclusions.txt",
    "rag/docs/fraud_rules.txt"
]:
    docs.extend(TextLoader(file).load())

vectorstore.add_documents(docs)
vectorstore.persist()
