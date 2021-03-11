import pyttsx3
import speech_recognition as sr
regonizer=sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Say Something')
        voice1=regonizer.listen(source)
        text=regonizer.recognize_google(voice1,language='en')
        print(text)
except:
    pass
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)

engine.runAndWait()


#for voice in voices: # to get all voices
    #engine.setProperty('voice', voice.id)
    #engine.say('We are friends and I really miss u')