# 🎯 End-to-End RAG Pipeline for Video Content

This project demonstrates an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline using video input.
It extracts audio, transcribes it using Whisper, splits the text into chunks, generates embeddings, stores them in FAISS, and finally answers questions using LLaMA2 (or DeepSeek) via Ollama.

---

## 📦 Features

- 🔊 Extract audio from video (MP4)
- ✍️ Transcribe audio using OpenAI Whisper
- ✂️ Chunk transcript text
- 🧠 Generate embeddings using HuggingFace models
- 🗃️ Store & retrieve vectors using FAISS
- 💬 Ask questions using LLaMA2 or DeepSeek-R1 with Ollama

## 🧠 Models Used

- **Whisper** : Audio-to-text transcription
- **MiniLM**  : Lightweight text embeddings
- **FAISS**   : Vector database
- **LLaMA2**  : Large Language Model (via Ollama)

---

## ✅ Prerequisites

- Python 3.10+
- Git
- Virtual environment (recommended)
- [Ollama](https://ollama.com/) installed and running --> 
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to system PATH --> https://youtu.be/K7znsMo_48I?si=4UMcKVZdIzqT_xrE
---


## 🔧 Installation Steps

  1. Clone repo | `git clone  && cd your-repo-name` |
  2. Create venv
     python -m venv .venv
     source .venv/bin/activate
  3. Install dependencies
     pip install -r requirements.txt
  4. Install FFmpeg 
     Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract & add `bin` to system PATH | --> https://youtu.be/K7znsMo_48I?si=4UMcKVZdIzqT_xrE
  5. Verify FFmpeg --> ffmpeg -version
  6. Install Ollama --> https://youtu.be/UtSSMs6ObqY?si=_JtAtxK6rWUX6u5J


---

## 🚀 Run the Pipeline

1. Prepare a video file **(make sure your video has audio)**
Place your **.mp4** file in the root directory or adjust the path in main.py.

2. Run the pipeline
python main.py

## ❓ Sample Question
Once the FAISS index is created, you'll be prompted to ask something like:

Q What is shown in the video ?
🍳 Cooking your answer...

You'll receive an answer generated using retrieved content and the LLM.

---

## 📁 Directory Structure

```bash
.
├── main.py
├── extractor.py          # Extracts audio & transcript
├── chunker.py            # Splits transcript into chunks
├── embedder.py           # Embeds chunks using HuggingFace
├── qa.py                 # RetrievalQA using LLaMA2 via Ollama
├── requirements.txt
├── README.md

