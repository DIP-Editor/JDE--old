
# from tkinter import *
# from custom_widgets import *

# root = Tk()
# root.geometry("500x500")
# font = Font(family="Courier New bold", size=15)

# def zoom(new_size):
#     new_size = int(new_size)
#     global size
#     if new_size < 25 and new_size > 13:
#         font.configure(size=new_size)
#         size = new_size

# text = Text(root, font=font)

# text.pack(side="left", fill="both", expand=True)

# size = 15

# root.bind("<Command-=>", lambda event: zoom(int(size)+1))
# root.bind("<Command-Key-minus>", lambda event: zoom(int(size)-1))

# root.mainloop()


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


# from tkinter import *
# root=Tk()
# root.geometry("500x400+200+100")

# class Menu_Entry(Entry):
#     def __init__(self,perant,*args,**kwargs):
#         Entry.__init__(self,perant,*args,**kwargs)
#         self.popup_menu=Menu(self,tearoff=0,background='#1c1b1a',fg='white',
#                                      activebackground='#534c5c',
#                              activeforeground='Yellow')
#         self.popup_menu.add_command(label="Cut                     ",command=self.Cut,
#                                     accelerator='Ctrl+V')
#         self.popup_menu.add_command(label="Copy                    ",command=self.Copy,compound=LEFT,
#                                     accelerator='Ctrl+C')
    
#         self.popup_menu.add_command(label="Paste                   ",command=self.Paste,accelerator='Ctrl+V')
#         self.popup_menu.add_separator()
#         self.popup_menu.add_command(label="Select all",command=self.select_all,accelerator="Ctrl+A")
#         self.popup_menu.add_command(label="Delete",command=self.delete_only,accelerator=" Delete")
#         self.popup_menu.add_command(label="Delete all",command=self.delete_selected,accelerator="Ctrl+D")
#         self.bind('<Button-2>',self.popup)
#         self.bind("<Control-d>",self.delete_selected_with_e1)
#         self.bind('<App>',self.popup)
#         self.context_menu = Menu(self, tearoff=0)
#         self.context_menu.add_command(label="Cut")
#         self.context_menu.add_command(label="Copy")
#         self.context_menu.add_command(label="Paste")
         
#     def popup(self, event):
#       try:
#         self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
#       finally:
#         self.popup_menu.grab_release()

#     def Copy(self):
#       self.event_generate('<<Copy>>')

#     def Paste(self):
#       self.event_generate('<<Paste>>')

#     def Cut(self):
#       self.event_generate('<<Cut>>')

#     def delete_selected_with_e1(self,event):
#       self.select_range(0, END)
#       self.focus()
#       self.event_generate("<Delete>")

#     def delete_selected(self):
#       self.select_range(0, END)
#       self.focus()
#       self.event_generate("<Delete>")

#     def delete_only(self):
#       self.event_generate("<BackSpace>")

#     def select_all(self):
#       self.select_range(0, END)
#       self.focus()



# ent=Menu_Entry(root)
# ent.pack()

# root.mainloop()


# from tkinter import *
# root=Tk()
# root.iconify()
# root.geometry("500x400+200+100")
# root.deiconify()
# root.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# root = Tk()
# s = Style()
# s.theme_use('clam')
# p = Progressbar(root, orient=HORIZONTAL, length=200, mode='indeterminate')
# p.pack(expand=True, fill=BOTH)
# p.start()
# root.mainloop()

# import sys

# import tkinter
# import tkinter.scrolledtext


# class Application:
#     def __init__(self):
#         # Create UI
#         self.window = tkinter.Tk()
#         self.window.geometry('800x600')
#         self.window.title("Tk-based event logger")

#         self.text_view = tkinter.scrolledtext.ScrolledText()
#         self.text_view.pack(fill=tkinter.BOTH, expand=1)
#         self.text_view.configure(state='disabled')

#         # Register event handlers
#         # See https://tcl.tk/man/tcl/TkCmd/tk_mac.html for list of
#         # macOS-specific commands
#         self.window.createcommand("::tk::mac::OpenDocument", self.open_document_handler)
#         self.window.createcommand("::tk::mac::LaunchURL", self.open_url_handler)  # works with Tcl/Tk >= 8.6.10

#     def append_message(self, msg):
#         """Append message to text view."""
#         self.text_view.configure(state='normal')
#         self.text_view.insert('end', msg + '\n')
#         self.text_view.configure(state='disabled')

#     def run(self):
#         """Run the main loop."""
#         app.append_message("Application started!")
#         app.append_message(f"Args: {sys.argv[1:]}")
#         self.window.mainloop()

#     # Event handlers
#     def open_document_handler(self, *args):
#         app.append_message(f"Open document event: {args}")

#     def open_url_handler(self, *args):
#         app.append_message(f"Open URL event: {args}")


# if __name__ == '__main__':
#     app = Application()
#     app.run()


# def callback(widget):
#     msg = widget.get()
#     msg = emojify(msg)
#     conn.sendall(msg)
#     tkmsg = with_surrogates(msg)
#     msglog.append(f'>>> {tkmsg}')

# def on_msg(msg):
#     tkmsg = with_surrogates(msg)
#     msglog.append(tkmsg)

import tkinter as tk

# Python 3.8.3
class Application(tk.Frame):
    def __init__(self, master=None):
        self.canvas = None
        self.quit_button = None
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=500, height=420, bg='yellow')
        #save the ID
        self.text_id = self.canvas.create_text(250, 200, font="* 180", text='\U0001F43F')
        self.canvas.grid()
        ##
        #
        chipmunk_utf_32 = '\U0001F43F'
        chipmunk_utf_16 = chipmunk_utf_32.encode('utf-16-be')
        chipmunk_utf_16 = chipmunk_utf_16.hex()
        chipmunk = '\\u{}\\u{}'.format(chipmunk_utf_16[0:4], chipmunk_utf_16[4:8])
        self.canvas.tk.eval('set the_tcl_chipmunk {}'.format(chipmunk))
        self.canvas.tk.eval( '{} itemconfig {} -text [set the_tcl_chipmunk]'.format( str(self.canvas), self.text_id ) )
        #
        ##
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()

app = Application()
app.master.title('Emoji')
app.mainloop()