
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
# import random
# window = Tk()
# s = Style(window)
# s.theme_use("clam")
# notebook = Notebook()
# notebook.pack(fill=BOTH, expand=True)
# index = 0
# def add_tab(event=None):
#     global index
#     frame = Text(notebook)
#     frame.insert("1.0", "This is text {}".format(index))
#     notebook.add(frame, text="Hello {}".format(index))
#     index += 1
#     notebook.select(frame)
# def delete_tab(event=None):
#     if len(notebook.tabs())>1:
#         index = notebook.index("current")
#         notebook.forget(notebook.select())
#         if len(notebook.tabs())>index:
#             notebook.select(index)
# def change_tab(event=None, index=None):
#     if index==None:
#         number = int(event.keysym)-1
#     else:
#         number = index
#     if len(notebook.tabs()) > number:
#         notebook.select(number)
# add_tab_btn = Button(window, text="Add Tab", command=add_tab)
# add_tab_btn.pack(side=BOTTOM)
# delete_tab_btn = Button(window, text="Delete Tab", command=delete_tab)
# delete_tab_btn.pack(side=BOTTOM)
# def show_issue(event=None):
#     add_tab()
#     add_tab()
#     #Change tabs 20 times with random indexes in the range of the tab count
#     tab_count = len(notebook.tabs())
#     for i in range(20):
#         change_tab(index=int(random.randint(0, tab_count-1)))
#     delete_tab()
# show_error_btn = Button(window, text="Show Error", command=show_issue)
# show_error_btn.pack(side=BOTTOM)
# window.bind("<Command-Key-1>", change_tab)
# window.bind("<Command-Key-2>", change_tab)
# window.bind("<Command-Key-3>", change_tab)
# window.bind("<Command-Key-4>", change_tab)
# window.bind("<Command-Key-5>", change_tab)
# window.bind("<Command-Key-6>", change_tab)
# window.bind("<Command-Key-7>", change_tab)
# window.bind("<Command-Key-8>", change_tab)
# window.bind("<Command-Key-9>", change_tab)
# window.bind("<Command-t>", add_tab)
# for i in range(5):
#     add_tab()
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

# import tkinter as tk

# # Python 3.8.3
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         self.canvas = None
#         self.quit_button = None
#         tk.Frame.__init__(self, master)
#         self.grid()
#         self.create_widgets()

#     def create_widgets(self):
#         self.canvas = tk.Canvas(self, width=500, height=420, bg='yellow')
#         #save the ID
#         self.text_id = self.canvas.create_text(250, 200, font="* 180", text='\U0001F43F')
#         self.canvas.grid()
#         ##
#         #
#         chipmunk_utf_32 = '\U0001F43F'
#         chipmunk_utf_16 = chipmunk_utf_32.encode('utf-16-be')
#         chipmunk_utf_16 = chipmunk_utf_16.hex()
#         chipmunk = '\\u{}\\u{}'.format(chipmunk_utf_16[0:4], chipmunk_utf_16[4:8])
#         self.canvas.tk.eval('set the_tcl_chipmunk {}'.format(chipmunk))
#         self.canvas.tk.eval( '{} itemconfig {} -text [set the_tcl_chipmunk]'.format( str(self.canvas), self.text_id ) )
#         #
#         ##
#         self.quit_button = tk.Button(self, text='Quit', command=self.quit)
#         self.quit_button.grid()

# app = Application()
# app.master.title('Emoji')
# app.mainloop()


# from tkinter import *
# from tkcode import *
# window = Tk()
# codeEditor = CodeEditor(window)
# codeEditor.pack()
# window.mainloop()


# from tkinter import *
# window = Tk()
# #Create a text widget with lots of text in it
# text = Text(window, height=20, width=30)
# text.pack()
# text.insert(END, "This is a text widget inside of a window.")
# #Add a green tag to all of the text
# text.tag_remove("green", "1.0", END)
# text.tag_add("green", "1.4", "1.18")
# text.tag_config("green", foreground="green")
# window.mainloop()

