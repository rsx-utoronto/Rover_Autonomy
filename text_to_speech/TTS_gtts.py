from gtts import gTTS
from playsound import playsound
import os

# text to speech function
def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")


if __name__ == '__main__':
    while (True):
        # get input from user
        user_text = str(input("Input text to convert: "))
        # check exit condition
        if user_text == "exit" or user_text == "quit":
            text_to_speech("OK, quiting application.")
            break
            
        text_to_speech(user_text)
