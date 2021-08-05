import speech_recognition as sr
import webbrowser
import pyttsx3
import os


print(" \n\n")
print("			*Menu Driven Program*\n")
print("	-------------------------------------------------------")
print(" 			Notepad")
print(" 			Chrome Browser")
print(" 			Gmail")
print(" 			Youtube")
print(" 			Whatsapp")
print(" 			Media Player")
print(" 			Zoom")
print(" 			LikedIn")
print(" 			Microsoft Teams")
print(" 			Telegram")
print(" 			Quit or Exit")
print("	-------------------------------------------------------\n\n")

pyttsx3.speak("Welcome")
#ch = input()

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        pyttsx3.speak("Hello, I am here how can i helpl you.... \n")
        pyttsx3.speak('Start saying...')
        print("Start saying....")
        audio = r.listen(source)
        pyttsx3.speak('we got it, Please wait!!....')
        print("We got it, Please Wait!!...")    
        print(" ")


    ch = r.recognize_google(audio)
    print("You said : {}".format(ch))

    

    if  ("Notepad" in ch) or ("Editor" in ch):
        pyttsx3.speak('Opening notepad for you')
        os.system("Notepad")
    elif ("Gmail" in ch) or ("email" in ch):
        pyttsx3.speak('Opening Gmail for you')
        webbrowser.open("https://mail.google.com/")
    elif ("YouTube" in ch):
        pyttsx3.speak('Opening Youtube for you')
        webbrowser.open("https://www.youtube.com/")
    elif ("Chrome" in ch) or ("Browser" in ch):
        pyttsx3.speak('Opening Chrome Browser for you')
        webbrowser.open("Chrome")
    elif ("Microsoft" in ch) or ("teams" in ch):
        pyttsx3.speak('Opening Microsoft Teams for you')
        webbrowser.open("https://login.microsoftonline.com/")
    elif ("who are you" in ch) or ("who developed you" in ch) or ("what is your name" in ch):
        pyttsx3.speak("Hi my name is Ruchi Ranjan and i am here to help you in doing any task. You can ask anything from me.")
    elif ("LinkedIn" in ch):
        pyttsx3.speak('Opening LinkedIn for you')
        webbrowser.open("https://www.linkedin.com/")
    elif ("Media" in ch ) or ("player" in ch):
        pyttsx3.speak('Opening Media Player')
        os.system('wmplayer')
    elif ("telegram" in ch):
        pyttsx3.speak('Opening Telegram for you')
        webbrowser.open("https://web.telegram.org/z/")
    elif ("zoom" in ch):
        pyttsx3.speak('Opening Zoom')
        webbrowser.open('https://zoom.us/')
    elif ("WhatsApp" in ch ):
        pyttsx3.speak('Opening Whatsapp for you')
        webbrowser.open('https://web.whatsapp.com/')
    elif ("quit" in ch ) or ("exit" in ch):
        pyttsx3.speak('Closing the Program')
        os.system('exit')
        break
    else:
        print(" Error!! ")
        pyttsx3.speak('Sorry..Try again')

        