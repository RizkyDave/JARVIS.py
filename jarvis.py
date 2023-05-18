import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import pyjokes

def get_response(input):
    if input == "let's fly RPS game":
        return "lets go choose one rock paper or scissors"
    
    elif input == "hello Jarvis" or input == "hey Jarvis":
        return "Hello Sir what can i help"
    
    elif input == "what the time is it" or input == "what time is it":
        d = datetime.datetime.now()
        hour = d.hour
        minute = d.minute

        return "The time is " + str(hour) + ":" + str(minute) + " sir !"

    
    elif input == "give me a joke" or input == "gime me joke":
        return pyjokes.get_joke()

    elif input == "what is":
        return "Please specify who you're looking for."
    
    elif input == "what is ":
        person = input.replace('what is ', '')
        info = wikipedia.summary(person, 1)
        return str(info)


    elif input == "goodbye":
        return "Talk to you later sir!"
    else:
        return "Try asking something else sir!"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        result = recognizer.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Recognition request failed: ", str(e))
    return None

while True:
    input_text = recognize_speech()
    if input_text:
        response = get_response(input_text)
        print("Jarvis:", response)
        speak(response)
