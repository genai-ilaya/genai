from extractor import extract_transcript
from chunking import chunk_transcript
from embedding import embed_chunks
from qa import answer_question
import os
import time
import sys

video_path = r"D:\Download\UrimeterMedical.mp4"
audio_path = r"D:\video_rag\data\UrimeterMedical_audio.mp3"
transcript_path = r"D:\video_rag\data\transcripts\UrimeterMedical.txt"
chunk_dir = r"D:\video_rag\data\chunks"
embedding_json_path = r"D:\video_rag\data\embeddings\embeddings.json"
index_path = r"D:\video_rag\data\index"

# Run preprocessing only if index doesn't exist
if not os.path.exists(index_path):
    print("Index not found. Running full pipeline...")
    text = extract_transcript(video_path, audio_path, transcript_path)
    chunks = chunk_transcript(transcript_path, chunk_dir)
    embed_chunks(chunk_dir, index_path, embedding_json_path)
else:
    print("Index found. Skipping extraction, chunking, and embedding.")


# Interactive QA loop
print("\nAsk your questions about the video! Type 'exit' to quit.\n")
while True:
    query = input("Q: ")
    if query.lower() in ['exit', 'quit']:
        break

    print("🍳 Cooking your answer", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    answer = answer_question(index_path, query)
    print("A:", answer)


print("Goodbye!")