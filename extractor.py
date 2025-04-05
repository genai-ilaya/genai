import subprocess, whisper, os

def extract_transcript(video_path, audio_path, transcript_path):

    print("*******************")
    print("Extracting audio...")
    print("*******************")

    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    command = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "mp3", audio_path]
    subprocess.run(command, check=True)

    print("**********************")
    print("Audio extracted to", audio_path)
    print("**********************")

    
    print("**********************")
    print("Transcribing audio...")
    print("**********************")

    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print("**********************")
    print("Transcript saved to", transcript_path)
    print("**********************")
    return result["text"]
