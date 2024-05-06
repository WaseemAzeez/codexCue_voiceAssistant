import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what's the time" in command:
        speak("The current time is ...")  # You can implement time retrieval logic here
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

def listen_for_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("User command:", command)
        process_command(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    speak("Hello! I'm your personal assistant. How can I assist you?")
    while True:
        listen_for_commands()
