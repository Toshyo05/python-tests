import wikipedia
from gtts import gTTS


def recherche(entrée, sentences):
    result = wikipedia.summary(entrée, sentences = sentences)
    return result


def bot_voi(langue, texte):
    speech = gTTS(text=texte, lang=langue, slow=False, tld="com.audio")
    speech.save("bot_default_a_renomer.mp3")