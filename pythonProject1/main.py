import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp

from decouple import config
from datetime import datetime
from random import choice
from conv import random_text

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 225)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER', default='Prathamesh')
HOSTNAME = config('BOT', default='JARVIS')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good morning {USER}")
    elif 12 <= hour <= 16:
        speak(f"Good afternoon {USER}")
    elif 16 <= hour < 19:
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may I assist you? {USER}")


listening = False  # Initially, not listening


def start_listening():
    global listening
    listening = True
    print("Started listening")


def pause_listening():
    global listening
    listening = False
    print("Stopped listening")


# Setting up hotkeys
keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if 'stop' not in query and 'exit' not in query:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()

    except Exception as e:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        query = 'None'
    return query


if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()

            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path = "C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)

            elif "open discord" in query:
                speak("Opening Discord for you sir")
                discord_path = "C:\\Users\\Prathmesh\\AppData\\Local\\Discord\\Update.exe"
                os.startfile(discord_path)

            elif "open valorant" in query:
                speak("Opening Valorant for you sir")
                valo_path = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
                sp.Popen([valo_path, "--launch-product=valorant", "--launch-patchline=live"])

            elif "open jetbrains" in query:
                speak("Opening JetBrains Toolbox for you sir")
                jetbrains_path = r"D:\python\jetbrains-toolbox-2.4.2.32922.exe"
                os.startfile(jetbrains_path)

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

