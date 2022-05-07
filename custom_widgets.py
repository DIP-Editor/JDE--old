from tkinter import *
from tkinter.filedialog import *
from tkinter import colorchooser
from tkinter.font import Font
from tkinter.messagebox import *
import os
# from pygments import *
# from pygments.formatters import *
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from idlelib.autocomplete import AutoComplete
import idlelib.colorizer as ic
import idlelib.percolator as ip
import smtplib
import re
from os import listdir
import sys
from pathlib import Path
if getattr(sys, "frozen", False):
    folder = Path(sys._MEIPASS)
else:
    folder = Path(__file__).parent

with open(folder / "keywords.txt", "r") as f:
    keywords_list = f.read().splitlines()
# keywords_list = ["from", "tkinter", "i", "import", "Tk", "winfo_screenwidth", "winfo_screenheight", "relx", "rely", "anchor", "CENTER", "mainloop", "geometry",  "Label", "Button", "Text", "Entry", "pack", "place", "grid", "False", "await", "else", "pass", "None", "break", "except", "in", "range", "raise", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "nonlocal", "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield", "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", "callable", "chr", "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate", "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list", "locals", "map", "max", "memoryview", "min", "next", "object", "oct", "open", "ord", "pow", "print", "property", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", "type", "vars", "zip", "breakpoint"]

def update_list():
    with open("keywords.txt", "r+") as f:
        f.truncate()
        f.seek(0)
        f.truncate()
        f.seek(0)
        for item in keywords_list:
            f.write(item + "\n")

class ToolTip(Frame):
    def __init__(self, master, *args, **kwargs):
        self.window = kwargs.pop("window")
        self.tooltip_text = kwargs.pop("text")
        Frame.__init__(self, *args, **kwargs)
        self.overall_widget = master
        self.height = int(self.overall_widget.winfo_height())
        self.overall_widget.bind("<Enter>", self.create_label)
        self.overall_widget.bind("<Leave>", self.destroy_label)
        self.overall_widget.bind("<ButtonPress>", self.destroy_label)

    def create_label(self, event):
        self.tooltip = Label(self.window, text=self.tooltip_text, bg="yellow", fg="black", bd=1, relief=SOLID, font=("Courier New bold",15))
        self.tooltip.place(x=self.overall_widget.winfo_x()+self.overall_widget.winfo_width()+5, y=self.overall_widget.winfo_y())
    
    def destroy_label(self, event):
        self.tooltip.destroy()

