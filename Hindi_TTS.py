import asyncio
import edge_tts

# Define your text and missing configuration variables
SAMPLE_TEXT = """ भगवद्गीता - अध्याय 1... """  # your full text here
SELECTED_VOICE = "hi-IN-MadhuramNeural"  # Example Hindi voice
OUTPUT_FILE = "output.mp3"

async def generate_speech():
    print(f"Starting Hindi narration using voice: {SELECTED_VOICE}...")
    communicate = edge_tts.Communicate(SAMPLE_TEXT, SELECTED_VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Success! Audio saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(generate_speech())
