from gtts import gTTS

#langue
langue = "en"
#message
text = "yo"

#dire le messaghe
speech = gTTS(text=text, lang=langue, slow=False, tld="com.audio")

#sauvegarder message
speech.save("wow1.mp3")