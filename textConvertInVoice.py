
import pyttsx3

def speak(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()

text = input("Enter Text _")
speak(text)
