import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak("Current time is :")

    speak(Time)

def date():
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    speak("Current date is :")

    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    speak("welcome back own light!")
    
    hour=(datetime.datetime.now().hour)
    if hour >=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
    
        speak("Good After Noon!")
    elif hour>=18 and hour<24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak(" you are my  Akka.")
    
    speak(" and i am your j.")
    speak(" how may i help you ? akka")

def exgf():
    speak(" baby is ur ex gf!")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=1,phrase_time_limit=10)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception  as e:
        print(e)
        speak("Say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('psgareja123@gmail.com','ryvv637s')
    server.sendmail('psgareja123@gmail.com',to,content)
    server.close()
def mygf():
    speak("first wash your face then ask me!")
def screenshot():
    img=pyautogui.screenshot()
    img.save('ss.png')
def cpu():
    usage=str(psutil.cpu_percent())
    spea("CPU is at"+usage)
    battery=(psutil.senser_battery())
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching on wikipedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath='/Users/pradipgareja/Desktop/Google Chrome.app %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'my x' in query:
            exgf()
        elif 'my gf' in query:
            mygf()
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to='psgareja@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unabale to send Email!")
                
        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'play songs' in query:
            songs_dir=''
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'remember that' in query:

            speak("what should i remember?")
            data=takeCommand()
            speak("you said me to remember that :"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you said me to remember that:"+remember.read())


        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            quit()