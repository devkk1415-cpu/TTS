from gtts import gTTS

# 1. Type the text you want the human voice to say
my_text = "Hello friend! Do I sound much better now? This voice is generated using Google's cloud system, making it sound like a real person instead of a clunky robot."

# 2. Tell the system to create a natural English voice
speech = gTTS(text=my_text, lang='en', slow=False)

# 3. Save the new realistic voice file
speech.save("human_voice.mp3")

print("Success! I created a realistic voice file named human_voice.mp3.")
