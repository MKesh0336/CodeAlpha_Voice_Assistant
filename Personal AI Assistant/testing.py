# from gtts import gTTS
# from playsound import playsound
# tts = gTTS('Hi My name is Vision. I have created by Muhammad Kashan Irshad. I am the Vision of his great creativity.')
# tts.save('speech.mp3')
# playsound('speech.mp3')
# import speech_recognition as sr
# recognizer = sr.Recognizer()
# print(hasattr(recognizer, 'recognize_google'))  # This should print True if the method exists
# import speech_recognition as sr

# def main():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         print(audio)
#         try:
#             print("Recognizing...")
#             text = recognizer.recognize_google(audio)
#             print("You said:", text)
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand the audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}.")

# if __name__ == "__main__":
#     main()
import speech_recognition as sr
print(dir(sr.Recognizer))  # This will list all the attributes and methods available in the Recognizer class.

