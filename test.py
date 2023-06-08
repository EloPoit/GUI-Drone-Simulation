from tkinter import *

window = Tk()

label = Label(window, text="Hello")
label.pack()

entry = Entry(window)
entry.pack()
entry.focus()



def clicked():
    if entry.get() == "yes" :
        label.configure(text="YESSSSSS")


btn = Button(window, text="Click Me", bg="white", fg="red", command=clicked)
btn.pack()



window.mainloop()