class ultra_text(Frame):
    def __init__(self, *args, **kwargs):
        self.window = kwargs.pop("window", None)
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
        else:
            bg = "white"
        #Defining colors for basic syntax highlighting
        self.cdg = ic.ColorDelegator()
        self.cdg.prog = re.compile(r"\b(?P<MYGROUP>tkinter)\b|" + ic.make_pat(), re.S)
        self.cdg.idprog = re.compile(r"\s+(\w+)", re.S)
        with open(folder / "settings.txt", "r") as settings:
            settings = settings.read()
        settings = settings.split("\n")
        tag_mygroup = str(settings[0])
        tag_comment = str(settings[1])
        tag_keyword = str(settings[2])
        tag_builtin = str(settings[3])
        tag_string = str(settings[4])
        tag_definition = str(settings[5])
        tag_class = str(settings[6])
        self.cdg.tagdefs["MYGROUP"] = {"foreground": tag_mygroup, "background": bg}
        self.cdg.tagdefs["COMMENT"] = {"foreground": tag_comment, "background":bg}
        self.cdg.tagdefs["KEYWORD"] = {"foreground": tag_keyword, "background": bg}
        self.cdg.tagdefs["BUILTIN"] = {"foreground": tag_builtin, "background": bg}
        self.cdg.tagdefs["STRING"] = {"foreground": tag_string, "background": bg}
        self.cdg.tagdefs["DEFINITION"] = {"foreground": tag_definition, "background": bg}
        self.cdg.tagdefs["CLASS"] = {"foreground": tag_class, "background": bg}

        # IMPORTANT NOTICE! THIS IS THE MAIN TEXT WIDGET. ALL ADDITIONS ARE TO BE ADDED HERE |
        #                                                                                    \/
        if "height" and "width" in kwargs:
            self.text = Text(self, height=kwargs["height"], width=kwargs["width"], borderwidth=2, relief=RIDGE, wrap=NONE, undo=True, font=("Courier New bold", 15))
        else:
            #, width=130, height=29
            self.text = Text(self, font=("Courier New bold", 15), wrap="none", undo=True, borderwidth=2, relief=RIDGE, width=95, height=25)
        ip.Percolator(self.text).insertfilter(self.cdg)

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40)
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.numberLines.pack(side=LEFT, fill=Y, padx=(5, 0))
        self.text.pack(side=RIGHT, fill=BOTH, expand=True)

        # self.window.bind("<KeyRelease>", self.update_location)
        # self.window.bind("<Motion>", self.update_location)
        # self.window.bind("<Button-1>", self.update_location)

        self.window.bind("<Any>", self.redraw())
        self.window.bind("<BackSpace>", lambda x: self.after(10, (self.redraw())), add=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

        self.text.bind("<Any-KeyRelease>", self._autocomplete)

        self.text.bind("<Tab>", self._handle_tab, add=True)

        self.text.bind("\"", self.double_quotes)
        self.text.bind("(", self.double_parentheses)
        self.text.bind(")", self.close_parentheses)
        self.text.bind("<BackSpace>", self.closing_backspace, add=True)
        self.text.bind("<BackSpace>", self.remove_indentation, add=True)
        self.text.bind("{", self.double_curly_braces)
        self.text.bind("}", self.close_curly_braces)
        self.text.bind("[", self.double_square_braces)
        self.text.bind("]", self.close_square_braces)
        self.text.bind("<Command-slash>", self.make_comment)
        self.text.bind("<Shift-Tab>", self.back_tab)
        self.text.bind("<KeyRelease-Return>", lambda x: [self.redraw(), self.new_line_indent(self)], add="+")
        self.text.bind("<Command-Shift-k>", self.delete_line)
        self.text.bind("<Command-b>", self.add_breakpoint)

        font = Font(font=self.text["font"])
        tab_width = font.measure("    ")
        self.text.config(tabs=(tab_width))

    def remove_indentation(self, event=None):
        #Get the current line contents
        current_line_contents = self.text.get("insert linestart", "insert lineend")
        #Get the current position
        current_position = int((self.text.index(INSERT)).split(".")[1])
        # Check if the current line is empty
        if current_line_contents != "":
            #Check if the current line is indented with four spaces
            if "    " in current_line_contents:
                #Check if previous four characters are to the left of the cursor and are spaces
                if current_line_contents[current_position-4:current_position] == "    ":
                    # Remove three spaces from the left of the cursor
                    new_line_contents = current_line_contents[:current_position-3] + current_line_contents[current_position:]
                    self.text.delete("insert linestart", "insert lineend")
                    self.text.insert("insert", new_line_contents)
                    self.text.mark_set("insert", "{}.{}".format(int(self.text.index("insert").split(".")[0]), current_position-3))

    def close_parentheses(self, event):
        try:
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents[current_position] == ")":
                new_line_contents = current_line_contents[:current_position] + current_line_contents[current_position+1:]
                self.text.delete("insert linestart", "insert lineend")
                self.text.insert("insert", new_line_contents)
                self.text.mark_set("insert", pos)
        except:
            pass

    def close_curly_braces(self, event):
        try:
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents[current_position] == "}":
                new_line_contents = current_line_contents[:current_position] + current_line_contents[current_position+1:]
                self.text.delete("insert linestart", "insert lineend")
                self.text.insert("insert", new_line_contents)
                self.text.mark_set("insert", pos)
        except:
            pass

    def close_square_braces(self, event):
        try:
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents[current_position] == "]":
                new_line_contents = current_line_contents[:current_position] + current_line_contents[current_position+1:]
                self.text.delete("insert linestart", "insert lineend")
                self.text.insert("insert", new_line_contents)
                self.text.mark_set("insert", pos)
        except:
            pass

    def closing_backspace(self, event):
        try:
            # global insert_char
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents != "":
                if current_line_contents[current_position-1] == "(" or "{" or "[" or "\"":
                    special_char = current_line_contents[current_position-1]
                    if special_char == "(":
                        insert_char = ")"
                    elif special_char == "{":
                        insert_char = "}"
                    elif special_char == "[":
                        insert_char = "]"
                    elif special_char == "\"":
                        insert_char = "\""
                    #Remove previous char to the left and add a closing parenthesis if it is to the right
                    new_line_contents = current_line_contents[:current_position-1] + insert_char + current_line_contents[current_position:]
                    if new_line_contents[current_position] == insert_char:
                        new_line_contents = new_line_contents[:current_position] + new_line_contents[current_position+1:]
                    self.text.delete("insert linestart", "insert lineend")
                    self.text.insert("insert", new_line_contents)
                    self.text.mark_set("insert", pos)
        except:
            pass

    def add_breakpoint(self, event=None):
        current_position = self.text.index(INSERT)
        current_line = current_position.split(".")[0]
        current_line_contents = self.text.get("insert linestart", "insert lineend")
        self.text.insert("{}.end".format(current_line), "\nbreakpoint()")
        if current_line_contents != "":
            if current_line_contents[0] != "#":
                if "    " not in current_line_contents:
                    for i in range(current_line_contents.count("\t")):
                        self.text.insert("{}.0".format(int(current_line)+1), "\t")
                    if current_line_contents[-1] == ":":
                        self.text.insert("{}.0".format(int(current_line)+1), "\t")
                else:
                    for i in range(current_line_contents.count("    ")):
                        self.text.insert("{}.0".format(int(current_line)+1), "    ")
                    if current_line_contents[-1] == ":":
                        self.text.insert("{}.0".format(int(current_line)+1), "    ")
        self.redraw()

    def delete_line(self, event=None):
        try:
            first_line = int(self.text.index("sel.first").split(".")[0])
            last_line = int(self.text.index("sel.last").split(".")[0])
            for line in range(first_line, last_line+1):
                if line != 1:
                    self.text.delete("{}.0 - 1 chars".format(line), "{}.end".format(line))
                    self.redraw()
                else:
                    self.text.delete("{}.0".format(line), "{}.end + 1 chars".format(line))
                    self.redraw()
        except:
            # if self.text.get("1.0", "end") != "":
            self.text.delete("insert linestart", "insert lineend")
            if self.text.index("insert") != "1.0":
                self.text.delete("insert -1 chars", "insert")
                self.redraw()
            else:
                self.text.delete("insert", "insert +1 chars")
                self.redraw()

    def tabs_to_spaces(self, event=None):
        while "\t" in self.text.get(1.0, END):
            new_contents = self.text.get(1.0, END).replace("\t", "    ")
            self.text.delete(1.0, END)
            self.text.insert(1.0, new_contents)
            self.text.mark_set(INSERT, INSERT)
    
    def spaces_to_tabs(self, event=None):
        while "    " in self.text.get(1.0, END):
            new_contents = self.text.get(1.0, END).replace("    ", "\t")
            self.text.delete(1.0, END)
            self.text.insert(1.0, new_contents)
            self.text.mark_set(INSERT, INSERT)

# #Place tag_config here

    def change_color(self, new_color):
        if new_color == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.config(background=bg)
        self.text.config(bg=bg, fg=fg, insertbackground=fg)
        self.numberLines.config(bg=bg)

    def reset_syntax(self, event=None, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        
        self.text.ResetColorizer()
        self.cdg.prog = re.compile(r"\b(?P<MYGROUP>tkinter)\b|" + ic.make_pat(), re.S)
        self.cdg.idprog = re.compile(r"\s+(\w+)", re.S)
        with open(folder / "settings.txt", "r") as settings:
            settings = settings.read()
        settings = settings.split("\n")
        tag_mygroup = str(settings[0])
        tag_comment = str(settings[1])
        tag_keyword = str(settings[2])
        tag_builtin = str(settings[3])
        tag_string = str(settings[4])
        tag_definition = str(settings[5])
        tag_class = str(settings[6])
        #, "background": bg
        self.cdg.tagdefs["MYGROUP"] = {"foreground": tag_mygroup, "background": bg}
        self.cdg.tagdefs["COMMENT"] = {"foreground": tag_comment, "background": bg}
        self.cdg.tagdefs["KEYWORD"] = {"foreground": tag_keyword, "background": bg}
        self.cdg.tagdefs["BUILTIN"] = {"foreground": tag_builtin, "background": bg}
        self.cdg.tagdefs["STRING"] = {"foreground": tag_string, "background": bg}
        self.cdg.tagdefs["DEFINITION"] = {"foreground": tag_definition, "background": bg}
        self.cdg.tagdefs["CLASS"] = {"foreground": tag_class, "background": bg}
        ip.Percolator(self.text).insertfilter(self.cdg)

    def callback(self, word):
        #Returns possible matches
        #words is a list of almost every keyword and builtin function
        words = keywords_list
        matches = [x for x in words if x.startswith(word)]
        return matches

    def _handle_tab(self, event):
        tag_ranges= self.text.tag_ranges("autocomplete")
        if tag_ranges:
            self.text.mark_set("insert", tag_ranges[1])
            self.text.tag_remove("sel", "1.0", "end")
            self.text.tag_remove("autocomplete", "1.0", "end")
            return "break"
        else:
            self.text.insert(INSERT, "    ")
            return "break"

    def _autocomplete(self, event):
        if event.char and self.callback and event.keysym != "BackSpace":
            word = self.text.get("insert-1c wordstart", "insert-1c wordend")
            matches = self.callback(word)
            if matches:
                remainder = matches[0][len(word):]
                insert = self.text.index("insert")
                self.text.insert(insert, remainder, ("sel", "autocomplete"))
                self.text.mark_set("insert", insert)

    def make_find_and_replace(self, event=None, **kwargs):
        color_mode = kwargs.pop("color_mode")
        self.search_bar = search_text(self, color_mode = color_mode)
        self.search_bar.attach(self.text)
        self.search_bar.focus_set()

    def open_template(self, event=None, **kwargs):
        color_mode = kwargs.pop("color_mode")
        self.open_template = temp_open_pop_up(self, text=self.text, color_mode=color_mode)
        # self.open_template.attach(self.text)

    def double_parentheses(self, event):
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, ")")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def double_curly_braces(self, event):
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "}")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def double_square_braces(self, event):
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "]")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def back_tab(self, event):
        try:
            first_line = int(self.text.index("sel.first").split(".")[0])
            last_line = int(self.text.index("sel.last").split(".")[0])
            for line in range(first_line, last_line+1):
                editable_line = self.text.get("{}.0".format(line), "{}.end".format(line))
                if "\t" in editable_line:
                    location_of_tab = editable_line.find("\t")
                    editable_line = editable_line[:location_of_tab] + editable_line[location_of_tab+1:]
                    self.text.delete("{}.0".format(line), "{}.end".format(line))
                    self.text.insert("{}.0".format(line), editable_line)
                elif "    " in editable_line:
                    location_of_tab = editable_line.find("    ")
                    editable_line = editable_line[:location_of_tab] + editable_line[location_of_tab+4:]
                    self.text.delete("{}.0".format(line), "{}.end".format(line))
                    self.text.insert("{}.0".format(line), editable_line)
        except:
            line = self.text.get("insert linestart", "insert lineend")
            editable_line = str(line)
            if editable_line != "":
                if "\t" in editable_line:
                    location_of_tab = editable_line.find("\t")
                    editable_line = editable_line[:location_of_tab] + editable_line[location_of_tab + 1:]
                    self.text.delete("insert linestart", "insert lineend")
                    self.text.insert("insert linestart", editable_line)
                elif "    " in editable_line:
                    location_of_tab = editable_line.find("    ")
                    editable_line = editable_line[:location_of_tab] + editable_line[location_of_tab + 4:]
                    self.text.delete("insert linestart", "insert lineend")
                    self.text.insert("insert linestart", editable_line)
        # return "break"
    
    def make_comment(self, event):
        try:
            first_line = int(self.text.index("sel.first").split(".")[0])
            last_line = int(self.text.index("sel.last").split(".")[0])
            for line in range(first_line, last_line+1):
                if line <= int(self.text.get("1.0", "end").count("\n")):
                    if self.text.get("{}.0".format(line), "{}.1".format(line)) != "#":
                        self.text.insert("{}.0".format(line), "#")
                    else:
                        self.text.delete("{}.0".format(line), "{}.1".format(line))
        except:
            self_anchor = (str(self.text.index("insert")).split("."))[0]
            if self.text.get(self_anchor + ".0", self_anchor + ".1") != "#":
                self.text.insert(float("{}.0".format(self_anchor)), "#")
            else:
                self.text.delete(self_anchor + ".0", self_anchor + ".1")

    def double_quotes(self, event):
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "\"")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def new_line_indent(self, event=None):
        line = self.text.get("insert-1c linestart", "insert-1c lineend")
        editable_line = str(line)
        if editable_line != "":
            if line[0] != "#":
                if "    " in editable_line:
                    #Get the tab count
                    tab_count = editable_line.count("    ")
                    space_count = tab_count * 4
                    # Check that the first space_count characters are spaces
                    if editable_line[:space_count] == " " * space_count:
                        for i in range(editable_line.count("    ")):
                            self.text.insert("insert", "    ")
                    else:
                        locations = [m.start() for m in re.finditer("    ", editable_line)]
                        if locations[0] == 0:
                            for i in range(tab_count):
                                #Get distance from this location to last location
                                distance = locations[i+1] - locations[i]
                                if distance > 4:
                                    tab_count = i+1
                                    break
                            for i in range(tab_count):
                                self.text.insert("insert", "    ")
                if editable_line[-1] == ":":
                    self.text.insert("insert", "    ")

    def get_text(self):
        return self.text.get("1.0", "end")

    def return_anchor(self, event):
        return self.text.index("insert")
    
    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()

