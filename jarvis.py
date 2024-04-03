import pyttsx3 #Text to speech conversation Library
import datetime  
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back sir!")
    speak("the current time is")
    time()
    speak("the current date is ")
    date()
    speak("Jarvis at you service Please tell me how can i help you?")
wishme()