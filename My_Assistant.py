# JARVIS Created by Ashwini Kumar Sethi


# *******MODULES*************
# *** NECESSARY apps required *** #

# download Powertoys by microsoft for use https://apps.microsoft.com/store/detail/microsoft-powertoys/XP89DCGQ3K6VLD <-- download link
# pc manger by microsoft: https://apps.microsoft.com/store/detail/microsoft-powertoys/XP89DCGQ3K6VLD <-- download link

import shutil
import speech_recognition as sr
import sys
import winshell
from time import sleep
from pynput.keyboard import Controller, Key as k
from pynput.mouse import Controller as Clm
from plyer import notification
import pyttsx3
import datetime
import os
import subprocess
import webbrowser


# ********************  Controllers for keyboard and mouse  ********************

kb = Controller()
m = Clm()

# *******************  Voice assistant voice  **********************************

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# *****************************************************


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon Sir !")
        speak("Good Afternoon Sir !")

    else:
        print("Good Evening Sir !")
        speak("Good Evening Sir !")

    assname = "Jarvis 1 point o"
    speak("jarvis at your service")
    print("jarvis at your service\n")
    speak("I am your Assistant")
    speak(assname)


def username():
    # speak("What should i call you sir")
    # uname = takeCommand()
    speak("Welcome Mister Ashwini")
    # speak(uname)
    print("Welcome Mister Ashwini")
    print("How can i Help you, Sir\n")
    columns = shutil.get_terminal_size().columns

    # print("#####################".center(columns))
    # print("Welcome Mr.Ashwini", uname.center(columns))
    # print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        qs = r.recognize_google(audio, language="en-US")
        print(f"User said:(●) {qs}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return qs


if __name__ == "__main__":
    clear = lambda: os.system("cls")

clear()
wishMe()
username()

# find all the commands here
"""
    open youtube web/ open youtube
    open whatsapp
    open web images
    open chrome
    kill
    mini / minimise all / maximize
    open spotify
    open figma
    open gmail
    send notification
    volume up
    volume down
    mute
    ** shutdown system **    <--- use this voice command wisely
    ** empty recycle bin **  <--- use this voice command wisely
    don't listen/ stop listening
    ** sleep/hibernation **  <--- use this voice command wisely
    ** restart system **     <--- use this voice command wisely
    open file manager
    how are you
    time
    open pc manager
    find the mouse <-- not working do not use
"""


# apps are been used to open through powertoys:https://apps.microsoft.com/store/detail/microsoft-powertoys/XP89DCGQ3K6VLD <-- download link

# *****************************************************

while True:

    qs = takeCommand().lower()

    if "open youtube" in qs:
        speak("Opening youtube")
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(1)
        kb.type("youtube")
        sleep(1)
        kb.press(k.enter)

    elif "open youtube web" in qs:
        speak("opening youtube in chrome")
        webbrowser.open_new("youtube.com")

    elif "open whatsapp" in qs:
        speak("Opening whatsapp")
        webbrowser.open_new("https://web.whatsapp.com/")

    elif "open web images" in qs:
        webbrowser.open_new("webbtelescope.org/resource-gallery/images")

    elif "open chrome" in qs:
        speak("Opening Chrome")
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(1)
        kb.type("chrome")
        sleep(1)
        kb.press(k.enter)

    elif "kill" in qs:
        speak("It was a sure working with you")
        sys.exit()

    elif "mini" in qs:
        with kb.pressed(k.cmd_l):
            kb.press(k.down)

    elif "maximize" in qs:
        with kb.pressed(k.cmd_l):
            kb.press(k.up)

    elif "open spotify" in qs:
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(0.5)
        kb.type("spotif")
        # kb.press(k.down)
        sleep(0.5)
        kb.press(k.enter)

    elif "power point presentation" in qs:
        speak("opening Power Point presentation")
        power = r"C:\\Users\\ashwi\\Desktop"
        os.startfile(power)

    elif "minimise all" in qs:
        speak("minimizing all window")
        with kb.pressed(k.cmd):
            kb.type("m")

    elif "open figma" in qs:
        speak("Opening Figma")
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(1)
        kb.type("figma")
        sleep(1)
        kb.press(k.enter)

    elif "send notification" in qs:
        pass

    elif "open gmail" in qs:
        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

    elif "volume up" in qs:
        kb.press(k.media_volume_up)

    elif "volume down" in qs:
        kb.press(k.media_volume_down)

    elif "mute" in qs:
        kb.press(k.media_volume_mute)

    elif "shutdown system" in qs:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call("shutdown / p /f")

    elif "empty recycle bin" in qs:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in qs or "stop listening" in qs:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(takeCommand())
        sleep(a)
        print(a)
        speak("I am on")

    elif "restart system" in qs:
        speak("restarting system")
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in qs or "sleep" in qs:
        speak("sleeping")
        subprocess.call("shutdown / h")

    elif "open file manager" in qs or "open this pc" in qs:
        speak("opening file manager")
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(0.5)
        kb.type("file Explorer")
        sleep(0.5)
        kb.press(k.enter)

    elif "how are you" in qs:
        speak("I'm fine, glad you asked me that")

    elif "time" in qs:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        speak(f"Sir, the time is {strTime}")

    # Another app : https://pcmanager.microsoft.com/ <-- visit link to download the app pc manger is not as same as file manager
    elif "open pc manager" in qs:
        speak("opening pc manager")
        with kb.pressed(k.alt):
            kb.press(k.space)
        sleep(0.5)
        kb.type("pc manger")
        sleep(0.5)
        kb.press(k.enter)

    # not working and this needs powertoys from microsoft to run: https://apps.microsoft.com/store/detail/microsoft-powertoys/XP89DCGQ3K6VLD
    elif "find the mouse" in qs:
        with kb.pressed(k.ctrl):
            kb.press(k.ctrl)
        speak("here is the mouse")
