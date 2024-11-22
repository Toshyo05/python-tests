import pyttsx3

uiui = ""

voi = pyttsx3.init()
voice = voi.getProperty("voice")

print(uiui)

voi.setProperty("voice", voice[0])
voi.say(uiui)
voi.runAndWait()
voi.stop()