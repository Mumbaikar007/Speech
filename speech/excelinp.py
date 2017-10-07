import xlwt
import speechtotext
import speech_recognition as sr



#Speech Part



    # print("Speech recognition start")
    # audio = r.listen(source)

# try:
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))

#Speechends

def tp():
    wb = xlwt.Workbook()

    ws = wb.add_sheet("Test_sheet", True)
    more = 1
    while(more == 1):
        print("Enter row")

        row = speechtotext.stot()
        print(row)

        print("Enter Column")

        column = speechtotext.stot()
        print(column)

        print("Enter data")
        # audio = r.listen(source)
        # string = r.recognize_google(audio)

        string='h'
        column=int(column)
        row=int(row)

        ws.write(row, column, string)
        print("More Values?1:0")
        more=0

    wb.save("ex1.xls")


