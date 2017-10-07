from tkinter import *

root = Tk()
logo = PhotoImage(file="index.gif")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w = Label(root, 
          compound = CENTER,
          text=explanation, 
          image=logo,  padx=5, pady=5).pack(side="right")

root.mainloop()