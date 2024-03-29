import speech_recognition as sr
import os
import sys
import re
import datetime
import webbrowser

def mainfunction():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        voice = r.recognize_google(audio).lower()
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        voice = mainfunction()
    return voice

def Response(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def assistant(voice):
    if 'open' in voice:
        match = re.search('open (.+)', voice)
        if match:
            domain = match.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            Response('The website has been opened Ashwin.')
        else:
            pass
  
    elif 'tell me about' in voice:
        match = re.search('tell me about (.*)', voice)
        if match:
            topic = match.group(1)
            search = wikipedia.page(topic)
            print(search.content[:500].encode('utf-8'))
            # Response(search.content[:500].encode('utf-8'))

    elif 'time' in voice:
        now = datetime.datetime.now()
        Response('Current time is %d hours %d minutes' % (now.hour, now.minute))

    elif 'joke' in voice:
        Response("A man got hit in the head with a can of Coke, but he was alright because it was a soft drink.")

    elif 'stop listening' in voice:
        Response("Bye Ashwin!")
        sys.exit(0)
    

while True:
    assistant(mainfunction())
