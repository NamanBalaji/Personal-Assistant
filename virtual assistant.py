#Description: This is a virtual assistant that gets the current date responds with a greeting and returns information about a person.
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import calendar
import random
import wikipedia

def RecordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)
        
    data = ''
    try:
       data  = r.recognize_google(audio)
       print('You said '+data)
    except sr.UnknownValueError:
        print('Could not understand the audio')
    except sr.ReuestError as e:
        print(e)
    
    return data
        
def AssistantResponse(text):
    print(text)
    myObj = gTTS(text = text, lang = 'en', slow = False)
    myObj.save('assistant_response.mp3')
    os.system('start assistant_response.mp3')

def WakeWord(text):
    WAKE_WORDS = ['hey assistant', 'hello assistant']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

def GetDate():
    now = datetime.datetime.now()
    date= datetime.datetime.today()
    weekday = calendar.day_name[date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    
    return 'Today is ' + weekday + ' ' + month_names[monthNum-1] + ' ' + 'the ' + ordinalNumbers[dayNum-1]+'.'

def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'hello', 'whats up']
    GREETING_RESPONSES = ['hello','hi there','whats good', 'hey']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)+'.'
    return ''

def GetPerson(text):
    word_list = text.split()
    for i in range(0, len(word_list)):
        if i+3<=len(word_list)  and word_list[i].lower() == 'who' and word_list[i+1].lower()=='is':
            return word_list[i+2]+' '+word_list[i+3]
        

while True:
    text = RecordAudio() 
    response = ''
    
    if(WakeWord(text)==True):
        response = response+greeting(text)
    if('date' in text):
        get_date=GetDate()
        response = response+' '+get_date
    if('who is' in text):
        person = GetPerson(text)
        wiki = wikipedia.summary(person,sentences=2)
        response = response+' '+wiki
    AssistantResponse(response)
        
