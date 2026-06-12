import asyncio
import edge_tts

async def generate_long_speech(text: str, voice: str, output_path: str):
    """Generates long-form speech using Microsoft Edge's advanced AI voices."""
    print(f"🤖 Initializing male voice [{voice}] for long audio generation...")
    
    # Configure the TTS engine
    communicate = edge_tts.Communicate(text, voice)
    
    print("⏳ Processing and saving your audio file (this may take a minute for long text)...")
    # Save the file directly to the cloud container
    await communicate.save(output_path)
    
    print(f"✨ Success! Audio file saved to: {output_path}")

if __name__ == "__main__":
    # --- CONFIGURATION ZONE ---
    
    # 1. SELECT YOUR MALE VOICE HERE:
    # For English (US Male), use: "en-US-BrianNeural" or "en-US-ChristopherNeural"
    # For Hindi (India Male), use: "hi-IN-MadhuramNeural"
    SELECTED_VOICE = "en-US-BrianNeural" 
    
    # 2. PASTE YOUR LONG TEXT HERE (Can be 6 to 10 minutes long):
    SAMPLE_TEXT = """
    Welcome to this long-form audio presentation. 
    This system is now powered by advanced neural networks, allowing it to read 
    pages of text without timing out or breaking down. You can paste paragraphs 
    of text here to generate your complete 6 to 10 minute audio file.
    """
    
    # 3. NAME YOUR OUTPUT FILE:
    OUTPUT_FILE = "long_english_male.mp3"
    
    # Run the async system required by edge-tts
    asyncio.run(generate_long_speech(SAMPLE_TEXT, SELECTED_VOICE, OUTPUT_FILE))

