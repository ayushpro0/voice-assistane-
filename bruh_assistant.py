import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning bruh")
    elif hour>=0 and hour<5:
        speak("its very late you should sleep")
    elif hour>=12 and hour<18:
        speak("Good Afternoon bruh")
    else:
        speak("Good Afternoon bruh")

    speak("what do you need")


def takeCommand():
    #it takes microphone input from the computer and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"me: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('kumarayushgg@gmail.com', 'account@ayush')
    server.sendmail('kumarayushgg@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()

    
    if(1):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching Wikipedia....")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("ofcourse bruh")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("ofcourse bruh")
            webbrowser.open("https://google.com")

        elif 'open spotify' in query:
            speak("ofcourse bruh")
            webbrowser.open("https://open.spotify.com/?_ga=2.57289834.1705352642.1599326620-924647805.1594920364")

        elif 'open download' in query:
            down_dir = 'E:\Downloads\walls'
            files = os.listdir(down_dir)
            print(files)
            os.startfile(os.path.join(down_dir, files[9]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"Bruh, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\personal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)\

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "riturajgiri22@gmail.com"
                sendEmail(to, content)
                print("Email sent!")
                speak("email has been sent")
            except Exception as e:
                print(e)
                print("cant sent it now")
                speak("cant sent it now")




            
