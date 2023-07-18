from tkinter import *
window = Tk()
window.title("calculator")
window.geometry("600x400")

window.configure(bg="blue")
window.attributes()
#widgets
lb1 = Label(window,text="learn tkinter python")
lb1.pack()
t1 = Entry(window)
t1.pack()
btn = Button(window,text="click me")
btn.pack()
window.mainloop()
