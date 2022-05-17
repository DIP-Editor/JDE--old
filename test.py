
from tkinter import *
from custom_widgets import *

root = Tk()
root.geometry("500x500")
font = Font(family="Courier New bold", size=15)

def zoom(new_size):
    new_size = int(new_size)
    global size
    if new_size < 25 and new_size > 13:
        font.configure(size=new_size)
        size = new_size

text = Text(root, font=font)

text.pack(side="left", fill="both", expand=True)

size = 15

root.bind("<Command-=>", lambda event: zoom(int(size)+1))
root.bind("<Command-Key-minus>", lambda event: zoom(int(size)-1))

root.mainloop()


# import tkinter as tk
# from tkinter.font import Font

# root = tk.Tk()
# root.geometry("500x500")
# font = Font(family="Courier New bold", size=15)

# def zoom(size):
#     font.configure(size=size)

# zoom_scale = tk.Scale(root, orient="vertical", from_=1, to=500)
# zoom_scale.config(command=zoom)
# text = tk.Text(root, font=font)

# zoom_scale.pack(fill="y", side="right")
# text.pack(side="left", fill="both", expand=True)

# zoom_scale.set(15)

# root.mainloop()



# from tkinter import *
# from tkinter.scrolledtext import ScrolledText

# def add_image():
#     text.image_create(1.0, image = img, justify=CENTER) # Example 1

# root = Tk()

# text = ScrolledText(root)
# text.pack(padx = 20, pady = 20)
# super_long_string = ""
# for i in range(100):
#     super_long_string += "This is line dhjgfjshdgfjhdg jfahsg jahsgf jhsg fjshg fhjdajhadsgsjahgsajh sfgjashgfjhsag jhsag jhsag fhjg fadjhga fsjhsfgahjfasg jahsg safjhg sfajhfgs ajhsfgahjfsag jhfsg fjhs gfsjhgsfjhgsfjhgsfjhsgjhasg hjsagfjhsg sfjhgs jhagsjhsagjhfsgjhsfg sahjg sahjgs afhjsfg jhsag jfshgfsjhg fsjhgfs jhfsga \n"
# text.insert(END, super_long_string)

# Button(root, text = "Insert", command = add_image).pack()
# img = PhotoImage(file = "extensions.png")
# root.mainloop()



# from tkinter import *
# from tkinter.ttk import *
# window = Tk()
# s = Style(window)
# s.theme_use("clam")
# notebook = Notebook()
# notebook.pack(fill=BOTH, expand=True)
# py_imgs = []
# txt_images = []
# def add_tab():
#     py_imgs.append(PhotoImage(file="python.png"))
#     txt_images.append(PhotoImage(file="txt.png"))
#     frame = Frame()
#     notebook.add(frame, image=py_imgs[len(py_imgs)-1], text="Hello", compound=LEFT)
#     frame = Frame()
#     notebook.add(frame, image=txt_images[len(txt_images)-1], text="World", compound=LEFT)
# def delete_tab():
#     index = notebook.index(notebook.select())
#     #Delete image with index
#     py_imgs.pop(index)
#     #Delete tab with index
#     notebook.forget(notebook.select())
# for i in range(5):
#     add_tab()
# add_tab_btn = Button(window, text="Add Tab", command=add_tab)
# add_tab_btn.pack(side=BOTTOM)
# delete_tab_btn = Button(window, text="Delete Tab", command=delete_tab)
# delete_tab_btn.pack(side=BOTTOM)
# window.mainloop()



# from tkinter import *
# from tkinter import ttk
# root = Tk()

# h = ttk.Scrollbar(root, orient=HORIZONTAL)
# v = ttk.Scrollbar(root, orient=VERTICAL)
# canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
# h["command"] = canvas.xview
# v["command"] = canvas.yview

# canvas.grid(column=0, row=0, sticky=(N,W,E,S))
# h.grid(column=0, row=1, sticky=(W,E))
# v.grid(column=1, row=0, sticky=(N,S))
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

# lastx, lasty = 0, 0

# def xy(event):
#     global lastx, lasty
#     lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

# def setColor(newcolor):
#     global color
#     color = newcolor
#     canvas.dtag("all", "paletteSelected")
#     canvas.itemconfigure("palette", outline="white")
#     canvas.addtag("paletteSelected", "withtag", "palette%s" % color)
#     canvas.itemconfigure("paletteSelected", outline="#999999")

# def addLine(event):
#     global lastx, lasty
#     x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
#     canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags="currentline")
#     lastx, lasty = x, y

# def doneStroke(event):
#     canvas.itemconfigure("currentline", width=1)        
        
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)
# canvas.bind("<B1-ButtonRelease>", doneStroke)

# id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=("palette", "palettered"))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
# id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=("palette", "paletteblue"))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
# id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=("palette", "paletteblack", "paletteSelected"))
# canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

# setColor("black")
# canvas.itemconfigure("palette", width=5)
# root.mainloop()



# from tkinter import *
# import sys
# from pathlib import Path
# #Get path (Used for application)
# if getattr(sys, "frozen", False):
#     folder = Path(sys._MEIPASS)
# else:
#     folder = Path(__file__).parent
# #Get color theme from file
# theme_style = open(folder / "color_theme.txt", "r").readlines()
# light_mode_style = theme_style[0].split(";")
# light_mode_bg = light_mode_style[0].split(": ")[1].split("=")[1]
# light_mode_fg = light_mode_style[1].split("=")[1].split(";")[0]
# dark_mode_style = theme_style[1].split(";")
# dark_mode_bg = dark_mode_style[0].split(": ")[1].split("=")[1]
# dark_mode_fg = dark_mode_style[1].split("=")[1].split(";")[0]
# #Get Font from file
# font_style = open(folder / "font.txt", "r").readlines()
# font_name = font_style[0].split("\n")[0]
# normal_size = int(font_style[1].split("\n")[0])
# medium_size = int(font_style[2].split("\n")[0])
# large_size = int(font_style[3].split("\n")[0])
# normal_font = (font_name, normal_size)
# medium_font = (font_name, medium_size)
# large_font = (font_name, large_size)

