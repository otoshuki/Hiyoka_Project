from watson_developer_cloud import TextToSpeechV1
from googletrans import Translator as Ts
import speech_recognition as sr
import json

print('Libraries Imported')

text_to_speech = TextToSpeechV1(
    username='d816def2-ebc4-4fec-8845-93362a41fb18',
    password='MdhCKRSjNKkx')

print('Username and Password Set-Up')

rec = sr.Recognizer()
trans = Ts()

def recog():
	try:
		with sr.Microphone() as source:
			rec.adjust_for_ambient_noise(source, duration=0.5)
			print("Say")
			audio = rec.listen(source, timeout = 5.0)
			print('Heard')
			answer = rec.recognize_google(audio)
			rec.operation_timeout = 10

	except:
		answer = 'error'
	return answer

find = recog()
print(type(find))
word = trans.translate(find, dest = 'ja')

with open('', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            word.text, 'audio/wav', 'ja-JP_EmiVoice').content)
