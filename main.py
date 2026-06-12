import os
from gtts import gTTS

def generate_speech(text: str, lang: str, output_path: str):
    print(f"🤖 Generating speech in language code: [{lang}]...")
    
    # This creates the text-to-speech using standard AI voices
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # Saves the file to your computer/cloud
    tts.save(output_path)
    print(f"✨ Audio successfully saved to: {output_path}")

if __name__ == "__main__":
    # EDIT THESE TWO LINES TO CHANGE THE TEXT AND LANGUAGE
    SAMPLE_TEXT = "Hello! This is a simple text to speech program running completely on GitHub."
    LANGUAGE = "en"  # Examples: 'en' (English), 'es' (Spanish), 'fr' (French), 'hi' (Hindi)
    
    OUTPUT_FILE = "output.mp3"

    generate_speech(SAMPLE_TEXT, LANGUAGE, OUTPUT_FILE)
