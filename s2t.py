import speech_recognition as sr
import pymysql

print("Important Rules!!")
print("Speech Queries")

print("connect host username password")


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say it!!")
    audio = r.listen(source)


try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
if(r.recognize_google(audio)=='connect'):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='testspeech')

    if(conn):
        cursor=conn.cursor()
        print("successfully connected")
    else:
        print("not connected")


    #sql=('select * from tab1')
    #cursor.execute(sql)
    #data=cursor.fetchall()
    #print(data)
