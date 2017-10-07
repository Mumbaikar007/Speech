from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("500x500")


# logo = PhotoImage(file="index.gif")
# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface 
# exists to allow additional image file
# formats to be added easily."""

# w = Label(root, 
#           compound = CENTER,
#           text=explanation, 
#           image=logo).pack(side="right")


im = Image.open("index.png")
resized = im.resize((100, 100),Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(resized)
myvar=Label(root, 
            compound = CENTER,
            text= "Data Ease",
            fg = "dark red",
            font = "Helvetica 16 bold italic", 
            image=tkimage)
myvar.image = tkimage
myvar.grid(row=0,column=0, columnspan=5)   

#w.config(height=20)
#w.grid(row=0, column=0, columnspan=5)

myButton1 = Button( text = 'Database', fg = 'blue', bg = 'green' ,padx=10, pady=10 ) 
myButton2 = Button( text = 'Excel', fg = 'blue', bg = 'green' ,padx=10, pady=10 )
myButton3 = Button( text = 'Word', fg = 'blue', bg = 'green' ,padx=10, pady=10)
myButton4 = Button( text = 'Email', fg = 'blue', bg = 'green' ,padx=10, pady=10)
myButton5 = Button( text = 'File', fg = 'blue', bg = 'green' ,padx=10, pady=10)



myButton1.grid(row=1,column=0)
myButton2.grid(row=1,column=1)
myButton3.grid(row=1,column=2)
myButton4.grid(row=1,column=3)
myButton5.grid(row=1,column=4)

root.mainloop() 	