from watson_developer_cloud import TextToSpeechV1
from googletrans import Translator
import speech_recognition as sr
import json

text_to_speech = TextToSpeechV1(
    username='d816def2-ebc4-4fec-8845-93362a41fb18',
    password='MdhCKRSjNKkx')

print('Username and Password Set-Up')

rec = sr.Recognizer()
trans = Translator()

#Recognition using Google web service
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

#Translation using Watson TTS
def translate(in_word,trans_affirm = False):

    print(in_word)

    #If input in english
    if trans_affirm == True:
        #Translate to Japanese
        translated = trans.translate(in_word, dest = 'ja')
        #Save the file
        file = './sounds/' + in_word
        with open(file, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    translated.text, 'audio/wav', 'ja-JP_EmiVoice').content)
    #If input in Japanse
    else:
        #Translate to Engish
        translated = trans.translate(in_word, dest = 'en')
        #Save as the translated word
        file = './sounds/' + translated.text
        with open(file, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    in_word, 'audio/wav', 'ja-JP_EmiVoice').content)

if __name__ == '__main__':
    #translate(recog())
    file = './sounds/' + 'ok'
    with open(file, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                "了解しました", 'audio/wav', 'ja-JP_EmiVoice').content)
