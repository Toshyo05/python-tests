import wikipedia
import pyttsx3


voi = pyttsx3.init()
voice = voi.getProperty("voice")
voi.setProperty("voice", voice[0])

In = input("recherche :")
result = wikipedia.summary(In, sentences = 3)
print(result)

voi.say(result)
voi.runAndWait()
voi.stop()
