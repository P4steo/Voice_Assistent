import speech_recognition as sr
import pyttsx3
import pytdm
import wikipedia
import pywhatkit


listener = sr.Recognizer()
player = pyttsx3.init()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def listen():
    with sr.Microphone() as input_device:
        print("Jestem gotowy, słucham...")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content, language='pl-PL')
        text_command = text_command.lower()
        print(text_command)

    return text_command


def talk(text): 
    player.say(text)
    player.runAndWait()

def run_voicebot(): 
    command = listen()
    if "co to" in command:
        command = command.replace("co to", "")
        wikipedia.set_lang("pl")
        info = wikipedia.summary(command, 1)
        talk(info)
    elif "kto to" in command:
        command = command.replace("kto to", "")
        wikipedia.set_lang('pl')
        info = wikipedia.summary(command, 1)
        talk(info)
    elif "graj" in command:
        talk("Gram " + command )
        command = command.replace("play", "")
        pywhatkit.playonyt(command)
    elif "cześć" in command:
        talk("Joł jestem Rio")
    elif ("jestem" in command):
        command = command.replace("jestem", "")
        talk("Cześć" + command)
    else:
        talk("Sorry bro, nie wiem jak to zrobić")

        


run_voicebot()


