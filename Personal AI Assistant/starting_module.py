from input_module import ask_something, listen
from process_module import process
from output_module import output, speak
import os

def clear_screen():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS and Linux
        os.system('clear')

def voice_mode():
    print("Voice Assistant Activated. Say something to start...")
    while True:
        try:
            command = listen()  # Get user input via speech
            if command.lower() == "exit voice mode":
                print("Exiting voice mode...")
                return  # Exit voice mode and return to the main menu
            response = process(command)  # Process the command
            speak(response)  # Output the response as speech
        except Exception as e:
            print(f"An error occurred in voice mode: {e}")

def text_mode():
    while True:
        try:
            user_input = ask_something()
            if user_input.lower() == "exit text mode":
                print("Exiting text mode...")
                return  # Exit text mode and return to the main menu
            response = process(user_input)
            output(response)
        except Exception as e:
            print(f"An error occurred in text mode: {e}")

def main_loop():
    clear_screen()
    while True:
        mode = input("Enter 'voice' to use voice mode, 'text' for text mode, or 'exit' to quit: ").lower()
        if mode == 'voice':
            speak("Voice Mode Activated")
            voice_mode()
        elif mode == 'text':
            speak("Text Mode Activated")
            text_mode()
        elif mode == 'exit':
            print("Exiting")
            print("Goodbye!")
            speak("GoodByeee!, See You Later")
            break
        else:
            print("Invalid mode selected. Please choose 'voice' or 'text'.")

if __name__ == "__main__":
    main_loop()