# class FlowChart(Frame):
#     def __init__(self,  *args, **kwargs):
#         #Get necessary arguments
#         self.color_mode = kwargs.pop("color_mode")
#         self.x = kwargs.pop("x")
#         self.y = kwargs.pop("y")
#         #Create the frame
#         Frame.__init__(self, *args, **kwargs)
#         #Create the colors
#         if self.color_mode == "Dark":
#             self.bg = dark_mode_bg
#             self.fg = dark_mode_fg
#         else:
#             self.bg = light_mode_bg
#             self.fg = light_mode_fg
#         #Create the window
#         self.flowchart_window = Toplevel(self)
#         self.flowchart_window.title("Flowchart")
#         self.flowchart_window.geometry("500x500+{}+{}".format(self.x, self.y))
#         self.flowchart_window.resizable(False, False)
#         self.flowchart_window.configure(background=self.bg)
#         #Create the toolbar
#         self.toolbar = Frame(self.flowchart_window, bg="#e0dcd4", width=100)
#         self.toolbar.pack(side=LEFT, fill=Y)
#         #Create the canvas
#         self.canvas = Canvas(self.flowchart_window, bg=self.bg)
#         self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)
#         #Create the buttons
#         self.draw_button = Button(self.toolbar, text="Draw", command=self.draw_line)
#         self.draw_button.place(relx=0.5, rely=0.05, anchor=CENTER)
#         self.draw_button.configure(highlightbackground="#e0dcd4")
#         self.erase_button = Button(self.toolbar, text="Erase", command=self.erase_line)
#         self.erase_button.place(relx=0.5, rely=0.1, anchor=CENTER)
#         self.erase_button.configure(highlightbackground="#e0dcd4")
#         self.clear_button = Button(self.toolbar, text="Clear", command=self.clear_canvas)
#         self.clear_button.place(relx=0.5, rely=0.15, anchor=CENTER)
#         self.clear_button.configure(highlightbackground="#e0dcd4")
#         self.draw_box_button = Button(self.toolbar, text="Box", command=self.draw_box)
#         self.draw_box_button.place(relx=0.5, rely=0.2, anchor=CENTER)
#         self.draw_box_button.configure(highlightbackground="#e0dcd4")
#         self.draw_rounded_box_button = Button(self.toolbar, text="Rounded Box", command=self.draw_rounded_box)
#         self.draw_rounded_box_button.place(relx=0.5, rely=0.25, anchor=CENTER)
#         self.draw_rounded_box_button.configure(highlightbackground="#e0dcd4")
#         self.draw_parallelogram_button = Button(self.toolbar, text="Parallelogram", command=self.draw_parallelogram)
#         self.draw_parallelogram_button.place(relx=0.5, rely=0.3, anchor=CENTER)
#         self.draw_parallelogram_button.configure(highlightbackground="#e0dcd4")
#         self.draw_diamond_button = Button(self.toolbar, text="Diamond", command=self.draw_diamond)
#         self.draw_diamond_button.place(relx=0.5, rely=0.35, anchor=CENTER)
#         self.draw_diamond_button.configure(highlightbackground="#e0dcd4")
#         self.draw_text_button = Button(self.toolbar, text="Text", command=self.draw_text)
#         self.draw_text_button.place(relx=0.5, rely=0.4, anchor=CENTER)
#         self.draw_text_button.configure(highlightbackground="#e0dcd4")
#         self.canvas.bind("<Button-1>", self.draw_line)

#     def draw_line(self, event=None):
#         #Create line at mouse position
#         self.canvas.create_line(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), fill=self.fg)

#     def erase_line(self, event=None):
#         #Erase anything at mouse position
#         self.canvas.delete(self.canvas.find_closest(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery()))

#     def clear_canvas(self, event=None):
#         #Clear the canvas
#         self.canvas.delete("all")

#     def draw_box(self, event=None):
#         #Create box at mouse position
#         self.canvas.create_rectangle(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), self.canvas.winfo_pointerx() + 100, self.canvas.winfo_pointery() + 100)

#     def draw_rounded_box(self, event=None):
#         #Create rounded box at mouse position
#         self.canvas.create_oval(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), self.canvas.winfo_pointerx() + 200, self.canvas.winfo_pointery() + 100)

#     def draw_parallelogram(self, event=None):
#         #Create parallelogram at mouse position
#         self.canvas.create_polygon(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), self.canvas.winfo_pointerx() + 100, self.canvas.winfo_pointery() + 100, self.canvas.winfo_pointerx() + 200, self.canvas.winfo_pointery() + 100)

#     def draw_diamond(self, event=None):
#         #Create diamond at mouse position
#         self.canvas.create_polygon(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), self.canvas.winfo_pointerx() + 100, self.canvas.winfo_pointery() + 100, self.canvas.winfo_pointerx() + 50, self.canvas.winfo_pointery() + 150, self.canvas.winfo_pointerx(), self.canvas.winfo_pointery() + 100)

#     def draw_text(self, event=None):
#         #Create text at mouse position
#         self.canvas.create_text(self.canvas.winfo_pointerx(), self.canvas.winfo_pointery(), text="Text")

# if __name__ == "__main__":
#     window = Tk()
#     FlowChart(color_mode="Dark", x=100, y=100).pack(fill=BOTH, expand=True)
#     window.mainloop()
