import speech_recognition as sr
import pymysql
import xlwt
import ctypes


#ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

print("Select option from following: ")
print("\n")
print("1: connect to database")
print("\n")
print("2: select table ")
print("\n")

option=input()

r = sr.Recognizer()


if(option=='1'):

    listaudio=[]
    count=0
    print("speak host username password database name ")
    while(count<=1):

        with sr.Microphone() as source:
            print("Say it!!")
            audio = r.listen(source)
            listaudio.append(r.recognize_google(audio))

        try:
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        count+=1

    #
    # speech_audio=r.recognize_google(audio)
    #
    # print("speech testing :"+speech_audio)
    #
    # listaudio=speech_audio.strip().split()
    # print(listaudio)


    host_id=listaudio[0]
    # user_id=listaudio[1]
    # pass_id=''
    db_id=listaudio[1]

    # if(listaudio[3]=='no'):
    #     pass_id=''
    # if(listaudio[2]=='route'):
    #     user_id='root'

    # print(host_id,user_id,pass_id,db_id)
    conn = pymysql.connect(host=str(host_id), user='root', passwd='', db=db_id)

    if(conn):
        cursor=conn.cursor()
        print("successfully connected")
    else:
        print("not connected")

elif(option=='2'):
    listaudio=[]
    count=0
    print("speak tablename ")
    while(count<=0):

        with sr.Microphone() as source:
            print("Say it!!")
            audio = r.listen(source)
            listaudio.append(r.recognize_google(audio))

        try:
            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        count+=1

        conn = pymysql.connect(host='localhost', user='root', passwd='', db='black')

        if(conn):
            cursor=conn.cursor()

            print(listaudio[0])

            sql=('select * from '+listaudio[0])
            cursor.execute(sql)
            data=cursor.fetchall()
            print(data)

        else:
            print("not connected")


else:
    print("invalid query")

        #sql=('select * from tab1')
        #cursor.execute(sql)
        #data=cursor.fetchall()
        #print(data)


#
# #Speech Part
#
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     # print("Speech recognition start")
#     # audio = r.listen(source)
# #
# # try:
# #     print("You said: " + r.recognize_google(audio))
# # except sr.UnknownValueError:
# #     print("Could not understand audio")
# # except sr.RequestError as e:
# #     print("Could not request results; {0}".format(e))
#
# #Speechends
#
#     wb = xlwt.Workbook()
#
#     ws = wb.add_sheet("Test_sheet", True)
#     more = 1
#     while(more == 1):
#         print("Enter row")
#         audio = r.listen(source)
#         row = r.recognize_google(audio)
#         print(row)
#
#         print("Enter Column")
#         audio = r.listen(source)
#         column = r.recognize_google(audio)
#         print(column)
#
#         print("Enter data")
#         # audio = r.listen(source)
#         # string = r.recognize_google(audio)
#
#         string='h'
#         column=int(column)
#         row=int(row)
#
#         ws.write(row, column, string)
#         print("More Values?1:0")
#         more=0
#
#     wb.save("ex1.xls")
