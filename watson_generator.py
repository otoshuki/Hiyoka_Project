#Recognition and Translation functions
#Import libraries
from watson_developer_cloud import TextToSpeechV1
from googletrans import Translator
import speech_recognition as sr
import json

#Set username and password tts
text_to_speech = TextToSpeechV1(
    username='d816def2-ebc4-4fec-8845-93362a41fb18',
    password='MdhCKRSjNKkx')

print('Username and Password Set-Up')

rec = sr.Recognizer()
trans = Translator()
punct = '''()-[]{}'"\<>/@#$%^&*_~'''

#Function to unpunctuate the input text
def unpunctuate(text):
	edit = ""
	for char in text:
		if char not in punct:
			edit = edit + char
	return edit

#Recognition using Google web service
def recog():
	try:
        #Get the input
		with sr.Microphone() as source:
			rec.adjust_for_ambient_noise(source, duration=0.5)
			print("Say")
			audio = rec.listen(source, timeout = 3.0)
			print('Heard')
			answer = rec.recognize_google(audio)
			rec.operation_timeout = 10
    #If no input
	except:
		answer = 'error'
	return answer

#Translation using Watson TTS
def translate(in_word,trans_affirm = False):

    print(in_word)

    #If input in english
    if trans_affirm == True:
        #Translate to Japanese
        translated = trans.translate(in_word, dest = 'ja')
        #Save the file
        file = './sounds/' + unpunctuate(in_word).replace(' ','_')
        with open(file, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    translated.text, 'audio/wav', 'ja-JP_EmiVoice').content)
        return file
    #If input in Japanse
    else:
        #Translate to Engish
        translated = trans.translate(in_word, dest = 'en')
        #Save as the translated word
        file = './sounds/' + unpunctuate(translated.text).replace(' ','_')
        with open(file, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    in_word, 'audio/wav', 'ja-JP_EmiVoice').content)
        return file

#Run standalone file
if __name__ == '__main__':
    #translate(recog())
    file = 'test'
    with open(file, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                "c", 'audio/wav', 'ja-JP_EmiVoice').content)
