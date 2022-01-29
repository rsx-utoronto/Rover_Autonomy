from google.cloud import texttospeech
from playsound import playsound
import os

def text_to_speech(text, client, voice, audio_config):
    synthesis_input = synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # play the audio
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    playsound("output.mp3")
    os.remove("output.mp3")
    
    

# Set the text input to be synthesized
if __name__ == '__main__':
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your key here.json"
    client = texttospeech.TextToSpeechClient() # note: this needs a valid key, see documentation for details

    # configure the voice
    accents = ["Australian: en-AU", "Indian: en-IN", "UK: en-GB", "US: en-US", "Chinese: cmn-CN"]
    for accent in accents:
        print(accent)
    language = str(input("\nChoose an accent from the list above: "))

    gender = str(input("Choose a gender (M/F/N): "))
    if gender == "M":
        gender = texttospeech.SsmlVoiceGender.MALE
    elif gender == "F":
        gender = texttospeech.SsmlVoiceGender.FEMALE
    else:
        gender = texttospeech.SsmlVoiceGender.NEUTRAL

    # set up voice parameters
    # Build the voice request, select the language code and the ssml
    voice = texttospeech.VoiceSelectionParams(
        language_code=language, ssml_gender=gender
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # demo
    while (True):
        # get input from user
        user_text = str(input("Input text to convert: "))
        if user_text == "exit" or user_text == "quit":
            text_to_speech("OK, quiting application", client, voice, audio_config)
            break
            
        text_to_speech(user_text, client, voice, audio_config)