# from tkinter import *
# from pygments import lex
# from pygments.lexers import PythonLexer
# root = Tk()
# textPad = Text(root, width=100, height=80)
# textPad.tag_configure("Token.Comment", foreground="#b21111")
# code = textPad.get("1.0", "end-1c")
# # Parse the code and insert into the widget
# def syn(event=None):
#     textPad.mark_set("range_start", "1.0")
#     data = textPad.get("1.0", "end-1c")
#     for token, content in lex(data, PythonLexer()):
#         textPad.mark_set("range_end", "range_start + %dc" % len(content))
#         textPad.tag_add(str(token), "range_start", "range_end")
#         textPad.mark_set("range_start", "range_end")
#     print(textPad.tag_names())
# textPad.pack()
# root.bind("<KeyRelease>", syn)
# root.mainloop()


# from tkinter import *
# from collections import deque
 
 
# class Window:
#     def __init__(self, master):
#         self.master = master
#         self.master.option_add("*Font", "Verdana 12")
 
#         self.Main = Frame(self.master)
 
#         self.stack = deque(maxlen = 10)
#         self.stackcursor = 0
 
#         self.L1 = Label(self.Main, text = "This is my Code Editor")
#         self.L1.pack(padx = 5, pady = 5)
 
 
#         #---------
 
#         self.T1 = Text(self.Main, width = 90, height = 25)
 
#         self.T1.tag_configure("orange", foreground = "orange", font = "Verdana 12")
#         self.T1.tag_configure("blue", foreground = "blue", font = "Verdana 12")
#         self.T1.tag_configure("purple", foreground = "purple", font = "Verdana 12")
#         self.T1.tag_configure("green", foreground = "green", font = "Verdana 12")
#         self.T1.tag_configure("red", foreground = "red", font = "Verdana 12")
 
#         self.tags = ["orange", "blue", "purple", "green", "red"]
 
#         self.wordlist = [ ["class", "def", "for", "if", "else", "elif", "import", "from", "as", "break", "while"],
#                           ["int", "string", "float", "bool", "__init__"],
#                           ["pygame", "tkinter", "sys", "os", "mysql"],
#                           ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] ]
 
#         self.T1.bind("<Return>", lambda event: self.indent(event.widget))
         
#         self.T1.pack(padx = 5, pady = 5)
 
#         #---------
 
#         self.menu = Menu(self.Main)
#         self.menu.add_command(label = "Print", command = self.print_stack)
#         self.menu.add_command(label = "Undo", command = self.undo)
#         self.menu.add_command(label = "Redo", command = self.redo)
 
#         self.master.config(menu = self.menu)
 
#         self.B1 = Button(self.Main, text = "Print", width = 8, command = self.display)
#         self.B1.pack(padx = 5, pady = 5, side = LEFT)
 
#         self.B2 = Button(self.Main, text = "Clear", width = 8, command = self.clear)
#         self.B2.pack(padx = 5, pady = 5, side = LEFT)
 
#         self.B3 = Button(self.Main, text = "Undo", width = 8, command = self.undo)
#         self.B3.pack(padx = 5, pady = 5, side = LEFT)
 
#         self.B4 = Button(self.Main, text = "Redo", width = 8, command = self.redo)
#         self.B4.pack(padx = 5, pady = 5, side = LEFT)
 
#         self.Main.pack(padx = 5, pady = 5)
 
 
#     def tagHighlight(self):
#         start = "1.0"
#         end = "end"
         
#         for mylist in self.wordlist:
#             num = int(self.wordlist.index(mylist))
 
#             for word in mylist:
#                 self.T1.mark_set("matchStart", start)
#                 self.T1.mark_set("matchEnd", start)
#                 self.T1.mark_set("SearchLimit", end)
 
#                 mycount = IntVar()
                 
