import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import wikipedia
import smtplib
import requests
import datetime
import random
#import subprocess
import sys
import pycurl
from pyowm import OWM
import urllib
from urllib.request import urlopen
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import wolframalpha
from PyDictionary import PyDictionary
from datetime import date
import calendar
from bs4 import BeautifulSoup as soup
import psutil
from nltk.corpus import wordnet
from textblob import TextBlob
import cv2
from time import sleep
import numpy as py
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

dictionary=PyDictionary()
    
def speak(audio):
    print('Ignis : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        return False

if is_internet():
    speak("Internet is active")
else:
    speak("Internet disconnected")
    sys.exit()

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak('Your last command couldn\'t be heard.')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'hi' in command or 'hello' in command or 'ignis' in command or 'hey' in command:
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
            speak("I am ignis. Please tell me how may I help you.")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
            speak("I am ignis. Please tell me how may I help you.")

        else:
            speak("Good Evening!")
            speak("I am ignis. Please tell me how may I help you.")

    elif 'meaning' in command:
        try:
            speak('Tell me the word')
            word=myCommand()
            print(PyDictionary.meaning(word))
            speak('Here is your answer')
        except exception as e:
            print(e)

    elif 'whatsapp' in command:
        driver = webdriver.Chrome('C:/Users/praveen kumar/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get('https://web.whatsapp.com/') 
        wait = WebDriverWait(driver, 600)
        target = 'Frn Kishore Clg'
        string = "Message sent using Python!!!"
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg))) 
        group_title.click() 
        inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        input_box = wait.until(EC.presence_of_element_located(( 
            By.XPATH, inp_xpath))) 
        for i in range(100): 
            input_box.send_keys(string + Keys.ENTER) 
            time.sleep(1) 
        
    elif 'synonym' in command:
        try:
            speak('Tell me the word')
            word=myCommand()
            syn = list()
            ant = list()
            for synset in wordnet.synsets(word):
                for lemma in synset.lemmas():
                    syn.append(lemma.name())    
                    if lemma.antonyms():    
                        ant.append(lemma.antonyms()[0].name())
            print('Synonyms: ' + str(syn))
        except exception as e:
            print(e)

    elif 'antonym' in command:
        try:
            speak('Tell me the word')
            word=myCommand()
            syn = list()
            ant = list()
            for synset in wordnet.synsets(word):
                for lemma in synset.lemmas():
                    syn.append(lemma.name())    
                    if lemma.antonyms():   
                        ant.append(lemma.antonyms()[0].name())
            print('Antonyms: ' + str(ant))
        except exception as e:
            print(e)

    elif 'translate' in command or 'translation' in command:
        speak('Tell me the word')
        word=myCommand()
        translator=TextBlob(word)
        print(translator.translate(from_lang='en', to='ta'))

    elif 'languages' in command:
        speak('I\'m currently programmed to speak english')

    elif 'news' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            # Print news title, url and publish date
            for news in news_list[:5]:
                print(news.title.text)
                print(news.link.text)
                print(news.pubDate.text)
                print('-'*60)
        except Exception as e:
                print(e)
    
    elif 'search' in command:
        new=2
        taburl="http://google.com/?#q="
        speak('What should i search ?')
        term=myCommand()
        webbrowser.open(taburl+term,new=new)

    elif 'google chrome' in command or 'in google chrome' in command:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    elif 'who are you' in command or 'who you are' in command:
        speak('Hi! I\'m ignis your virtual assistant')

    elif 'made you' in command or 'built you' in command or 'invented you' in command:
        speak('Kishore R, Praveen kumar K, Praveen P, Monesh S, mentored by Rengaraj alias muralidharan from saranathan college of engineering, Information Technology department.')

    elif 'wikipedia' in command or 'tell me about' in command:
        try:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            command = command.replace("tell me about", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            
        except exception as e:
            print(e)
            speak("Couldn't get you!!!");

    elif 'in which language are you written' in command or 'language used' in command:
        speak('I\m written in python')

    
    elif 'open drive' in command or 'open directory' in command:
        speak('Which drive?')
        drive = myCommand()
        if drive=='c drive' or drive=='c directory' or drive=='c colon':
            os.startfile('C:')
        elif drive=='d drive' or drive=='d directory' or drive=='d colon':
            os.startfile('D:')
        elif drive=='e drive' or drive=='e directory' or drive=='e colon':
            os.startfile('E:')
        elif drive=='f drive' or drive=='f directory' or drive=='f colon':
            os.startfile('F:')
        else:
            speak('Please tell the correct drive!!');
        
            
    elif 'play music' in command:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak('Okay, here is your music! Enjoy!')
            sys.exit()

    elif 'current weather' in command or 'current temperature' in command:
        try:
            reg_ex = re.search('current weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
        except exception as e:
            print('Sry, cannot find details about your city')
 

    elif 'battery percentage' in command or 'charge percentage' in command:
        speak(f"Remaining battery is {psutil.sensors_battery().percent}%")

        
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak('Done! task completed')
        else:
            pass

    elif "what's up" in command or 'how are you' in command:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

    elif 'microsoft word' in command:
        os.startfile()
            
            
    elif 'joke' in command:
       try:
            res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
       except exception as e:
            print(e)
            speak("Couldn't get you!!!")

    elif 'notepad' in command:
        speak('Tell the file name')
        filename=myCommand()
        if os.path.isfile('D:\\Ignis\\'+filename):
            speak('Say the content to write')
            ipt=myCommand()
            f=open(filename,"a")
            f.write(ipt)
            speak('Text written successfully')
            os.startfile('D:\\Ignis\\'+filename)
        else:
            f=open(filename,"w+")
            speak('Say the content to write')
            ipt=myCommand()
            f.write(ipt)
            speak('Text written successfully')
            os.startfile('D:\\Ignis\\'+filename)
        
            
    elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

    elif 'the day' in command or 'day' in command:
        now = datetime.datetime.now()
        speak(now.strftime("%A"))
        

    elif 'date' in command:
        today=date.today()
        d2 = today.strftime("%B %d, %Y")
        speak(d2)

    elif 'open command prompt' in command or 'open cmd' in command or 'command prompt' in command or 'cmd' in command:
        os.startfile('C:\\Users\\praveen kumar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt')

    elif 'nothing' in command or 'abort' in command or 'stop' in command or 'bye' in command:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()
    
    elif 'email' in command or 'mail' in command:
        try:
            speak('Recipient mail ID?')
            recipient = myCommand()
            if (recipient.find('@') < recipient.find('.') and '@' in recipient and len(recipient) > 5):
                speak('What should I say?')
                content = myCommand()

                #init gmail SMTP
                mail = smtplib.SMTP('smtp.gmail.com', 587)

                #identify to server
                mail.ehlo()

                #encrypt session
                mail.starttls()

                #login
                mail.login('pk9489114199@gmail.com', 'kannanpraveen')

                #send message
                mail.sendmail('pk9489114199@gmail.com', recipient.replace(" ",""), content)

                #end mail connection
                mail.close()

                speak('Email sent.')
            else:
                speak('Please check the mail ID')

        except exception as e:
            print(e)
            speak("Sorry, I am not able to send this email")

    else:
        speak('I don\'t know what you mean!')


speak('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
