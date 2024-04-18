import speech_recognition as sr
def ask_something():
    i = input("Me: ").lower()  # Convert input to lowercase immediately after receiving it
    return i


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return "I didn't understand that."
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "Failed to connect to the service."

