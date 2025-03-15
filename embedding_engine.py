import chromadb
from langchain_community.embeddings import OpenAIEmbeddings
import os

class EmbeddingEngine:
    def __init__(self):
        self.embedding_model = OpenAIEmbeddings(openai_api_key="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")
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="news_articles")

    def create_embedding(self, text):
        return self.embedding_model.embed_documents([text])[0]

    def store_article(self, article):
        content = article["title"] + " " + article["description"]
        embedding = self.create_embedding(content)
        self.collection.add(
            documents=[content],
            metadatas=[{"source": article["url"]}],
            ids=[article["url"]]
        )

    def search_similar(self, query, top_k=3):
        embedding = self.create_embedding(query)
        return self.collection.query(query_embeddings=[embedding], n_results=top_k)
