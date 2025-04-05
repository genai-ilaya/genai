from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
# from langchain.llms import Ollama  # or Ollama, etc.
from langchain_ollama import OllamaLLM
# from langchain_community.llms import HuggingFaceHub

def answer_question(index_path, query):
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(index_path, embed_model, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()
    llm = OllamaLLM(model="llama2", temperature=0.5)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    # return qa.invoke({"query": query})
    return qa.invoke({"query": query})["result"]
