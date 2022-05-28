import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import time
import webbrowser
import winsound
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import pywhatkit as kt
from playsound import playsound
from googletrans import Translator
from gtts import gTTS
import os
from requests import get
# engine that is used in speak function for converting text to speech
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(text):
    engine.setProperty("rate",165)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        statement=r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")

    except Exception as e:
        speak("Can you please repeat")
        return "None"  
    return statement.lower()

def gretings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    speak("Hi am ARA, how can I help you")

def tellDay():
    
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1803010117@gmail.com', 'khushboosharma239')
    server.sendmail('1803010117@gmail.com', to, content)
    server.close()

def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
    notificator.show_toast(f"Reminder",remider,duration=20)

    #alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

def Commands():
    #statement=takeCommand()
    while True:
        statement =takeCommand()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement or "bye" in statement:
                speak('your personal assistant is shutting down, Goodbye')
                print('your personal assistant is shutting down, Goodbye')
                break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            speak("What should I search ??")
            target=takeCommand()
            time.sleep(1)
            kt.search(target)
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        elif 'open news' in statement or 'news' in statement:
            news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines' )
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif 'write an email' in statement:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("To whome should i send?")
                    to = takeCommand()    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry! your email was not sent")

        elif 'the time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f" the time is {strTime}")  

        elif "day it is" in statement:
                tellDay()
                continue
            
        elif "tell me the time" in statement:
                tellTime()
                continue  
        elif "set an alarm" in statement:
                speak("What is the alarm in relation to?: ")
                words=takeCommand()
                time.sleep(2)
                speak("For how many seconds: ")
                sec= takeCommand()
                time.sleep(1)
                timer(words,int(sec) )
        elif "search for me" in statement:
                speak("what do you want me to search")
                target=takeCommand()
                time.sleep(1)
                kt.search(target)
        elif "repeat after me" in statement:
                speak("what would you like me to repeat?")
                input1=takeCommand()
                time.sleep(3)
                speak("you said"+" "+input1)
                print()
        elif "what can you do" in statement:
                speak("I am glad you asked i can do many things ...  like I can tell you time, do search for you , open youTube ,set an alarm and many more")
                print("I am glad you asked i can do many things ...  like I can tell you time, do search for you , open youTube ,set an alarm and many more")
        elif "ip address"in statement :
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is{ip}")
        
if __name__=='__main__':
    gretings()
    Commands()
    
    