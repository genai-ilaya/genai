import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_transcript(transcript_path, chunk_dir):
    print("**********************")
    print("Chunking transcript...")
    print("**********************")
    with open(transcript_path, "r", encoding="utf-8") as f:
        text = f.read()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    os.makedirs(chunk_dir, exist_ok=True)
    for i, chunk in enumerate(chunks):
        with open(os.path.join(chunk_dir, f"chunk_{i+1}.txt"), "w", encoding="utf-8") as f:
            f.write(chunk)
    print("**********************")
    print("Chunks saved to", chunk_dir)
    print("**********************")
    return chunks
