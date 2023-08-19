import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Hello bro, my name is Dino")
    # time()
    # date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning bro!")
    elif hour >=12 and hour < 18:
        speak("Good afternon bro")
    elif hour >=18 and hour <24:
        speak("Good evening bro")
    else:
        speak("Good night bro")
        
    speak("tell me how can i help you ?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
        
    return query 
def sendEmail(to, content):
    server = smtplib.SMTP("smtb.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("abcd@gmail.com", "123")
    server.sendmail("abc@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\99450\\Desktop\\JARVIS\\img\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
        elif 'wikipedia' in query:
            speak("Serarching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 3)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                #sendEmail(to, content)
                speak(content)
                
            except Exception as e:
                print(e)
                speak("Uabel to send the email")
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("restart /r /t 1")
        elif 'play song' in query:
            #buraya spotify dwz'lt
            print("dfd")
            
        elif 'remember that' in query:
            speak("What should i remeber ?")
            data = takeCommand()
            speak("you said me to remeber that"+data)
            remember =open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data//data.txt", "r")
            speak("You said me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        
        elif 'date' in query:
            date()
        elif 'offline' in query:
            quit()

