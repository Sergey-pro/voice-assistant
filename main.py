import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()
#r = sr.Recognizer()
#with sr.Microphone(device_index=1) as sourse:
#    print('Скажите что-нибудь...')
#   audio = r.listen(sourse)

#query = r.recognize_google(audio, language="RU")
#if query == 'время':
#	now = datetime.datetime.now()
#	engine.say("Сейчас " + str(now.hour) + ":" + str(now.minute))
#	engine.runAndWait()
#else:
#	engine.say('Вы сказали ' + query)
#	engine.runAndWait()
engine.say('хэй')
engine.say('И если под этим роликом наберётся 5 лайкав, то выйдет продолжение!')
engine.runAndWait()