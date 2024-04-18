from assistant_information import name
import pyttsx3

def speak(text):
    """Function to speak the text using TTS."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def output(o):
    """Prints the output to the console and speaks it out loud."""
    print(o)  # Print output to console for visibility or debugging
    speak(o)  # Speak the output aloud