#                 while True:
#                     index= self.T1.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
 
#                     if index == "": break
#                     if mycount.get() == 0: break
 
#                     self.T1.mark_set("matchStart", index)
#                     self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
 
#                     preIndex = "%s-%sc" % (index, 1)
#                     postIndex = "%s+%sc" % (index, mycount.get())
                     
#                     if self.check(index, preIndex, postIndex):
#                         self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")
                         
 
#     def check(self, index, pre, post):
#         letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
#                    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
 
#         if self.T1.get(pre) == self.T1.get(index):
#             pre = index
#         else:
#             if self.T1.get(pre) in letters:
#                 return 0
 
#         if self.T1.get(post) in letters:
#             return 0
 
#         return 1
 
 
#     def scan(self):
#         start = "1.0"
#         end = "end"
#         mycount = IntVar()
 
#         regex_patterns = [r'".*"', r'#.*']
 
#         for pattern in regex_patterns:
#             self.T1.mark_set("start", start)
#             self.T1.mark_set("end", end)
 
#             num = int(regex_patterns.index(pattern))
 
#             while True:
#                 index = self.T1.search(pattern, "start", "end", count=mycount, regexp = True)
 
#                 if index == "": break
 
#                 if (num == 1):
#                     self.T1.tag_add(self.tags[4], index, index + " lineend")
#                 elif (num == 0):
#                     self.T1.tag_add(self.tags[3], index, "%s+%sc" % (index, mycount.get()))
 
#                 self.T1.mark_set("start", "%s+%sc" % (index, mycount.get()))
 
 
#     def indent(self, widget):
 
#         index1 = widget.index("insert")
#         index2 = "%s-%sc" % (index1, 1)
#         prevIndex = widget.get(index2, index1)
 
#         prevIndentLine = widget.index(index1 + "linestart")
#         print("prevIndentLine ",prevIndentLine)
#         prevIndent = self.getIndex(prevIndentLine)
#         print("prevIndent ", prevIndent)
 
 
#         if prevIndex == ":":
#             widget.insert("insert", "\n" + "     ")
#             widget.mark_set("insert", "insert + 1 line + 5char")
 
#             while widget.compare(prevIndent, ">", prevIndentLine):
#                 widget.insert("insert", "     ")
#                 widget.mark_set("insert", "insert + 5 chars")
#                 prevIndentLine += "+5c"
#             return "break"
         
#         elif prevIndent != prevIndentLine:
#             widget.insert("insert", "\n")
#             widget.mark_set("insert", "insert + 1 line")
 
#             while widget.compare(prevIndent, ">", prevIndentLine):
#                 widget.insert("insert", "     ")
#                 widget.mark_set("insert", "insert + 5 chars")
#                 prevIndentLine += "+5c"
#             return "break"
 
 
#     def getIndex(self, index):
#         while True:
#             if self.T1.get(index) == " ":
#                 index = "%s+%sc" % (index, 1)
#             else:
#                 return self.T1.index(index)
            
                    
#     def update(self):
#         self.stackify()
#         self.tagHighlight()
#         self.scan()
 
#     def display(self):
#         print(self.T1.get("1.0", "end"))     
 
#     def clear(self):
#         self.T1.delete("1.0", "end")
 
#     def stackify(self):
#         self.stack.append(self.T1.get("1.0", "end - 1c"))
#         if self.stackcursor < 9: self.stackcursor += 1
 
#     def undo(self):
#         if self.stackcursor != 0:
#             self.clear()
#             if self.stackcursor > 0: self.stackcursor -= 1
#             self.T1.insert("0.0", self.stack[self.stackcursor])
 
#     def redo(self):
#         if len(self.stack) > self.stackcursor + 1:
#             self.clear()
#             if self.stackcursor < 9: self.stackcursor += 1
#             self.T1.insert("0.0", self.stack[self.stackcursor])
 
