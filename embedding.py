import os
import json
from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

def embed_chunks(chunk_dir, index_path, embedding_json_path):
    print("**********************")
    print("embedding chunks......")
    print("**********************")

    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    docs = []
    for file in sorted(os.listdir(chunk_dir)):
        with open(os.path.join(chunk_dir, file), "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(Document(page_content=content))

    # Extract texts and generate embeddings
    texts = [doc.page_content for doc in docs]
    vectors = embed_model.embed_documents(texts)

    # Prepare data for JSON
    embedded_data = []
    for text, vector in zip(texts, vectors):
        embedded_data.append({
            "chunk": text,
            "embedding": vector
        })

    # Save to JSON
    os.makedirs(os.path.dirname(embedding_json_path), exist_ok=True)
    with open(embedding_json_path, "w", encoding="utf-8") as f:
        json.dump(embedded_data, f, indent=2)

    print(f"✅ Embedded data saved to JSON: {embedding_json_path}")

    # Save FAISS index too
    db = FAISS.from_documents(docs, embed_model)
    os.makedirs(index_path, exist_ok=True)
    db.save_local(index_path)
    print(f"✅ FAISS index saved to: {index_path}")
