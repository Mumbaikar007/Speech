# from tkinter import *

# root = Tk()

# frametop = Frame(root)
# framebottom = Frame(root)
# frameleft = Frame(framebottom)
# frameright = Frame(framebottom)

# text = Text(frametop)
# scroll = Scrollbar(frametop, command=text.yview)
# btn1 = Button(frameleft, text="Course")
# btn2 = Button(frameleft, text="Abscences")
# btn3 = Button(frameright, text="Notes")
# btn4 = Button(frameright, text="Return")

# text['yscrollcommand'] = scroll.set

# frametop.pack(side=TOP, fill=BOTH, expand=1)
# framebottom.pack(side=BOTTOM, fill=BOTH, expand=1)
# frameleft.pack(side=LEFT, fill=BOTH, expand=1)
# frameright.pack(side=RIGHT, fill=BOTH, expand=1)

# text.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
# scroll.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)
# btn1.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
# btn2.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)
# btn3.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
# btn4.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)

# root.mainloop()

from tkinter import *

root = Tk()

button_frame = Frame(root)
button_frame.pack(fill=X, side=BOTTOM)

reset_button = Button(button_frame, text='Reset')
run_button = Button(button_frame, text='Run')

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

reset_button.grid(row=0, column=0, sticky=W+E)
run_button.grid(row=0, column=1, sticky=W+E)

root.mainloop()