#     def print_stack(self):
#         i = 0
#         for stack in self.stack:
#             print(str(i) + " " + stack)
#             i += 1
 
                      
# root = Tk()
# window = Window(root)
# root.bind("<Key>", lambda event: window.update())
# root.mainloop()

# from tkinter import *
# window = Tk()
# Button(window, text="Example", font=("Courier New bold", 15)).pack()
# window.mainloop()


# class Patient:
#     def __init__(self, case_number, name, age):
#         self.case_number = case_number
#         self.name = name
#         self.age = age
#         self.notes = []

#     def change_name(self, new_name):
#         self.name = new_name
    
#     def change_age(self, new_age):
#         self.age = new_age

#     def change_case_number(self, new_case_number):
#         self.case_number = new_case_number
    
#     def get_info(self):
#         return (self.case_number, self.name, self.age)

#     def add_note(self, note):
#         self.notes.append(note)

# patients = []
# while True:
#     decision = input("Would you like to:\nA) Add a patient\nB) Remove a patient\nC) Get all patient info\nD) Get info from index\nE) Get index from case number\n?) ")
#     if decision == "A":
#         case_number = input("Enter the case number: ")
#         name = input("Enter the name: ")
#         age = input("Enter the age: ")
#         patients.append(Patient(case_number, name, age))
#     elif decision == "B":
#         case_number = input("Enter the case number: ")
#         for patient in patients:
#             if patient.case_number == case_number:
#                 patients.remove(patient)
#                 break
#     elif decision == "C":
#         for patient in patients:
#             print(patient.get_info())
#     elif decision == "D":
#         index = input("Enter the index: ")
#         print(patients[index].get_info())
#     elif decision == "E":
#         case_number = input("Enter the case number: ")
#         for patient in patients:
#             if patient.case_number == case_number:
#                 print(patients.index(patient))

# from tkinter import *
# root = Tk()
# the_button = Button().pack()
# menu = Menu(root)
# for i in ('One', 'Two', 'Three'):
#     menu.add_command(label=i)
# if (root.tk.call('tk', 'windowingsystem')=='aqua'):
#     root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
#     root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
# else:
#     root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
# root.mainloop()

# from tkinter import *
# root = Tk()
# menu = Menu(root)
# for i in ('One', 'Two', 'Three'):
#     menu.add_command(label=i)
# if (root.tk.call('tk', 'windowingsystem')=='aqua'):
#     root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
#     root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
# else:
#     root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
# root.mainloop()

# import os
# file = "/Users/joshyacktman/Desktop/JDE/JDE.pdf"
# # command = "open -a Preview {}".format(file)
# # command = "osascript print {} dialog true".format(file)
# command = "lpr {}".format(file)
# os.system(command)



# test .startswith()

# print("hello".startswith("h"))
# words = ['from', 'tkinter', 'i', 'import', 'font', 'window', 'Tk', 'winfo_screenwidth', 'winfo_screenheight', 'relx', 'rely', 'text', 'anchor', 'CENTER', 'mainloop', 'geometry', 'Label', 'Button', 'Text', 'Entry', 'pack', 'place', 'grid', 'False', 'await', 'else', 'pass', 'None', 'break', 'except', 'in', 'range', 'raise', 'True', 'class', '__init__', 'finally', 'is', 'return', 'and', 'continue', 'lambda', 'try', 'as', 'def', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with', 'async', 'elif', 'if', 'or', 'yield', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'for', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 'breakpoint']
# word = "f"
# matches = [x for x in words if x.startswith(word)]
# print(matches)

from tukaan import App, Label
app = App("Test")
main_label = Label(app, text="Hello", tooltip="Yellow bugs\nstay tyello\nyooo")
main_label.grid()
app.run()

# import tkinter
# window = tkinter.Tk()
# window.eval("""
# ttk::style theme use clam
# set n [ttk::notebook .nb]
# pack $n -fill both -expand 1

