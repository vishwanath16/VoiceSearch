import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    audio = r3.listen(source)
    r2 = sr.Recognizer()
    url = 'https://www.amazon.in/s?k='
    with sr.Microphone() as source:
        print('which product you want to search?')
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError as e:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

