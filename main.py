import os
import sys
import torch
from TTS.api import TTS

def generate_multilingual_speech(text: str, lang: str, speaker_audio: str, output_path: str):
    print("🤖 Loading multilingual TTS model... (This may take a minute)")
    # Force CPU usage since free GitHub Codespaces do not have a GPU
    device = "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    print(f"🎙️ Generating speech in [{lang}]...")
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_audio,
        language=lang,
        file_path=output_path
    )
    print(f"✨ Audio successfully saved to: {output_path}")

if __name__ == "__main__":
    # EDIT THESE THREE LINES TO CHANGE TEXT OR LANGUAGE
    SAMPLE_TEXT = "Hello! This is a test running completely on GitHub cloud."
    LANGUAGE = "en"  # Options include: en, es, fr, de, it, ja, zh, hi
    REFERENCE_AUDIO = "sample_voice.wav"
    OUTPUT_FILE = "output.wav"

    if not os.path.exists(REFERENCE_AUDIO):
        print(f"❌ Error: Please upload a 5-second '{REFERENCE_AUDIO}' file to your repository.")
        sys.exit(1)

    generate_multilingual_speech(SAMPLE_TEXT, LANGUAGE, REFERENCE_AUDIO, OUTPUT_FILE)
