import pyttsx3

# This sets up the talking engine
engine = pyttsx3.init()

# We save the voice to an audio file so we can hear it in the browser!
engine.save_to_file("Hello friend! Your GitHub setup is completely finished and working!", "voice_output.mp3")
engine.runAndWait()

print("Success! I created a file named voice_output.mp3 inside your folder.")