class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, font=("Courier New bold", 15), fill="#2197db") #606366 #90a395 #808090 #14a83c #2893d1 #2197db
            i = self.textwidget.index("%s+1line" % i)

class search_text(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.search_text_window = Toplevel(self)
        self.search_text_window.title("Search / Find and Replace")
        self.search_text_window.config(bg=bg)
        self.search_text_window.geometry("+0+0")
        self.search_text_window.attributes("-topmost", True)
        self.text_search_entry = Entry(self.search_text_window, borderwidth=3, font=("Courier New bold", 15))
        self.search_button = Button(self.search_text_window, text="Search File", font=("Courier New bold", 15), command=self.find)
        self.text_replace_entry = Entry(self.search_text_window, borderwidth=3, font=("Courier New bold", 15))
        self.replace_button = Button(self.search_text_window, text="Replace", font=("Courier New bold", 15), command=self.find_and_replace)
        self.skip_match = Button(self.search_text_window, text="Skip Match", font=("Courier New bold", 15), command=self.skip_match)
        self.search_list = list()
        self.s = ""
        self.text_search_entry.pack(side=LEFT, fill=BOTH, expand=1)
        self.search_button.pack(side=LEFT)
        self.text_replace_entry.pack(side=LEFT, fill=BOTH, expand=1)
        self.replace_button.pack(side=LEFT)
        self.skip_match.pack(side=LEFT)
        self.text_search_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.text_replace_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.search_button.configure(highlightbackground=bg)
        self.replace_button.configure(highlightbackground=bg)
        self.skip_match.configure(highlightbackground=bg)

    def attach(self, text):
        self.text = text

    def reset_list(self):
        if self.s != self.text_search_entry.get():
            self.search_list.clear()
            self.text.tag_remove(SEL, 1.0,"end-1c")
        
    def find(self):
        self.reset_list()
        self.text.focus_set()
        self.s = self.text_search_entry.get()

        if self.s:
            if self.search_list == []:
                idx = "1.0"
            else:
                idx = self.search_list[-1]

            idx = self.text.search(self.s, idx, nocase=1, stopindex=END)
            lastidx = "%s+%dc" % (idx, len(self.s))

            try:
                self.text.tag_remove(SEL, 1.0,lastidx)
            except:
                pass

            try:
                self.text.tag_add(SEL, idx, lastidx)
                counter_list = []
                counter_list = str(idx).split(".")      
                self.text.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
                self.text.see(float(int(counter_list[0])))
                self.search_list.append(lastidx)
            except:
                showinfo("Search Complete","Search Completed\n\nThere Are No Further Matches")
                self.search_list.clear()
                self.text.tag_remove(SEL, 1.0,"end-1c")
    def skip_match(self):
        self.find()
    def find_and_replace(self):
        #Replaces the match in the text box with the text in the replace box
        self.reset_list()
        self.text.focus_set()
        self.s = self.text_search_entry.get()
        self.r = self.text_replace_entry.get()
        new_line = ""
        if self.s:
            line = self.text.get("insert linestart", "insert lineend")
            editable_line = str(line)
            if self.search_list == []:
                idx = "1.0"
            else:
                idx = self.search_list[-1]
            location_of_match = idx.split(".")[1]
            location_of_match = location_of_match.split("c")[0]
            location_of_match = location_of_match.split("+")[0]
            length_of_match = len(str(self.s))

            new_line = editable_line[:int(location_of_match)] + self.r + editable_line[int(location_of_match)+length_of_match:]
            self.text.delete("insert linestart", "insert lineend")
            self.text.insert("insert linestart", new_line)
            self.text.see("insert")
            self.text.tag_remove(SEL, 1.0,"end-1c")
            self.text.tag_add(SEL, "insert linestart", "insert lineend")
            self.text.focus_set()
            self.text.mark_set("insert", "insert linestart")
            self.reset_list()

class temp_name_pop_up:
    def __init__(self, text_info, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.text_info = text_info.get("1.0", END)
        self.pop_up_window = Toplevel()
        self.pop_up_window.title("Template Name")
        self.pop_up_window.config(bg=bg)
        self.pop_up_window.geometry("300x100+0+0")
        self.pop_up_window.resizable(width=False, height=False)
        self.pop_up_window.focus_force()
        self.pop_up_name_label = Label(self.pop_up_window, text="Template Name:", font=("Courier New bold", 15))
        self.pop_up_name_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.pop_up_name_label.configure(bg=bg, fg=fg)
        self.pop_up_name_entry = Entry(self.pop_up_window, font=("Courier New bold", 15))
        self.pop_up_name_entry.place(relx=.5, rely=.4, anchor=CENTER)
        self.pop_up_name_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.pop_up_name_entry.focus_force()
        self.confirm_button = Button(self.pop_up_window, text="Confirm", font=("Courier New bold", 15), command=self.confirm)
        self.confirm_button.place(relx=.125, rely=.85, anchor=CENTER)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.pop_up_window, text="Cancel", font=("Courier New bold", 15), command=self.cancel)
        self.cancel_button.place(relx=.875, rely=.85, anchor=CENTER)
        self.cancel_button.configure(highlightbackground=bg)

    def confirm(self):
        temp_name = self.pop_up_name_entry.get()
        if (folder / "{}.py".format(temp_name)).exists():
            showinfo("Template Name Error", "Template Name Already Exists")
            self.pop_up_window.destroy()
        else:
            if (temp_name != "") and (temp_name != " "):
                with open(folder / "{}.py".format(temp_name), "w") as f:
                    f.write(self.text_info)
                    f.close()
                self.pop_up_window.destroy()
                showinfo("Template Created", "Template Created\n\nTemplate has been created")
            else:
                showerror("Template Name Error", "Template Name Cannot be Blank")
                self.pop_up_window.destroy()

    def cancel(self):
        global temp_name
        temp_name = None
        self.pop_up_window.destroy()

class temp_open_pop_up(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        self.text = kwargs.pop("text")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.temp_open_pop_up_window = Toplevel()
        self.temp_open_pop_up_window.title("Template Selection")
        self.temp_open_pop_up_window.config(bg=bg)
        self.temp_open_pop_up_window.geometry("400x300+0+0")
        self.temp_open_pop_up_window.resizable(width=False, height=False)
        self.temp_open_pop_up_window.attributes("-topmost", True)
        self.templates_start_list = listdir(folder)
        self.templates_list = []
        for file in self.templates_start_list:
            if file.endswith(".py"):
                self.templates_list.append(file)
        self.templates_list.sort()
        self.temp_open_pop_up_label = Label(self.temp_open_pop_up_window, text="Select a template:", font=("Courier New bold", 20))
        self.temp_open_pop_up_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.temp_open_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_open_pop_up_listbox = Listbox(self.temp_open_pop_up_window, width=30, height=10)
        self.temp_open_pop_up_listbox.place(relx=.5, rely=.5, anchor=CENTER)
        self.temp_open_pop_up_listbox.configure(selectbackground=bg, selectforeground=fg)
        for item in self.templates_list:
            item = item.split(".py")[0]
            self.temp_open_pop_up_listbox.insert(END, item)
        self.confirm_button = Button(self.temp_open_pop_up_window, text="Confirm", font=("Courier New bold", 15), command=self.confirm)
        self.confirm_button.place(relx=.1, rely=.95, anchor=CENTER)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.temp_open_pop_up_window, text="Cancel", font=("Courier New bold", 15), command=self.cancel)
        self.cancel_button.place(relx=.9, rely=.95, anchor=CENTER)
        self.cancel_button.configure(highlightbackground=bg)
        self.temp_open_pop_up_window.mainloop()

    def attach(self, text):
        self.text = text

    def confirm(self):
        self.file_chosen = self.temp_open_pop_up_listbox.get(ANCHOR) + ".py"
        if self.file_chosen != ".py":
            self.text.delete(1.0, END)
            with open(folder / self.file_chosen, "r") as f:
                self.text.insert(END, f.read())
                f.close()
            self.temp_open_pop_up_window.destroy()
        else:
            showerror("Template Error", "Template Could Not Be Opened\n\nNo Template Selected")
            self.temp_open_pop_up_window.destroy()

    def cancel(self):
        self.temp_open_pop_up_window.destroy()

class temp_destroy_pop_up:
    def __init__(self, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.temp_destroy_pop_up_window = Toplevel()
        self.temp_destroy_pop_up_window.title("Template Selection")
        self.temp_destroy_pop_up_window.config(bg=bg)
        self.temp_destroy_pop_up_window.geometry("400x300+0+0")
        self.temp_destroy_pop_up_window.resizable(width=False, height=False)
        self.temp_destroy_pop_up_window.focus_force()
        self.templates_start_list = listdir(folder)
        self.templates_list = []
        for file in self.templates_start_list:
            if file.endswith(".py"):
                self.templates_list.append(file)
        self.templates_list.sort()
        self.temp_destroy_pop_up_label = Label(self.temp_destroy_pop_up_window, text="Select a template:", font=("Courier New bold", 20))
        self.temp_destroy_pop_up_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.temp_destroy_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_destroy_pop_up_listbox = Listbox(self.temp_destroy_pop_up_window, width=30, height=10)
        self.temp_destroy_pop_up_listbox.place(relx=.5, rely=.5, anchor=CENTER)
        self.temp_destroy_pop_up_listbox.configure(selectbackground=bg, selectforeground=fg)
        for item in self.templates_list:
            item = item.split(".py")[0]
            self.temp_destroy_pop_up_listbox.insert(END, item)
        self.confirm_button = Button(self.temp_destroy_pop_up_window, text="Confirm", font=("Courier New bold", 15), command=self.confirm)
        self.confirm_button.place(relx=.1, rely=.95, anchor=CENTER)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.temp_destroy_pop_up_window, text="Cancel", font=("Courier New bold", 15), command=self.cancel)
        self.cancel_button.place(relx=.9, rely=.95, anchor=CENTER)
        self.cancel_button.configure(highlightbackground=bg)

    def confirm(self):
        self.file_chosen = self.temp_destroy_pop_up_listbox.get(ANCHOR) + ".py"
        if self.file_chosen != ".py":
            os.remove(folder / self.file_chosen)
            self.temp_destroy_pop_up_window.destroy()
            showinfo("Template Deleted", "Template Deleted\n\nTemplate Has Been Beleted")
        else:
            showerror("Template Error", "Template Could Not Be Deleted\n\nNo Template Selected")
            self.temp_destroy_pop_up_window.destroy()

    def cancel(self):
        self.temp_destroy_pop_up_window.destroy()

class settings(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        self.settings_window = Toplevel()
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.settings_window.configure(background=bg)
        self.settings_window.title("Settings")
        self.settings_window.geometry("375x450+0+0")
        self.settings_window.resizable(width=False, height=False)
        self.settings_window.attributes("-topmost", True)
        self.settings_window.focus_force()
        self.settings_window_main_label = Label(self.settings_window, text="Settings", font=("Courier New bold", 35))
        self.settings_window_main_label.place(relx=.5, rely=.075, anchor=CENTER)
        self.settings_window_main_label.configure(bg=bg, fg=fg)
        # tag_mygroup
        # tag_comment 
        # tag_keyword 
        # tag_builtin 
        # tag_string
        # tag_definition
        # tag_class
        self.my_group_color_changer_button = Button(self.settings_window, text="MYGROUP Color Picker", font=("Courier New bold", 20), width=22, command=self.my_group_color_changer)
        self.my_group_color_changer_button.place(relx=.5, rely=.15, anchor=CENTER)
        self.my_group_color_changer_button.configure(highlightbackground=bg)
        self.comment_color_changer_button = Button(self.settings_window, text="COMMENT Color Picker", font=("Courier New bold", 20), width=22, command=self.comment_color_changer)
        self.comment_color_changer_button.place(relx=.5, rely=.23055, anchor=CENTER)
        self.comment_color_changer_button.configure(highlightbackground=bg)
        self.keyword_color_changer_button = Button(self.settings_window, text="KEYWORD Color Picker", font=("Courier New bold", 20), width=22, command=self.keyword_color_changer)
        self.keyword_color_changer_button.place(relx=.5, rely=.3111, anchor=CENTER)
        self.keyword_color_changer_button.configure(highlightbackground=bg)
        self.builtin_color_changer_button = Button(self.settings_window, text="BUILTIN Color Picker", font=("Courier New bold", 20), width=22, command=self.builtin_color_changer)
        self.builtin_color_changer_button.place(relx=.5, rely=.39165, anchor=CENTER)
        self.builtin_color_changer_button.configure(highlightbackground=bg)
        self.string_color_changer_button = Button(self.settings_window, text="STRING Color Picker", font=("Courier New bold", 20), width=22, command=self.string_color_changer)
        self.string_color_changer_button.place(relx=.5, rely=.4722, anchor=CENTER)
        self.string_color_changer_button.configure(highlightbackground=bg)
        self.definition_color_changer_button = Button(self.settings_window, text="DEFINITION Color Picker", font=("Courier New bold", 20), width=22, command=self.definition_color_changer)
        self.definition_color_changer_button.place(relx=.5, rely=.55275, anchor=CENTER)
        self.definition_color_changer_button.configure(highlightbackground=bg)
        self.class_color_changer_button = Button(self.settings_window, text="CLASS Color Picker", font=("Courier New bold", 20), width=22, command=self.class_color_changer)
        self.class_color_changer_button.place(relx=.5, rely=.6333, anchor=CENTER)
        self.class_color_changer_button.configure(highlightbackground=bg)
        self.keyword_changer_button = Button(self.settings_window, text="Keyword Changer", font=("Courier New bold", 20), width=22, command=self.keyword_changer)
        self.keyword_changer_button.place(relx=.5, rely=.71385, anchor=CENTER)
        self.keyword_changer_button.configure(highlightbackground=bg)
        #import keywords.txt button
        #export keywords.txt button
        import_keywords_button = Button(self.settings_window, text="Import Keywords", font=("Courier New bold", 20), width=22, command=self.import_keywords)
        import_keywords_button.place(relx=.5, rely=.7944, anchor=CENTER)
        import_keywords_button.configure(highlightbackground=bg)
        export_keywords_button = Button(self.settings_window, text="Export Keywords", font=("Courier New bold", 20), width=22, command=self.export_keywords)
        export_keywords_button.place(relx=.5, rely=.87495, anchor=CENTER)
        export_keywords_button.configure(highlightbackground=bg)
        self.quit_button = Button(self.settings_window, text="Quit", font=("Courier New bold", 15), command=self.quit)
        self.quit_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.quit_button.configure(highlightbackground=bg)

    def import_keywords(self):
        global keywords_list
        #Get the file path
        file_path = askopenfilename(initialdir="/", title="Select file", filetypes=([("Text files", "*.txt")]))
        #Check that the file path is not empty and the name is keywords.txt
        if file_path != "" and file_path.endswith("keywords.txt"):
            #update the keywords list
            keywords_list = []
            #open the file
            with open(file_path, "r") as file:
                #read the file
                keywords_list = file.readlines()
            #remove the newline characters
            keywords_list = [keyword.replace("\n", "") for keyword in keywords_list]
            #update the keywords list
            update_list()

    def export_keywords(self):
        file_path = asksaveasfilename(initialdir="/", title="Select file", filetypes=([("Text files", "*.txt")]))
        if file_path != "":
            #open the file
            with open(file_path, "w") as file:
                #write the keywords to the file
                for keyword in keywords_list:
                    file.write(keyword + "\n")

    def color_changer(self, index):
        color = colorchooser.askcolor(title="Choose color")
        if color[1] != None:
            hex = (str(color).split(",")[3].split("'")[1])
            with open(folder / "settings.txt", "r+") as settings:
                settings_info = settings.readlines()
            settings_info[index] = hex  + "\n"
            with open(folder / "settings.txt", "r+") as settings:
                settings.truncate()
                settings.seek(0)
                settings.truncate()
                settings.seek(0)
                settings.writelines(settings_info)
            showinfo("Color Not Changed", "Color Has Not Been Changed Yet\n\nFor Syntax Colors To Change JDE Must Be Closed and Then Re-Opened Or The Reset-Syntax Button Must Be Pressed")

    def my_group_color_changer(self):
        self.color_changer(0)

    def comment_color_changer(self):
        self.color_changer(1)

    def keyword_color_changer(self):
        self.color_changer(2)

    def builtin_color_changer(self):
        self.color_changer(3)

    def string_color_changer(self):
        self.color_changer(4)

    def definition_color_changer(self):
        self.color_changer(5)

    def class_color_changer(self):
        self.color_changer(6)

    def quit(self):
        self.settings_window.destroy()

    def keyword_changer(self):
        keyword_change_page(color_mode = self.color_mode)

class report_bug(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.report_bug_window = Toplevel()
        self.report_bug_window.configure(background=bg)
        self.report_bug_window.title("Report Bug")
        self.report_bug_window.geometry("410x350+0+0")
        self.report_bug_window.resizable(width=False, height=False)
        self.report_bug_window.attributes("-topmost", True)
        self.report_bug_window.focus_force()
        self.report_bug_window_main_label = Label(self.report_bug_window, text="Report Bug", font=("Courier New bold", 35))
        self.report_bug_window_main_label.place(relx=.5, rely=.075, anchor=CENTER)
        self.report_bug_window_main_label.configure(bg=bg, fg=fg)
        self.report_bug_window_text_label = Label(self.report_bug_window, text="Subject:", font=("Courier New bold", 15))
        self.report_bug_window_text_label.place(relx=.5, rely=.175, anchor=CENTER)
        self.report_bug_window_text_label.configure(bg=bg, fg=fg)
        self.subject_entry = Entry(self.report_bug_window, borderwidth=2, relief=RIDGE, width=40)
        self.subject_entry.place(relx=.5, rely=.25, anchor=CENTER)
        self.subject_entry.configure(bg=bg, insertbackground=fg, fg=fg)
        self.message_text_label = Label(self.report_bug_window, text="Message:", font=("Courier New bold", 15))
        self.message_text_label.place(relx=.5, rely=.33, anchor=CENTER)
        self.message_text_label.configure(bg=bg, fg=fg)
        self.message_text = Text(self.report_bug_window, borderwidth=2, relief=RIDGE, width=50, height=10)
        self.message_text.place(relx=.5, rely=.6, anchor=CENTER)
        self.message_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.report_bug_button = Button(self.report_bug_window, text="Report Bug", font=("Courier New bold", 15), command=self.report_bug)
        self.report_bug_button.place(relx=.5, rely=.875, anchor=CENTER)
        self.report_bug_button.configure(highlightbackground=bg)
        self.quit_button = Button(self.report_bug_window, text="Quit", font=("Courier New bold", 15), command=self.quit)
        self.quit_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.quit_button.configure(highlightbackground=bg)

    def report_bug(self):
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", END)
        if subject == "":
            showinfo("Error", "Subject Cannot Be Empty")
        elif message == " ":
            showinfo("Error", "Message Cannot Be Empty")
        else:
            sender_email = "encryptedmessager@gmail.com"
            sender_password = "zyapguy!"
            recipient = "joshyacktman@gmail.com"
            subject = "JDE: " + subject
            body = ("Bug Report: {}".format(message))
            final_message = "Subject: {}\n\n{}".format(subject, body)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, final_message)
            showinfo("Report Bug", "Bug Report Has Been Sent")
            self.report_bug_window.destroy()

    def quit(self):
        self.report_bug_window.destroy()

class help_info(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.help_info_window = Toplevel()
        self.help_info_window.title("Help")
        self.help_info_window.geometry("400x400+0+0")
        self.help_info_window.configure(background=bg)
        self.help_info_window.resizable(width=False, height=False)
        self.help_info_window.attributes("-topmost", True)
        self.help_info_window.focus_force()
        self.help_info_window_main_label = Label(self.help_info_window, text="Help", font=("Courier New bold", 35))
        self.help_info_window_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.help_info_window_main_label.configure(bg=bg, fg=fg)
        self.info_text = Text(self.help_info_window, borderwidth=3, relief=SUNKEN, width=50, height=20)
        self.info_text.insert("1.0", "- Clear-CMD: Clears the terminal\n- StackOverflow: Opens StackOverflow\n- Create-Temp: Creates template\n- Open-Temp: Opens template\n- Delete-Temp: Deletes template")
        self.info_text.config(state=DISABLED)
        self.info_text.place(relx=.5, rely=.5, anchor=CENTER)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button = Button(self.help_info_window, text="Ok", font=("Courier New bold", 15), command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)

    def ok(self):
        self.help_info_window.destroy()

class shortcuts_page(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.shortcuts_page_window = Toplevel()
        self.shortcuts_page_window.title("Shortcuts")
        self.shortcuts_page_window.geometry("400x400+0+0")
        self.shortcuts_page_window.configure(background=bg)
        self.shortcuts_page_window.resizable(width=False, height=False)
        self.shortcuts_page_window.attributes("-topmost", True)
        self.shortcuts_page_window.focus_force()
        self.shortcuts_page_main_label = Label(self.shortcuts_page_window, text="Shortcuts", font=("Courier New bold", 35))
        self.shortcuts_page_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.shortcuts_page_main_label.configure(bg=bg, fg=fg)
        self.info_text = Text(self.shortcuts_page_window, borderwidth=3, relief=SUNKEN, width=50, height=20)
        self.info_text.insert("1.0", "- Command + t: Creates a new tab\n- Command + O: Opens a file\n- Command + S: Saves a file\n- Command + F: Find and replace\n- Command + R / F5: Runs file\n- Command + /: Turns line(s) into comment(s)\n- Shift + Tab: Unindents line\n- Command + Shift + K: Deletes line\n- F1: Help menu\n- Command + B: Adds breakpoint to next line")
        self.info_text.config(state=DISABLED)
        self.info_text.place(relx=.5, rely=.5, anchor=CENTER)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button = Button(self.shortcuts_page_window, text="Ok", font=("Courier New bold", 15), command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)

    def ok(self):
        self.shortcuts_page_window.destroy()

class keyword_change_page(Frame):
    def __init__(self, *args, **kwargs):
        self.color_mode = kwargs.pop("color_mode")
        Frame.__init__(self, *args, **kwargs)
        if self.color_mode == "Dark":
            bg = "#4f4c4d"
            fg = "white"
        else:
            bg = "white"
            fg = "#4f4c4d"
        self.keyword_change_page_window = Toplevel()
        self.keyword_change_page_window.title("Keyword Change")
        self.keyword_change_page_window.geometry("400x500+0+0")
        self.keyword_change_page_window.configure(background=bg)
        self.keyword_change_page_window.resizable(width=False, height=False)
        self.keyword_change_page_window.attributes("-topmost", True)
        self.keyword_change_page_window.focus_force()
        self.keyword_change_page_main_label = Label(self.keyword_change_page_window, text="Keyword Change", font=("Courier New bold", 35))
        self.keyword_change_page_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.keyword_change_page_main_label.configure(bg=bg, fg=fg)
        self.keyword_listbox = Listbox(self.keyword_change_page_window, width=30, height=10)
        self.keyword_listbox.place(relx=.5, rely=.325, anchor=CENTER)
        self.keyword_listbox.configure(bg=bg, fg=fg, selectbackground=bg, selectforeground=fg)
        for item in keywords_list:
            self.keyword_listbox.insert(END, item)
        self.add_entry = Entry(self.keyword_change_page_window, width=30)
        self.add_entry.place(relx=.5, rely=.525, anchor=CENTER)
        self.add_entry.configure(bg=bg, fg=fg, insertbackground=fg)
        self.add_button = Button(self.keyword_change_page_window, text="Add Item", font=("Courier New bold", 15), width=15, command=self.add)
        self.add_button.place(relx=.5, rely=.5786, anchor=CENTER)
        self.add_button.configure(highlightbackground=bg)
        self.remove_button = Button(self.keyword_change_page_window, text="Remove Item", font=("Courier New bold", 15), width=15, command=self.remove)
        self.remove_button.place(relx=.5, rely=.6322, anchor=CENTER)
        self.remove_button.configure(highlightbackground=bg)
        self.move_up_button = Button(self.keyword_change_page_window, text="Move Up", font=("Courier New bold", 15), width=15, command=self.move_up)
        self.move_up_button.place(relx=.5, rely=.6858, anchor=CENTER)
        self.move_up_button.configure(highlightbackground=bg)
        self.move_to_top_button = Button(self.keyword_change_page_window, text="Move to Top", font=("Courier New bold", 15), width=15, command=self.move_to_top)
        self.move_to_top_button.place(relx=.5, rely=.7394, anchor=CENTER)
        self.move_down_button = Button(self.keyword_change_page_window, text="Move Down", font=("Courier New bold", 15), width=15, command=self.move_down)
        self.move_down_button.place(relx=.5, rely=.793, anchor=CENTER)
        self.move_down_button.configure(highlightbackground=bg)
        self.move_to_bottom_button = Button(self.keyword_change_page_window, text="Move to Bottom", font=("Courier New bold", 15), width=15, command=self.move_to_bottom)
        self.move_to_bottom_button.place(relx=.5, rely=.8466, anchor=CENTER)
        self.move_to_middle_button = Button(self.keyword_change_page_window, text="Move to Middle", font=("Courier New bold", 15), width=15, command=self.move_to_middle)
        self.move_to_middle_button.place(relx=.5, rely=.9002, anchor=CENTER)
        self.move_to_middle_button.configure(highlightbackground=bg)
        self.ok_button = Button(self.keyword_change_page_window, text="Ok", font=("Courier New bold", 15), command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)

    def add(self):
        if self.add_entry.get() != "":
            if " " not in self.add_entry.get():
                keywords_list.append(self.add_entry.get())
                update_list()
                self.keyword_listbox.insert(END, self.add_entry.get())
                self.add_entry.delete(0, END)
            else:
                showerror("Error Found", "Keyword Insertion Error\n\nNo Spaces Allowed in Keyword")
        else:
            showerror("Error Found", "Keyword Insertion Error\n\nPlease Enter A Keyword")

    def remove(self):
        if self.keyword_listbox.curselection() != ():
            self.keyword_listbox.delete(self.keyword_listbox.curselection())
            keywords_list.remove(keywords_list[self.keyword_listbox.curselection()[0]])
            update_list()


    def move_up(self):
        if self.keyword_listbox.get(ANCHOR) != "":
            position_list = self.keyword_listbox.curselection()
            for position in position_list:
                item = self.keyword_listbox.get(position)
                self.keyword_listbox.delete(position)
                keywords_list.pop(position)
                self.keyword_listbox.insert(position-1, item)
                keywords_list.insert(position-1, item)
            update_list()

    def move_to_top(self):
        if self.keyword_listbox.get(ANCHOR) != "":
            position_list = self.keyword_listbox.curselection()
            for position in position_list:
                item = self.keyword_listbox.get(position)
                self.keyword_listbox.delete(position)
                keywords_list.pop(position)
                self.keyword_listbox.insert(0, item)
                keywords_list.insert(0, item)
            update_list()

    def move_down(self):
        if self.keyword_listbox.get(ANCHOR) != "":
            position_list = self.keyword_listbox.curselection()
            for position in position_list:
                item = self.keyword_listbox.get(position)
                self.keyword_listbox.delete(position)
                keywords_list.pop(position)
                self.keyword_listbox.insert(position+1, item)
                keywords_list.insert(position+1, item)
            update_list()

    def move_to_bottom(self):
        if self.keyword_listbox.get(ANCHOR) != "":
            position_list = self.keyword_listbox.curselection()
            for position in position_list:
                item = self.keyword_listbox.get(position)
                self.keyword_listbox.delete(position)
                keywords_list.pop(position)
                self.keyword_listbox.insert(END, item)
                keywords_list.append(item)
            update_list()

    def move_to_middle(self):
        if self.keyword_listbox.get(ANCHOR) != "":
            position_list = self.keyword_listbox.curselection()
            for position in position_list:
                item = self.keyword_listbox.get(position)
                self.keyword_listbox.delete(position)
                keywords_list.pop(position)
                self.keyword_listbox.insert(int(len(keywords_list)/2), item)
                keywords_list.insert(int(len(keywords_list)/2), item)
            update_list()

    def ok(self):
        self.keyword_change_page_window.destroy()

#Testing purposes
if __name__ == "__main__":
    root = Tk()
    root.title("Widget Testing")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("{}x{}+0+0".format(width, height))
    # Main widget called ultra_text
    text = ultra_text(root, window=root, color_mode = "Light", width=130, height=30)
    text.place(relx=.5, rely=.5, anchor=CENTER)
    text.text.focus()
    text.change_color("Light")
    # # keyword_change_page(root, color_mode = "Light")
    # settings(root, color_mode = "Light")
    root.mainloop()