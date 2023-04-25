import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by Rahul")

while True:
    x = input("Enter what you want to speak me: ")
    speak.Speak(x)
    if x == "exit":
        speak.Speak("Good bye!")
        break