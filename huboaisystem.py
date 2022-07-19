import pyttsx3
from email.mime import audio
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
name="HUBO"
def speek(audio):
    engine.say(audio)
    engine.runAndWait()
def wiseMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speek("Good Morning!")
    elif hour>=12 and hour<18:
        speek("Good Afternoon!")
    else:
        speek("Good Evening")
    speek(f"I am {name}, Sir please tell me,How may i help you")
def takeCommand():
    ''' it takes microphone input from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')#use for google recognize
        print(f"User said:{query}\n")
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    # speek("Sourik is a good boy")
    wiseMe()
    # while True:
    while True:
        query=takeCommand().lower()
        #set logic for executing task based on query
        #same proces added any webbrowser site and its work
        if "wikipedia" in query:
            speek("searching wikipedia...")
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=2)
                speek("According to wikipedia")
                print(results)
                speek(results)
            except Exception as e:
                speek("sorry,I can not find. please try agin.....")


        elif "what's your name" in query:
            speek(f"my name is {name}")
        elif "about yourself" in query:
            speek(f"My name is a {name}, I am a sofware, Build in Python, create me my best friend sourik.My brain memory is a 4gb ram and 64gb rom")
       
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open github" in query:
            webbrowser.open("github.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "play music song" in query:
            music_dir="D:\\songs\\favorite"
            songs=os.listdir(music_dir)
            # print(songs)   FOR DEBUGGING
            random_song=random.randint(0,len(songs))
            # print(random_song)  FOR DEBUGGING
            speek('now your song is playing!!!Enjoy your song')
            os.startfile(os.path.join(music_dir,songs[random_song]))
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speek(f"sir, now the time is{strtime}")
        elif "the date today" in query:
            strdate=datetime.date.today()
            print(strdate)
            speek(strdate)
        elif "the date tomorrow" in query:
            today=datetime.date.today()
            tomorrowDate=today+datetime.timedelta(days=1)
            print(tomorrowDate)
            speek(tomorrowDate)
        elif "the date yesterday" in query:
             today=datetime.date.today()
             yesterdayDate=today-datetime.timedelta(days=1)
             print(yesterdayDate)
             speek(yesterdayDate)
        elif "open code" in query:
            codepath="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open Devc" in query:
            codepath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codepath)
        elif "open chrome" in query:
            codepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)
        elif "open my memory" in query:
            codepath="D:\\MEMORY"
            os.startfile(codepath)
        elif "exit" in query:
            speek("thank you sir,have a nice day")
            exit()
            
            
