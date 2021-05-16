import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# fuction makes voice audibles


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greetings function


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am edith. Please tell me how may I help you")

# takes comand from microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
          print("Recognizing...")    
          query = r.recognize_google(audio, language='en-in') 
          print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower() 

        # logic for commands
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            # print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\mis\\Music\\Favs '
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, Favs[0]))
        elif ' send email ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gopashah1403@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('180320132051.ict.dhairvi@gmail.com', 'Dhairvi@2911')
    server.sendmail('gopashah1403@gmail.com', to, content)
    server.close()
