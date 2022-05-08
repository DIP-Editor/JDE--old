from tkinter import *
from tkinter.ttk import *
if __name__ == "__main__":
    window = Tk()
    window.geometry("400x450")
    t = Text(window)
    t.pack()
    for i in range(100):
        t.insert(END, "{}\n".format(i))
    def get_y():
        global y
        y = t.yview()
    b = Button(window, text="get y", command=get_y)
    b.pack()
    b1 = Button(window, text="set y", command=lambda: t.yview_moveto(y[0]))
    b1.pack()
    window.mainloop()