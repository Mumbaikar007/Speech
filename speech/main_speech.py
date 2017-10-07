from tkinter import *
import speechtotext
import openfile
import s2t
import wordinp
import excelinp
import email_send

print("Choose from Following: ")
print("Use voice to complete following tasks")
print("1: Access database\n2: Access files\n3: create Exel Doc\n4: create word doc\n5: send mail")
option_main=int(input().strip())

if(option_main==1):
    s2t.s2t2()
elif(option_main==2):
    openfile.ofile()

elif(option_main==3):
    excelinp.tp()

elif(option_main==4):
    wordinp.word_main()

elif(option_main==5):
    email_send.email_main()

