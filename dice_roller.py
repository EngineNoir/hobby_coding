from tkinter import *
import random


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='# of Die Sides')
        self.lbl2 = Label(win, text='Roll Result')
        self.lbl3 = Label(win, text='# of Die')
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn1 = Button(win, text='Roll Dice')
        self.lbl1.place(x=10, y=50)
        self.t1.place(x=110, y=50)
        self.b1 = Button(win, text='Roll Dice', font=("Helvetica", 14), command=self.roll)
        self.b1.place(x=10, y=80)
        self.b1.config(height=1, width=8)
        self.lbl2.place(x=10, y=130)
        self.t2.place(x=110, y=130)
        self.lbl3.place(x=10, y=20)
        self.t3.place(x=110, y=20)

    def roll(self):
        self.t2.delete(0, 'end')
        n = int(self.t1.get())
        x = int(self.t3.get())
        result = 0
        i = 0
        while i < x:
            result += random.randint(1, n)
            i += 1
        self.t2.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Dice Roller')
window.geometry("250x170+10+10")
window.mainloop()
