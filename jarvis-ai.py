import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime

engi = pyttsx3.init("sapi5")
voice = engi.getProperty('voices')
engi.setProperty("voice", voice[0].id)


def speak(audio):
    engi.say(audio)
    engi.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning boss")
    elif hour > 12 and hour < 18:
        speak("good afternoon boss")
    else:
        speak("good evening boss")
    speak("i am jarvis sir , tell how i want to help you")


def takecom():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("wait panuga")
        r.adjust_for_ambient_noise(source, duration=2)
        print("start speaking")
        audio = r.listen(source)
    try:
        print("Regonosing...")
        q = r.recognize_google(audio, language="en-in")
        print(f"user said :{q}")
    except:
        speak("say that again sir......")
        print("say that again sir......")
        return "None"
    takecom()
    return q

wishme()
while True:
    q = takecom().lower()
    if "who are you" in q:
        speak("my name is jarvis boss, i am your assistan to help you")
    elif "how are you" in q:
        speak("i am fine boss what about you")
    elif "what can you do" in q:
        speak("i can browse , tell joke , play games and more interesing things")
    elif "sleep" in q:
        break
    elif "hi" in q:
        speak("hello sir what you want...")

    elif "open google" in q:
        webbrowser.open("google.com")
        speak("do you want me to search")
        a=takecom().lower()
        if "search google" in q:
              while True:
                  speak("Listening...")
                  s= takecom().lower()
                  if "close" in s:
                      speak("exiting google...")
                      break
                  elif "none" not in s:
                      webbrowser.open_new_tab(f"http://www.google.com/search?q={s}")
    elif "time now" in q:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time now is (time_now)")
