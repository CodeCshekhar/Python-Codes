# The lib is for text to speech
import pyttsx3

# This engine is to init the pyttsx3
engine = pyttsx3.init()

# We ask to say
engine.say("This is my program where i will ask the machine to speak something")

# We can now run and wait for the speech
engine.runAndWait()