# #Create tabs
# foreach tab [list First Second Third] {
#     set w [frame $n.[string tolower $tab]]
#     label $w.src_lab -text "Clicked Tab Index:" -anchor e
#     label $w.src_idx -textvariable src_index -width 3
#     label $w.dst_lab -text "Released Tab Index:" -anchor e
#     label $w.dst_idx -textvariable dst_index -width 3
#     grid $w.src_lab $w.src_idx -sticky news
#     grid $w.dst_lab $w.dst_idx -sticky news
#     $n add $w -text $tab
# }

# #Bindings
# bind all <KeyPress-question> {console show}
# bind $n <ButtonPress>   [list click   %W %x %y]
# bind $n <ButtonRelease> [list release %W %x %y]
# bind $n <Motion>        [list motion  %W %X %Y]

# #Sets index of tab clicked.
# proc click   {W x y} {
#     variable src_index [$W index @$x,$y]
#     puts stderr "Clicked $src_index"
# }

# #Moves the tab to the position where it was dropped.
# proc release {W x y} {
#     variable src_index
#     variable dst_index
#     puts stderr "Released $src_index"
#     #Check for a valid source
#     if {[string is int -strict $src_index]} {
#         set dst_index [$W index @$x,$y]
#         #Check for a valid destination
#         if {[string is int -strict $dst_index]} {
#             set tab [lindex [$W tabs] $src_index]
#             $W insert $dst_index $tab
#             puts stderr "Insert $tab @ $dst_index"
#         }
#     }
# }

# #Passes mouse motion events to underlying widgets while dragging.
# #Allows the notebook tabs to highlight on mouse-over.
# proc motion  {W X Y} {
#     set w [winfo containing $X $Y]
#     if {$w ne $W && $w ne ""} {
#         set x [expr {$X - [winfo rootx $w]}]
#         set y [expr {$Y - [winfo rooty $w]}]
#         event generate $w <Motion> -x $x -y $y
#     }
# }
# """)
# window.mainloop()

# import tkinter as tk

# root = tk.Tk()

# textbox = tk.Text(root, width=30, height=10, font=('Courier New bold',12), spacing1=1)
# textbox.pack()

# # config a tag with error.xbm as bgstipple in red color
# biterror = tk.BitmapImage(file="error.xbm")
# textbox.tag_config("squiggly", bgstipple="@error.xbm", background='red')
# textbox.insert("end", "hello", "squiggly") # add squiggly line
# textbox.insert("end", " world! ")
# textbox.insert("end", "Python", "squiggly") # add squiggly line
# textbox.insert("end", "\nthis is second line")

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.title('Main')
# root.geometry('200x100')

# def close_all(master):
#     for child in master.winfo_children():
#         str_child = str(child)
#         if str_child.__contains__(".!toplevel"):
#         # if isinstance(child, tk.Toplevel):
#             child.destroy()  # Call method.

# button = tk.Button(root, text=f"Close Toplevels",
#                    command=lambda master=root: close_all(master))
# button.pack()

# for i in reversed(range(4)):  # Create them bottom to top.
#     toplevel = tk.Toplevel()
#     toplevel.title(f'Toplevel {i+1}')
#     toplevel.geometry('200x75')
#     toplevel.lift()

#     button = tk.Button(toplevel, text="Close me", command=toplevel.destroy)
#     button.pack()

# def add_toplevel():
#     toplevel = tk.Toplevel()
#     toplevel.title(f'Toplevel {len(root.winfo_children())}')
#     toplevel.geometry('200x75')
#     toplevel.lift()

#     button = tk.Button(toplevel, text="Close me", command=toplevel.destroy)
#     button.pack()

# button1 = tk.Button(root, text="Add Toplevel", command=add_toplevel)
# button1.pack()

# root.mainloop()


# from tkinter.simpledialog import askstring
# name = askstring('Name', 'What is your name?')

# import tkinter as tk

