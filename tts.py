import pyttsx3
import engineio
import time

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
print(voices)
engineio.setProperty('rate', 100);
engineio.setProperty('voice',voices[1].id)


file = open("HandsOn_ModuleB.txt","rt")
for line in file:
    for word in line.split():
        engineio.say(word)

engineio.runAndWait()