# class TextLineNumbers(tk.Canvas):
#     def __init__(self, *args, **kwargs):
#         tk.Canvas.__init__(self, *args, **kwargs)
#         self.textwidget = None

#     def attach(self, text_widget):
#         self.textwidget = text_widget
        
#     def redraw(self, *args):
#         '''redraw line numbers'''
#         self.delete("all")

#         i = self.textwidget.index("@0,0")
#         while True :
#             dline= self.textwidget.dlineinfo(i)
#             if dline is None: break
#             y = dline[1]
#             linenum = str(i).split(".")[0]
#             self.create_text(2,y,anchor="nw", text=linenum)
#             i = self.textwidget.index("%s+1line" % i)

# class CustomText(tk.Text):
#     def __init__(self, *args, **kwargs):
#         tk.Text.__init__(self, *args, **kwargs)

#         # create a proxy for the underlying widget
#         self._orig = self._w + "_orig"
#         self.tk.call("rename", self._w, self._orig)
#         self.tk.createcommand(self._w, self._proxy)

#     def _proxy(self, *args):
#         # let the actual widget perform the requested action
#         cmd = (self._orig,) + args
#         result = self.tk.call(cmd)

#         # generate an event if something was added or deleted,
#         # or the cursor position changed
#         if (args[0] in ("insert", "replace", "delete") or 
#             args[0:3] == ("mark", "set", "insert") or
#             args[0:2] == ("xview", "moveto") or
#             args[0:2] == ("xview", "scroll") or
#             args[0:2] == ("yview", "moveto") or
#             args[0:2] == ("yview", "scroll")
#         ):
#             self.event_generate("<<Change>>", when="tail")

#         # return what the actual widget returned
#         return result        

# class Example(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         self.text = CustomText(self)
#         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
#         self.text.configure(yscrollcommand=self.vsb.set)
#         self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
#         self.linenumbers = TextLineNumbers(self, width=30)
#         self.linenumbers.attach(self.text)

#         self.vsb.pack(side="right", fill="y")
#         self.linenumbers.pack(side="left", fill="y")
#         self.text.pack(side="right", fill="both", expand=True)

#         self.text.bind("<<Change>>", self._on_change)
#         self.text.bind("<Configure>", self._on_change)

#         self.text.insert("end", "one\ntwo\nthree\n")
#         self.text.insert("end", "four\n",("bigfont",))
#         self.text.insert("end", "five\n")
#         self.text.insert("end", "\n"*10000)

#     def _on_change(self, event):
#         self.linenumbers.redraw()

# if __name__ == "__main__":
#     root = tk.Tk()
#     Example(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()


# import tkinter # Tkinter -> tkinter in Python 3

# class FancyListbox(tkinter.Listbox):

#     def __init__(self, parent, *args, **kwargs):
#         tkinter.Listbox.__init__(self, parent, *args, **kwargs)

#         self.popup_menu = tkinter.Menu(self, tearoff=0)
#         self.popup_menu.add_command(label="Delete",
#                                     command=self.delete_selected)
#         self.popup_menu.add_command(label="Select All",
#                                     command=self.select_all)

#         self.bind("<Button-2>", self.popup) # Button-2 on Aqua

#     def popup(self, event):
#         try:
#             self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
#         finally:
#             self.popup_menu.grab_release()

#     def delete_selected(self):
#         for i in self.curselection()[::-1]:
#             self.delete(i)

#     def select_all(self):
#         self.selection_set(0, 'end')


# root = tkinter.Tk()
# flb = FancyListbox(root, selectmode='multiple')
# for n in range(10):
#     flb.insert('end', n)
# flb.pack()
# root.mainloop()



# import tkinter as tk

# # This is a scrollable text widget
# class ScrollText(tk.Frame):
#     def __init__(self, master, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         self.text = tk.Text(self, bg='#2b2b2b', foreground="#d1dce8", 
#                             insertbackground='white',
#                             selectbackground="blue", width=120, height=30)

#         self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
#         self.text.configure(yscrollcommand=self.scrollbar.set)

#         self.numberLines = TextLineNumbers(self, width=40, bg='#313335')
#         self.numberLines.attach(self.text)

#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
#         self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#         self.text.bind("<Key>", self.onPressDelay)
#         self.text.bind("<Button-1>", self.numberLines.redraw)
#         self.scrollbar.bind("<Button-1>", self.onScrollPress)
#         self.text.bind("<MouseWheel>", self.onPressDelay)

#     def onScrollPress(self, *args):
#         self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

#     def onScrollRelease(self, *args):
#         self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

#     def onPressDelay(self, *args):
#         self.after(2, self.numberLines.redraw)

#     def get(self, *args, **kwargs):
#         return self.text.get(*args, **kwargs)

#     def insert(self, *args, **kwargs):
#         return self.text.insert(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         return self.text.delete(*args, **kwargs)

#     def index(self, *args, **kwargs):
#         return self.text.index(*args, **kwargs)

#     def redraw(self):
#         self.numberLines.redraw()


# '''THIS CODE IS CREDIT OF Bryan Oakley (With minor visual modifications on my side): 
# https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget'''


# class TextLineNumbers(tk.Canvas):
#     def __init__(self, *args, **kwargs):
#         tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
#         self.textwidget = None

#     def attach(self, text_widget):
#         self.textwidget = text_widget

#     def redraw(self, *args):
#         '''redraw line numbers'''
#         self.delete("all")

#         i = self.textwidget.index("@0,0")
#         while True :
#             dline= self.textwidget.dlineinfo(i)
#             if dline is None: break
#             y = dline[1]
#             linenum = str(i).split(".")[0]
#             self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
#             i = self.textwidget.index("%s+1line" % i)


# '''END OF Bryan Oakley's CODE'''

# if __name__ == '__main__':
#     root = tk.Tk()
#     scroll = ScrollText(root)
#     scroll.insert(tk.END, "HEY" + 20*'\n')
#     scroll.pack()
#     scroll.text.focus()
#     scroll.redraw()
#     root.mainloop()





# from github import Github

# def print_repo(repo):
#     # repository full name
#     print("Full name:", repo.full_name)
#     # repository description
#     print("Description:", repo.description)
#     # the date of when the repo was created
#     print("Date created:", repo.created_at)
#     # the date of the last git push
#     print("Date of last push:", repo.pushed_at)
#     # home website (if available)
#     print("Home Page:", repo.homepage)
#     # programming language
#     print("Language:", repo.language)
#     # number of forks
#     print("Number of forks:", repo.forks)
#     # number of stars
#     print("Number of stars:", repo.stargazers_count)
#     print("-"*50)
#     # repository content (files & directories)
#     print("Contents:")
#     for content in repo.get_contents(""):
#         print(content)

# username = "Moosems"
# password = "Windermere8154"

# # authenticate to github
# g = Github(username, password)
# # get the authenticated user
# user = g.get_user()

# repo = g.search_repositories("JDE")[0]

# # create a file and commit n push
# repo.create_file("test.txt", "commit message", "content of the file")

# # delete that created file
# contents = repo.get_contents("test.txt")
# repo.delete_file(contents.path, "remove test.txt", contents.sha)




# from tkinter import *

# def donothing():
#    filewin = Toplevel(root)
#    button = Button(filewin, text="Do nothing button")
#    button.pack()
   
# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)

# filemenu.add_separator()

# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)

# editmenu.add_separator()

# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)

# menubar.add_cascade(label="Edit", menu=editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)

# root.config(menu=menubar)
# root.mainloop()


# from tkinter import *
# root = Tk()
# menu = Menu(root)
# for i in ('One', 'Two', 'Three'):
#     menu.add_command(label=i)
# if (root.tk.call('tk', 'windowingsystem')=='aqua'):
#     root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
#     root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
# else:
#     root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
# root.mainloop()