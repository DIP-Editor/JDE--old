#get imports
from tkinter import *
from tkinter.filedialog import *
from tkinter import colorchooser
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter.ttk import Progressbar, Style, Notebook
from extension_handler import *
import os
import idlelib.colorizer as ic
import idlelib.percolator as ip
import smtplib
from itertools import groupby
import re
from os import listdir
import sys
from pathlib import Path
#Get path (Used for application)
if getattr(sys, "frozen", False):
    folder = Path(sys._MEIPASS)
else:
    folder = Path(__file__).parent
#Get theme from file
theme_style = open(folder / "color_theme.txt", "r").readlines()
light_mode_style = theme_style[0].split(";")
light_mode_bg = light_mode_style[0].split(": ")[1].split("=")[1]
light_mode_fg = light_mode_style[1].split("=")[1].split(";")[0]
dark_mode_style = theme_style[1].split(";")
dark_mode_bg = dark_mode_style[0].split(": ")[1].split("=")[1]
dark_mode_fg = dark_mode_style[1].split("=")[1].split(";")[0]
#Get Font from file
font_style = open(folder / "font.txt", "r").readlines()
font_name = font_style[0].split("\n")[0]
normal_size = int(font_style[1].split("\n")[0])
medium_size = int(font_style[2].split("\n")[0])
large_size = int(font_style[3].split("\n")[0])
min = font_style[4].split("\n")[0]
max = font_style[5].split("\n")[0]
normal_font = (font_name, normal_size)
medium_font = (font_name, medium_size)
large_font = (font_name, large_size)
#Get the dilate size from file
dilate_size = int(open(folder / "dilate_size.txt", "r").readlines()[0])
def update_dilate_size():
    global dilate_size
    with open(folder / "dilate_size.txt", "r") as f:
        dilate_size = int(f.readlines()[0])
#Create function to reset fonts and colors
def reset_fonts_colors():
    global normal_font
    global medium_font
    global large_font
    global normal_size
    global medium_size
    global large_size
    global min
    global max
    global light_mode_bg
    global light_mode_fg
    global dark_mode_bg
    global dark_mode_fg
    global keywords_list
    font_style = open(folder / "font.txt", "r").readlines()
    font_name = font_style[0].split("\n")[0]
    normal_size = int(font_style[1].split("\n")[0])
    medium_size = int(font_style[2].split("\n")[0])
    large_size = int(font_style[3].split("\n")[0])
    min = font_style[4].split("\n")[0]
    max = font_style[5].split("\n")[0]
    normal_font = (font_name, normal_size)
    medium_font = (font_name, medium_size)
    large_font = (font_name, large_size)
    theme_style = open(folder / "color_theme.txt", "r").readlines()
    light_mode_style = theme_style[0].split(";")
    light_mode_bg = light_mode_style[0].split(": ")[1].split("=")[1]
    light_mode_fg = light_mode_style[1].split("=")[1].split(";")[0]
    dark_mode_style = theme_style[1].split(";")
    dark_mode_bg = dark_mode_style[0].split(": ")[1].split("=")[1]
    dark_mode_fg = dark_mode_style[1].split("=")[1].split(";")[0]
    with open(folder / "keywords.txt", "r") as f:
        keywords_list = f.read().splitlines()
#Get keywords from file
with open(folder / "keywords.txt", "r") as f:
    keywords_list = f.read().splitlines()
#Create function to update keywords file and list
def update_list():
    with open(folder / "keywords.txt", "r+") as f:
        f.truncate()
        f.seek(0)
        f.truncate()
        f.seek(0)
        for item in keywords_list:
            f.write(item + "\n")
#Create function to get all the info updated
def get_info_from_files():
    global theme_style
    global light_mode_style
    global light_mode_bg
    global light_mode_fg
    global dark_mode_style
    global dark_mode_bg
    global dark_mode_fg
    global font_style
    global font_name
    global normal_size
    global medium_size
    global large_size
    global min
    global max
    global normal_font
    global medium_font
    global large_font
    theme_style = open(folder / "color_theme.txt", "r").readlines()
    light_mode_style = theme_style[0].split(";")
    light_mode_bg = light_mode_style[0].split(": ")[1].split("=")[1]
    light_mode_fg = light_mode_style[1].split("=")[1].split(";")[0]
    dark_mode_style = theme_style[1].split(";")
    dark_mode_bg = dark_mode_style[0].split(": ")[1].split("=")[1]
    dark_mode_fg = dark_mode_style[1].split("=")[1].split(";")[0]
    #Get Font from file
    font_style = open(folder / "font.txt", "r").readlines()
    font_name = font_style[0].split("\n")[0]
    normal_size = int(font_style[1].split("\n")[0])
    medium_size = int(font_style[2].split("\n")[0])
    large_size = int(font_style[3].split("\n")[0])
    min = font_style[4].split("\n")[0]
    max = font_style[5].split("\n")[0]
    normal_font = (font_name, normal_size)
    medium_font = (font_name, medium_size)
    large_font = (font_name, large_size)
    update_dilate_size()
    reset_fonts_colors()

#Create ToolTip class
class ToolTip():
    def __init__(self, master, orient="E", *args, **kwargs):
        #Get necessary arguments
        self.window = kwargs.pop("window")
        self.tooltip_text = kwargs.pop("text")
        self.orient = orient
        self.overall_widget = master
        #Get info and create bindings
        self.overall_widget.bind("<Enter>", self.create_label)
        self.overall_widget.bind("<Leave>", self.destroy_label)
        self.overall_widget.bind("<ButtonPress>", self.destroy_label)

    def create_label(self, event):
        #Create tooltip label and place next to widget
        self.tooltip = Label(self.window, text=self.tooltip_text, bg="yellow", fg="black", bd=1, relief=SOLID, font=normal_font)
        if self.orient == "N":
            self.tooltip.place(x=self.overall_widget.winfo_x(), y=self.overall_widget.winfo_y()-self.tooltip.winfo_reqheight()-5)
        elif self.orient == "E":
            self.tooltip.place(x=self.overall_widget.winfo_x()+self.overall_widget.winfo_reqwidth()+5, y=self.overall_widget.winfo_y())
        elif self.orient == "S":
            self.tooltip.place(x=self.overall_widget.winfo_x(), y=self.overall_widget.winfo_y()+self.overall_widget.winfo_reqheight()+5)
        elif self.orient == "W":
            self.tooltip.place(x=self.overall_widget.winfo_x()-self.tooltip.winfo_reqwidth()-5, y=self.overall_widget.winfo_y())
        elif self.orient == "NE":
            self.tooltip.place(x=self.overall_widget.winfo_x()+self.overall_widget.winfo_reqwidth()+5, y=self.overall_widget.winfo_y()-self.tooltip.winfo_reqheight()-5)
        elif self.orient == "NW":
            self.tooltip.place(x=self.overall_widget.winfo_x()-self.tooltip.winfo_reqwidth()-5, y=self.overall_widget.winfo_y()-self.tooltip.winfo_reqheight()-5)
        elif self.orient == "SE":
            self.tooltip.place(x=self.overall_widget.winfo_x()+self.overall_widget.winfo_reqwidth()+5, y=self.overall_widget.winfo_y()+self.overall_widget.winfo_reqheight()+5)
        elif self.orient == "SW":
            self.tooltip.place(x=self.overall_widget.winfo_x()-self.tooltip.winfo_reqwidth()-5, y=self.overall_widget.winfo_y()+self.overall_widget.winfo_reqheight()+5)
        else:
            self.tooltip.place(x=self.overall_widget.winfo_x()+self.overall_widget.winfo_reqwidth()+5, y=self.overall_widget.winfo_y())
    def destroy_label(self, event):
        #Destroy tooltip label
        self.tooltip.destroy()

class ultra_text(Frame):
    def __init__(self, *args, **kwargs):
        #Get necessary arguments
        self.have_syntax = kwargs.pop("have_syntax")
        self.window = kwargs.pop("window")
        self.color_mode = kwargs.pop("color_mode")
        #Set up Frame
        Frame.__init__(self, *args, **kwargs)
        #Set up color_mode
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Defining colors for syntax highlighting
        self.cdg = ic.ColorDelegator()
        with open(folder / "settings.txt", "r") as settings:
            settings = settings.read()
        settings = settings.split("\n")
        tag_imports = str(settings[0])
        tag_comment = str(settings[1])
        tag_keyword = str(settings[2])
        tag_builtin = str(settings[3])
        tag_string = str(settings[4])
        tag_definition = str(settings[5])
        tag_class = str(settings[6])
        self.cdg.tagdefs["COMMENT"] = {"foreground": tag_comment}
        self.cdg.tagdefs["KEYWORD"] = {"foreground": tag_keyword}
        self.cdg.tagdefs["BUILTIN"] = {"foreground": tag_builtin}
        self.cdg.tagdefs["STRING"] = {"foreground": tag_string}
        self.cdg.tagdefs["DEFINITION"] = {"foreground": tag_definition}
        self.cdg.tagdefs["CLASS"] = {"foreground": tag_class}

        update_dilate_size()
        self.text_font = (font_name, dilate_size)

        #Create base text widget
        if "height" and "width" in kwargs:
            self.text = Text(self, height=kwargs["height"], width=kwargs["width"], borderwidth=2, relief=RIDGE, wrap=NONE, undo=True, font=self.text_font)
        else:
            #, width=130, height=29
            self.text = Text(self, font=self.text_font, wrap="none", undo=True, borderwidth=2, relief=RIDGE, width=95, height=25)
        #Check if syntax highlighting is needed
        self.perc = ip.Percolator(self.text)
        if self.have_syntax == True:
            self.perc.insertfilter(self.cdg)
        
        #Create scrollbar
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        #Create numberLines
        self.numberLines = TextLineNumbers(self, width=40)
        self.numberLines.attach(self.text)

        #Create breakpoints
        if self.have_syntax == True:
            self.breakpoints = BreakpointBar(self, width=20)
            self.breakpoints.attach(self.text)

        #Pack widgets
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.numberLines.pack(side=LEFT, fill=Y, padx=(5, 0))
        if self.have_syntax == True:
            self.breakpoints.pack(side=LEFT, fill=Y)
        self.text.pack(side=RIGHT, fill=BOTH, expand=True)

        #Create bindings
        self.window.bind("<Any-KeyRelease>", self.redraw)
        self.window.bind("<BackSpace>", lambda x: self.after(1, (self.redraw())), add=True)
        self.text.bind("<Motion>", self.redraw)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        self.text.bind("<KeyRelease-Return>", self.redraw, add=True)
        self.text.bind("<KeyRelease-Return>", lambda x: [self.redraw(), self.new_line_indent(self), self.callback("")], add=True)
        self.text.bind("<Any-KeyRelease>", self._autocomplete, add=True)
        self.text.bind("<Any-KeyRelease>", self.parse_line, add=True)
        self.window.bind("<Button-1>", self.parse_line, add=True)
        self.text.bind("<BackSpace>", self.parse_text, add=True)
        self.text.bind("<Return>", self.parse_text, add=True)
        self.text.bind("<Tab>", self._handle_tab, add=True)
        self.text.bind("\"", self.double_quotes)
        self.text.bind("\'", self.double_punctuation)
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
        self.text.bind("<Command-k>", self.delete_line)
        self.text.bind("<Command-b>", self.add_breakpoint)
        self.text.bind("<Command-a>", self.select_all)
        self.text.bind("<Command-Shift-Z>", self.redo)

        #Create font with 4 spaces
        font = Font(font=self.text["font"])
        tab_width = font.measure("    ")
        self.text.config(tabs=(tab_width))

        self.temporary_autocomplete_list = []
        self.restricted_events = [97, 100663418, 134217827, 50331750, 285212788, 150995062, 117440632, 671088747, 251658354, 104857722, 218103927, 906033406, 704643164]

    def redo(self, event):
        self.text.edit_redo()
        self.redraw()

    def select_all(self, event=None):
        line_count = self.text.index("end-1c").split(".")[0]
        for i in range(int(line_count)):
            self.text.tag_add("sel", "{}.0".format(i+1), "{}.end".format(i+1))
            if self.text.get("{}.0".format(i+1), "{}.end".format(i+1)) == "":
                self.text.insert("{}.0".format(i+1), " ")
            self.text.tag_add("sel", "{}.0".format(i+1), "{}.end".format(i+1))
        length_of_line = self.text.index("end-1c").split(".")[1]
        self.text.mark_set("insert", "{}.{}".format(line_count, length_of_line))
        self.text.see("insert")
        return "break"

    def increase_font(self, event=None):
        if int(self.text_font[1])+1 <= int(max):
            self.text_font = (self.text_font[0], int(self.text_font[1]) + 1)
            self.text.config(font=self.text_font)
            self.redraw()

    def decrease_font(self, event=None):
        if int(self.text_font[1])-1 >= int(min):
            self.text_font = (self.text_font[0], int(self.text_font[1]) - 1)
            self.text.config(font=self.text_font)
            self.redraw()

    def remove_indentation(self, event=None):
        #Print yview
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
        #Check if the ) is being pressed in front of a ) and then remove the ) if it is
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
        #Check if the } is being pressed in front of a } and then remove the } if it is
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
        #Check if the ] is being pressed in front of a ] and then remove the ] if it is
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
        #Check if the backspace is being pressed in front of a ( or { or [ and then remove the ) or } or ] if they are to the right
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
        #Insert breakpoint to the next line (Creates a new line for the breakpoint)
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
                    elif current_line_contents[-1] == ":":
                        self.text.insert("{}.0".format(int(current_line)+1), "\t")
                    elif current_line_contents[-1] == ",":
                        self.text.insert("{}.0".format(int(current_line)+1), "\t") 
                else:
                    for i in range(current_line_contents.count("    ")):
                        self.text.insert("{}.0".format(int(current_line)+1), "    ")
                    if current_line_contents[-1] == ":":
                        self.text.insert("{}.0".format(int(current_line)+1), "    ")
        self.redraw()

    def delete_line(self, event=None):
        #Deletes the current line
        try:
            first_line = int(self.text.index("sel.first").split("."))
            last_line = int(self.text.index("sel.last").split("."))
            self.text.delete("{}".format(first_line), "{}".format(last_line))
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
        #Converts tabs to spaces
        while "\t" in self.text.get(1.0, END):
            new_contents = self.text.get(1.0, END).replace("\t", "    ")
            self.text.delete(1.0, END)
            self.text.insert(1.0, new_contents)
            self.text.mark_set(INSERT, INSERT)
    
    def spaces_to_tabs(self, event=None):
        #Converts spaces to tabs
        while "    " in self.text.get(1.0, END):
            new_contents = self.text.get(1.0, END).replace("    ", "\t")
            self.text.delete(1.0, END)
            self.text.insert(1.0, new_contents)
            self.text.mark_set(INSERT, INSERT)

    def change_color(self, new_color):
        #Changes the color of the text
        if new_color == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.config(background=bg)
        self.text.config(bg=bg, fg=fg, insertbackground=fg)
        self.numberLines.config(bg=bg)
        if self.have_syntax == True:
            self.breakpoints.config(bg=bg)

    def reset_syntax(self):
        if self.have_syntax:
            self.perc.removefilter(self.cdg)
            self.cdg = ic.ColorDelegator()
            with open(folder / "settings.txt", "r") as settings:
                settings = settings.read()
            settings = settings.split("\n")
            tag_imports = str(settings[0])
            tag_comment = str(settings[1])
            tag_keyword = str(settings[2])
            tag_builtin = str(settings[3])
            tag_string = str(settings[4])
            tag_definition = str(settings[5])
            tag_class = str(settings[6])
            self.cdg.tagdefs["COMMENT"] = {"foreground": tag_comment}
            self.cdg.tagdefs["KEYWORD"] = {"foreground": tag_keyword}
            self.cdg.tagdefs["BUILTIN"] = {"foreground": tag_builtin}
            self.cdg.tagdefs["STRING"] = {"foreground": tag_string}
            self.cdg.tagdefs["DEFINITION"] = {"foreground": tag_definition}
            self.cdg.tagdefs["CLASS"] = {"foreground": tag_class}
            self.perc.insertfilter(self.cdg)

    def squeeze(self, s):
        return re.sub(r'(.)\1+', r'\1', s)

    def special_sort(self, special_list):
        for i in range(len(special_list)):
            for j in range(len(special_list)):
                if special_list[i] in special_list[j]:
                    #Bring behind i
                    special_list.insert(i, special_list.pop(j))
            return special_list

    def callback(self, word):
        #Returns possible matches
        #Remove duplicates without changing order
        self.temporary_autocomplete_list = list(dict.fromkeys(self.temporary_autocomplete_list))
        #Remove old variables
        self.check_in_file()
        #words is a list of almost every keyword and builtin function
        words = keywords_list + self.temporary_autocomplete_list
        #Remove duplicates without changing order
        words = list(dict.fromkeys(words))
        #Sort and squeeze
        words = [s for _, g in groupby(words, self.squeeze) for s in sorted(g, key=len)]
        # 
        # 
        # 
        #Sort using special_sort
        last_sort = self.special_sort(words)
        while True:
            sort = self.special_sort(last_sort)
            if sort == last_sort:
                break
            else:
                last_sort = sort
        #Make words the sorted list
        words = last_sort
        # 
        # 
        # 
        #Remove blank words
        words = [word for word in words if word != ""]
        matches = [x for x in words if x.startswith(word)]
        return matches

    def _handle_tab(self, event):
        #Handles tab key ans inserts four spaces
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
        #Autocompletes the current word 
        print(event)
        if event.char and self.callback and event.keysym != "BackSpace" and (event.keycode not in self.restricted_events):
            word = self.text.get("insert-1c wordstart", "insert-1c wordend")
            #wordstart
            if "\n" in word:
                word = word.split("\n")[1]
            matches = self.callback(word)
            if matches:
                remainder = matches[0][len(word):]
                insert = self.text.index("insert")
                self.text.insert(insert, remainder, ("sel", "autocomplete"))
                self.text.mark_set("insert", insert)

    def parse_line(self, event=None, line=None):
        if line is None:
            current_line = int(self.text.index("insert").split(".")[0])
            current_line_contents = self.text.get("{}.0".format(current_line-1), "{}.end".format(current_line-1))
        else:
            current_line_contents = line
        #Parse the line to get variables and functions so they can be added to the temporary_autocomplete_list
        #This is done to avoid autocompleteing variables and functions that are not in other files
        #Get the contents of the last line
        #Check if the current line is a variable or a function or a class or a module or none of the above
        if "=" or "def" or "class" or "module" in current_line_contents:
            if "=" in current_line_contents:
                #Get the variable name
                variable_name = current_line_contents.split("=")[0].strip()
                #Add the variable name to the list of important things
                #Check if it is only one character long
                if len(variable_name) == 1:
                    #Check if it is a letter
                    if variable_name.isalpha():
                        #Add to the front of the list
                        self.temporary_autocomplete_list.insert(0, variable_name)
                else:
                    self.temporary_autocomplete_list.append(variable_name)
            elif current_line_contents.startswith("def"):
                #Get the function name
                function_name = current_line_contents.split("(")[0].split("def")[1].strip()
                #Add the function name to the list of important things
                self.temporary_autocomplete_list.append(function_name)
            elif current_line_contents.startswith("class"):
                #Get the class name
                class_name = current_line_contents.split(":")[0].split("class")[1].strip()
                #Check if the class is a subclass of another class
                if "(" in class_name:
                    #Get the superclass name
                    superclass_name = class_name.split("(")[0].strip()
                    #Add the superclass name to the list of important things
                    self.temporary_autocomplete_list.append(superclass_name)
                #Add the class name to the list of important things
                self.temporary_autocomplete_list.append(class_name)
            elif current_line_contents.startswith("import") or current_line_contents.startswith("from"):
                if "from" in current_line_contents:
                    try:
                        #Get the module name
                        module_name = current_line_contents.split("import")[0].split("from")[1].split(".")[0].strip()
                        #Add the module name to the list of important things
                        self.temporary_autocomplete_list.append(module_name)
                        #Get what is being imported
                        imported_name = current_line_contents.split("import")[1]
                        if "," in imported_name:
                            imported_split = imported_name.split(",")
                            for split_import in imported_split:
                                #Add the imported name to the list of important things
                                self.temporary_autocomplete_list.append(split_import.strip())
                        else:
                            #Add the imported name to the list of important things
                            self.temporary_autocomplete_list.append(imported_name.strip())
                    except:
                        pass
                else:
                    #Get the module name
                    module_name = current_line_contents.split("import")[1].split(".")[0].strip()
                    #Add the module name to the list of important things
                    self.temporary_autocomplete_list.append(module_name)

    def parse_text(self, event=None):
        self.temporary_autocomplete_list = []
        contents = self.text.get(1.0, END)
        for line in contents.split("\n"):
            self.parse_line(line = line)
        self.callback("")

    def check_in_file(self, event=None):
        contents = self.text.get(1.0, END)
        for item in self.temporary_autocomplete_list:
            if item not in contents:
                self.temporary_autocomplete_list.remove(item)

    def open_template(self, x, y, event=None, **kwargs):
        #Creates an open template window
        color_mode = kwargs.pop("color_mode")
        self.open_template = temp_open_pop_up(self, text=self, x=x, y=y, color_mode=color_mode)

    def double_parentheses(self, event):
        #Inserts back parentheses when ( is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, ")")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def double_curly_braces(self, event):
        #Inserts back curly braces when { is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "}")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def double_square_braces(self, event):
        #Inserts back square braces when [ is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "]")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def back_tab(self, event):
        #removes one tab when Command-Shift-Tab is pressed
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
        #Makes a comment on the current line when Command-/ is pressed
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
        #Inserts back quotes when " is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "\"")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def double_punctuation(self, event):
        #Inserts back punctuation when ' is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, "'")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))

    def new_line_indent(self, event=None):
        #Inserts a new line and indents it when Enter is pressed
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

    def return_anchor(self, event):
        #Returns the anchor of the current cursor
        return self.text.index("insert")
    
    def onScrollPress(self, *args):
        #Scrolls the text when mouse wheel is used
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)
        if self.have_syntax == True:
            self.scrollbar.bind("<B1-Motion>", self.breakpoints.redraw)

    def onScrollRelease(self, *args):
        #Unbinds the scrollbar when mouse wheel is released
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)
        if self.have_syntax == True:
            self.scrollbar.unbind("<B1-Motion>", self.breakpoints.redraw)

    def onPressDelay(self, *args):
        #Delays the execution of the onPress function
        self.redraw(*args)


    def get(self, *args, **kwargs):
        #Allowws for the use of get
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        #Allows for the use of insert
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        #Allows for the use of delete
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        #Allows for the use of index
        return self.text.index(*args, **kwargs)

    def redraw(self, event=None):
        #Redraws the text
        self.numberLines.redraw()
        if self.have_syntax == True:
            if event:
                self.breakpoints.redraw(event)
            else:
                self.breakpoints.redraw()

#Create TextLineNumbers class
class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        #Initializes the canvas
        Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        #Attaches the canvas to the text widget
        self.textwidget = text_widget

    def redraw(self, *args):
        #Redraws the canvas
        """redraw line numbers"""
        try:
            self.delete("all")

            i = self.textwidget.index("@0,0")
            while True :
                dline= self.textwidget.dlineinfo(i)
                if dline is None: break
                y = dline[1]
                linenum = str(i).split(".")[0]
                size = normal_size
                if int(linenum) >= 10000:
                    #line_size is every 10^nth increment of the line number after the first 10000 lines
                    line_size = linenum[:len(linenum)-4]
                    #Turn line_size to an integer divided by 10
                    line_size = int(int(line_size)/10)
                    if line_size == 0:
                        line_size = 1
                    size = size-int(3*(line_size*1.75))
                    if size < 3:
                        size = 3
                self.create_text(2, y, anchor="nw", text=linenum, font=(font_name, size), fill="#2197db") #606366 #90a395 #808090 #14a83c #2893d1 #2197db
                i = self.textwidget.index("%s+1line" % i)
        except:
            pass

#Create a breakpoint bar class
class BreakpointBar(Canvas):
    def __init__(self, *args, **kwargs):
        #Initializes the canvas
        Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None
        self.bind("<Motion>", self.redraw)

    def attach(self, text_widget):
        #Attaches the canvas to the text widget
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        i = self.textwidget.index("@0,0")
        if len(args) > 0:
            self.delete("all")
            self.unbind_all("<Enter>")
            self.unbind_all("<Leave>")
            event = args[0]
            # print(str(event).split(" ")[0].split("<")[1])
            index = self.textwidget.index("@{},{}".format(event.x, event.y))
            index_linenum = str(index).split(".")[0]
            while True:
                dline= self.textwidget.dlineinfo(i)
                if dline is None: break
                y = dline[1]
                linenum = str(i).split(".")[0]
                if linenum == index_linenum:
                    oval = self.create_oval(5, y, 15, y+10, fill="red", outline="red")
                    self.tag_bind(oval, "<Enter>", lambda event: self.on_enter(event, oval))
                    self.tag_bind(oval, "<Leave>", lambda event: self.on_exit(event, oval))
                    self.tag_bind(oval, "<Button-1>", lambda event: self.on_press(event, oval))
                i = self.textwidget.index("%s+1line" % i)

    def on_enter(self, event, oval):
        self.itemconfig(oval, fill="dark red", outline="dark red")


    def on_exit(self, event, oval):
        self.itemconfig(oval, fill="red", outline="red")

    def on_press(self, event, oval):
        index_linenum = int(str(self.textwidget.index("@{},{}".format(event.x, event.y))).split(".")[0])
        self.textwidget.tag_remove("sel", "1.0", "end")
        self.textwidget.insert("{}.end".format(index_linenum), "\nbreakpoint()\n")
        self.textwidget.focus()
        self.textwidget.mark_set("insert", "{}.end".format(index_linenum+2))
        # self.after(10, self.redraw(event))

#Create find and replace class
class search_text(Frame):
    def __init__(self, *args, **kwargs):
        #Get necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create frame
        Frame.__init__(self, *args, **kwargs)
        #Set colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create window
        self.search_text_window = Toplevel(self)
        self.search_text_window.resizable(False, False)
        self.search_text_window.title("Search / Find and Replace")
        self.search_text_window.config(bg=bg)
        self.search_text_window.geometry("+{}+{}".format(self.x, self.y))
        self.search_text_window.attributes("-topmost", True)
        #Create widgets
        self.text_search_entry = Entry(self.search_text_window, borderwidth=3, font=normal_font, relief=SUNKEN, justify=CENTER)
        self.search_button = Button(self.search_text_window, text="Search File", font=normal_font, command=self.test_find)
        self.text_replace_entry = Entry(self.search_text_window, borderwidth=3, font=normal_font, relief=SUNKEN, justify=CENTER)
        self.replace_button = Button(self.search_text_window, text="Replace", font=normal_font, command=self.test_replace)
        self.replace_all_button = Button(self.search_text_window, text="Replace All", font=normal_font, command=self.test_replace_all)
        self.search_list = list()
        self.index = 0
        self.locations = []
        self.is_first_search = True
        self.text_search_entry.pack(side=LEFT, fill=BOTH, expand=1)
        self.search_button.pack(side=LEFT)
        self.text_replace_entry.pack(side=LEFT, fill=BOTH, expand=1)
        self.replace_button.pack(side=LEFT)
        self.replace_all_button.pack(side=LEFT)
        self.text_search_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.text_replace_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.search_button.configure(highlightbackground=bg)
        self.replace_button.configure(highlightbackground=bg)
        self.replace_all_button.configure(highlightbackground=bg)
        self.search_text_window.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        #Close window
        self.search_text_window.destroy()
        self.destroy()

    def reset_color(self):
        #Resets the color of the text
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.search_text_window.config(bg=bg)
        self.text_search_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.text_replace_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.search_button.configure(highlightbackground=bg)
        self.replace_button.configure(highlightbackground=bg)
        self.replace_all_button.configure(highlightbackground=bg)
        #Update fonts
        self.text_search_entry.configure(font=normal_font)
        self.text_replace_entry.configure(font=normal_font)
        self.search_button.configure(font=normal_font)
        self.replace_button.configure(font=normal_font)
        self.replace_all_button.configure(font=normal_font)
    
    def change_self_color(self):
        #Changes the color mode and then calls the reset_color function
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def attach(self, text, widget):
        #Attach the text widget
        self.text = text
        self.them = widget

    def search(self, special_string, target):
        occurences = []
        string_split = special_string.split("\n")
        target  = self.text_search_entry.get()
        if target:
            for row in range(len(string_split)):
                for col in range(len(string_split[row])):
                    if(string_split[row][col] == target[0] and len(string_split[row])-col >= len(target)):
                        iss = True
                        index = [str(row+1)+'.'+str(col)]
                        for i in range(1, len(target)):
                            if(string_split[row][col+1] != target[i]):
                                iss = False
                                break
                            else:
                                col = col + 1
                        if not iss:
                            continue
                        else:
                            index.append(str(row+1)+'.'+str(col+1))
                            occurences.append(index)
        return occurences

    def test_find(self):
        #Testing new finding method
        self.locations = []
        contents = self.text.get("1.0", "end")
        target = self.text_search_entry.get()
        if target == "":
            showwarning("Find and Replace Error", "A Find and Replace Error Has Occured.\n\nPlease Enter A Search Term.")
        else:
            self.locations = self.search(contents, target)
            if self.locations == []:
                pass
            else:
                if self.is_first_search == True:
                    self.is_first_search = False
                else:
                    self.index += 1
                if self.index > len(self.locations) - 1:
                    self.index = 0
                self.text.tag_remove(SEL, "1.0", "end")
                self.text.tag_add(SEL, self.locations[self.index][0], self.locations[self.index][1])
                self.text.mark_set(SEL, self.locations[self.index][1])
                self.text.see(self.locations[self.index][0])
                self.them.redraw()
                
    def find_no_show(self):
        self.locations = []
        contents = self.text.get("1.0", "end")
        target = self.text_search_entry.get()
        if target == "":
            return "No Search Term Entered"
        else:
            self.locations = self.search(contents, target)
            if self.locations == []:
                pass
            else:
                if self.is_first_search == True:
                    self.is_first_search = False
                else:
                    self.index += 1
                if self.index > len(self.locations) - 1:
                    self.index = 0

    def test_replace(self, replacing_all = False):
        #Test new replace method
        try:
            index = self.index
            works = self.find_no_show()
            if works == "No Search Term Entered":
                if replacing_all == False:
                    showwarning("Find and Replace Error", "A Find and Replace Error Has Occured.\n\nPlease Enter A Search Term")
            else:
                self.index = index
                if self.index > len(self.locations) - 1:
                    self.index = 0
                location = self.locations[self.index]
                self.text.delete(location[0], location[1])
                self.text.insert(location[0], self.text_replace_entry.get())
                if replacing_all == False:    
                    self.text.tag_remove(SEL, "1.0", "end")
                    self.text.tag_add(SEL, location[0], float(location[0])+(len(self.text_replace_entry.get())/10))
                    self.text.mark_set(SEL, float(location[0])+(len(self.text_replace_entry.get())/10))
                    self.text.see(float(location[0])+(len(self.text_replace_entry.get())/10))
                self.them.redraw()
        except:
            if replacing_all == False:
                showwarning("Find and Replace Error", "A Find and Replace Error Has Occured.\n\nCould Not Replace Desired Text")

    def test_replace_all(self):
        index = self.index
        self.find_no_show()
        self.index = index
        for i in range(len(self.locations)):
            self.index = i
            self.test_replace()

#Create template classes
class temp_name_pop_up(Frame):
    def __init__(self, text_info, **kwargs):
        #Get necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.text_info = text_info.get("1.0", "end-1c")
        #Initialize Frame
        Frame.__init__(self, bg=bg)
        #Create window
        self.pop_up_window = Toplevel()
        self.pop_up_window.title("Template Name")
        self.pop_up_window.config(bg=bg)
        self.pop_up_window.geometry("300x100+{}+{}".format(self.x, self.y))
        self.pop_up_window.resizable(width=False, height=False)
        self.pop_up_window.attributes("-topmost", True)
        self.pop_up_name_label = Label(self.pop_up_window, text="Template Name:", font=medium_font)
        self.pop_up_name_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.pop_up_name_label.configure(bg=bg, fg=fg)
        self.pop_up_name_entry = Entry(self.pop_up_window, font=normal_font, borderwidth=3, relief=SUNKEN, justify=CENTER)
        self.pop_up_name_entry.place(relx=.5, rely=.4, anchor=CENTER)
        self.pop_up_name_entry.configure(bg=bg, insertbackground = fg, fg=fg)
        self.confirm_button = Button(self.pop_up_window, text="Confirm", font=normal_font, command=self.confirm)
        self.confirm_button.place(relx=.125, rely=.85, anchor=CENTER)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.pop_up_window, text="Cancel", font=normal_font, command=self.cancel)
        self.cancel_button.place(relx=.875, rely=.85, anchor=CENTER)
        self.cancel_button.configure(highlightbackground=bg)
        self.pop_up_window.protocol("WM_DELETE_WINDOW", self.cancel)

    def reset_color(self):
        #Reset colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.pop_up_window.config(bg=bg)
        self.pop_up_name_label.configure(bg=bg, fg=fg)
        self.pop_up_name_entry.configure(bg=bg, insertbackground=fg, fg=fg)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button.configure(highlightbackground=bg)
        #Update fonts
        self.pop_up_name_label.configure(font=medium_font)
        self.pop_up_name_entry.configure(font=normal_font)
        self.confirm_button.configure(font=normal_font)
        self.cancel_button.configure(font=normal_font)

    def change_self_color(self):
        #Change the color and then reset
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def confirm(self):
        #Confirm the template name
        temp_name = self.pop_up_name_entry.get()
        if (folder / "{}.py".format(temp_name)).exists():
            showinfo("Template Name Error", "A Template Naming Error Has Occurred\n\nTemplate Name Already Exists")
        else:
            if (temp_name != "") and (temp_name != " "):
                with open(folder / "{}.py".format(temp_name), "w") as f:
                    f.write(self.text_info)
                    f.close()
                showinfo("Template Created", "Template Created\n\nTemplate Has Been Created")
                self.pop_up_window.destroy()
                self.destroy()
            else:
                showwarning("Template Name Error", "A Template Naming Error Has Occurred\n\nTemplate Name Cannot be Blank")

    def cancel(self):
        #Cancel the template creation
        global temp_name
        temp_name = None
        self.pop_up_window.destroy()
        self.destroy()

#Create template classes
class temp_open_pop_up(Frame):
    def __init__(self, *args, **kwargs):
        #Get necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.text = kwargs.pop("text")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create Frame
        Frame.__init__(self, *args, **kwargs)
        #Create colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.temp_open_pop_up_window = Toplevel()
        self.temp_open_pop_up_window.title("Template Selection")
        self.temp_open_pop_up_window.config(bg=bg)
        self.temp_open_pop_up_window.geometry("400x300+{}+{}".format(self.x, self.y))
        self.temp_open_pop_up_window.resizable(width=False, height=False)
        self.temp_open_pop_up_window.attributes("-topmost", True)
        self.templates_start_list = listdir(folder)
        self.templates_list = []
        for file in self.templates_start_list:
            if file.endswith(".py"):
                self.templates_list.append(file)
        self.templates_list.sort()
        self.temp_open_pop_up_label = Label(self.temp_open_pop_up_window, text="Select a template:", font=medium_font)
        self.temp_open_pop_up_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.temp_open_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_open_pop_up_listbox = Listbox(self.temp_open_pop_up_window, width=30, height=10)
        self.temp_open_pop_up_listbox.place(relx=.5, rely=.5, anchor=CENTER)
        self.temp_open_pop_up_listbox.configure(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
        for item in self.templates_list:
            item = item.split(".py")[0]
            self.temp_open_pop_up_listbox.insert(END, item)
        self.temp_open_pop_up_listbox.bind("<Double-Button-1>", self.confirm)
        self.export_img = PhotoImage(file=str(folder / "export_template.png"))
        self.export_button = Button(self.temp_open_pop_up_window, image=self.export_img, command=self.export_template)
        self.export_button.place(relx=.5, rely=.9, anchor=CENTER)
        self.export_button.configure( highlightbackground=bg)
        ToolTip(self.export_button, text="Export Template", window=self.temp_open_pop_up_window)
        self.confirm_button = Button(self.temp_open_pop_up_window, text="Confirm", font=normal_font, command=self.confirm)
        self.confirm_button.pack(anchor=S, side=LEFT)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.temp_open_pop_up_window, text="Cancel", font=normal_font, command=self.cancel)
        self.cancel_button.pack(anchor=S, side=RIGHT)
        self.cancel_button.configure(highlightbackground=bg)
        self.temp_open_pop_up_window.protocol("WM_DELETE_WINDOW", self.cancel)

    def reset_color(self):
        #Reset colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.temp_open_pop_up_window.config(bg=bg)
        self.temp_open_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_open_pop_up_listbox.configure(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
        self.export_button.configure(highlightbackground=bg)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button.configure(highlightbackground=bg)
        #Update fonts
        self.temp_open_pop_up_label.config(font=medium_font)
        self.temp_open_pop_up_listbox.config(font=normal_font)
        self.confirm_button.config(font=normal_font)
        self.cancel_button.config(font=normal_font)

    def change_self_color(self):
        #Change colors
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def export_template(self):
        #Allow the user to export the template
        self.file_chosen = self.temp_open_pop_up_listbox.get(ANCHOR) + ".py"
        if self.file_chosen != ".py":
            file_path = asksaveasfile(initialfile=self.file_chosen, defaultextension=".py", filetypes=[("Python Files", "*.py")], initialdir="/")
            if file_path is not None:
                with open(folder / self.file_chosen, "r") as f:
                    self.contents = f.read()
                with open(file_path.name, "w") as f:
                    f.write(self.contents)
                    f.close()
                showinfo("Template Exported", "Template Exported")
            else:
                showwarning("Template Export Error", "Template Export Could Not Be Completed\n\nNo Path Was Chosen")
        else:
            showwarning("Export Error", "No Template Selected\n\nPlease Select A Template To Export")

    def confirm(self):
        #Confirm the template selection
        self.file_chosen = self.temp_open_pop_up_listbox.get(ANCHOR) + ".py"
        if self.file_chosen != ".py":
            with open(folder / self.file_chosen, "r") as f:
                self.text.text.insert("insert", f.read())
                f.close()
            self.text.redraw()
            self.temp_open_pop_up_window.destroy()
        else:
            showwarning("Template Error", "Template Could Not Be Opened\n\nNo Template Selected")
            self.temp_open_pop_up_window.destroy()

    def cancel(self):
        #Cancel the template selection
        self.temp_open_pop_up_window.destroy()
        self.destroy()

class temp_destroy_pop_up(Frame):
    def __init__(self, **kwargs):
        #Get necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create Frame
        Frame.__init__(self, **kwargs)
        #Initialize window
        self.temp_destroy_pop_up_window = Toplevel()
        self.temp_destroy_pop_up_window.title("Template Selection")
        self.temp_destroy_pop_up_window.config(bg=bg)
        self.temp_destroy_pop_up_window.geometry("400x300+{}+{}".format(self.x, self.y))
        self.temp_destroy_pop_up_window.resizable(width=False, height=False)
        self.temp_destroy_pop_up_window.attributes("-topmost", True)
        self.templates_start_list = listdir(folder)
        self.templates_list = []
        for file in self.templates_start_list:
            if file.endswith(".py"):
                self.templates_list.append(file)
        self.templates_list.sort()
        self.temp_destroy_pop_up_label = Label(self.temp_destroy_pop_up_window, text="Select a template:", font=medium_font)
        self.temp_destroy_pop_up_label.place(relx=.5, rely=.1, anchor=CENTER)
        self.temp_destroy_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_destroy_pop_up_listbox = Listbox(self.temp_destroy_pop_up_window, width=30, height=10)
        self.temp_destroy_pop_up_listbox.place(relx=.5, rely=.5, anchor=CENTER)
        self.temp_destroy_pop_up_listbox.configure(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
        for item in self.templates_list:
            item = item.split(".py")[0]
            self.temp_destroy_pop_up_listbox.insert(END, item)
        self.temp_destroy_pop_up_listbox.bind("<Double-Button-1>", self.confirm)
        self.confirm_button = Button(self.temp_destroy_pop_up_window, text="Confirm", font=normal_font, command=self.confirm)
        self.confirm_button.place(relx=.1, rely=.95, anchor=CENTER)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button = Button(self.temp_destroy_pop_up_window, text="Cancel", font=normal_font, command=self.cancel)
        self.cancel_button.place(relx=.9, rely=.95, anchor=CENTER)
        self.cancel_button.configure(highlightbackground=bg)
        self.temp_destroy_pop_up_window.protocol("WM_DELETE_WINDOW", self.cancel)

    def reset_color(self):
        #Change colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Change colors
        self.temp_destroy_pop_up_window.configure(bg=bg)
        self.temp_destroy_pop_up_label.configure(bg=bg, fg=fg)
        self.temp_destroy_pop_up_listbox.configure(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
        self.confirm_button.configure(highlightbackground=bg)
        self.cancel_button.configure(highlightbackground=bg)
        #Update fonts
        self.temp_destroy_pop_up_label.configure(font=medium_font)
        self.confirm_button.configure(font=normal_font)
        self.cancel_button.configure(font=normal_font)
        
    def change_self_color(self):
            #Change color_mode and then call the reset_color function
            if self.color_mode == "Dark":
                self.color_mode = "light"
            else:
                self.color_mode = "Dark"
            self.reset_color()

    def confirm(self, event=None):
        #Confirm the template selection
        confirmation = askyesno("Confirmation", "File Deletion Confirmation\n\nAre You Sure You Want To Delete This Template?")
        if confirmation == True:
            self.file_chosen = self.temp_destroy_pop_up_listbox.get(ANCHOR) + ".py"
            if self.file_chosen != ".py":
                os.remove(folder / self.file_chosen)
                showinfo("Template Deleted", "Template Deleted\n\nTemplate Has Been Beleted")
                self.temp_destroy_pop_up_window.destroy()
            else:
                showwarning("Template Error", "Template Could Not Be Deleted\n\nNo Template Selected")

    def cancel(self):
        #Cancel the template selection
        self.temp_destroy_pop_up_window.destroy()
        self.destroy()

#Create settings class
class settings(Frame):
    def __init__(self, *args, **kwargs):
        #Get necessary variables
        self.window = kwargs.pop("window")
        self.function = kwargs.pop("function")
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create Frame
        Frame.__init__(self, *args, **kwargs)
        #Create window
        self.settings_window = Toplevel()
        #Create colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.settings_window.configure(background=bg)
        self.settings_window.title("Settings")
        self.settings_window.geometry("375x450+{}+{}".format(self.x, self.y))
        self.settings_window.resizable(width=False, height=False)
        self.settings_window.attributes("-topmost", True)
        self.settings_window_main_label = Label(self.settings_window, text="Settings", font=large_font)
        self.settings_window_main_label.place(relx=.5, rely=.075, anchor=CENTER)
        self.settings_window_main_label.configure(bg=bg, fg=fg)
        # tag_comment 
        # tag_keyword 
        # tag_builtin 
        # tag_string
        # tag_definition
        # tag_class
        self.my_group_color_changer_button = Button(self.settings_window, text="MYGROUP Color Picker", font=medium_font, width=22, command=self.my_group_color_changer)
        self.my_group_color_changer_button.place(relx=.5, rely=.15, anchor=CENTER)
        self.my_group_color_changer_button.configure(highlightbackground=bg)
        self.comment_color_changer_button = Button(self.settings_window, text="COMMENT Color Picker", font=medium_font, width=22, command=self.comment_color_changer)
        self.comment_color_changer_button.place(relx=.5, rely=.23055, anchor=CENTER)
        self.comment_color_changer_button.configure(highlightbackground=bg)
        self.keyword_color_changer_button = Button(self.settings_window, text="KEYWORD Color Picker", font=medium_font, width=22, command=self.keyword_color_changer)
        self.keyword_color_changer_button.place(relx=.5, rely=.3111, anchor=CENTER)
        self.keyword_color_changer_button.configure(highlightbackground=bg)
        self.builtin_color_changer_button = Button(self.settings_window, text="BUILTIN Color Picker", font=medium_font, width=22, command=self.builtin_color_changer)
        self.builtin_color_changer_button.place(relx=.5, rely=.39165, anchor=CENTER)
        self.builtin_color_changer_button.configure(highlightbackground=bg)
        self.string_color_changer_button = Button(self.settings_window, text="STRING Color Picker", font=medium_font, width=22, command=self.string_color_changer)
        self.string_color_changer_button.place(relx=.5, rely=.4722, anchor=CENTER)
        self.string_color_changer_button.configure(highlightbackground=bg)
        self.definition_color_changer_button = Button(self.settings_window, text="DEFINITION Color Picker", font=medium_font, width=22, command=self.definition_color_changer)
        self.definition_color_changer_button.place(relx=.5, rely=.55275, anchor=CENTER)
        self.definition_color_changer_button.configure(highlightbackground=bg)
        self.class_color_changer_button = Button(self.settings_window, text="CLASS Color Picker", font=medium_font, width=22, command=self.class_color_changer)
        self.class_color_changer_button.place(relx=.5, rely=.6333, anchor=CENTER)
        self.class_color_changer_button.configure(highlightbackground=bg)
        self.keyword_changer_button = Button(self.settings_window, text="Keyword Changer", font=medium_font, width=22, command=self.keyword_changer)
        self.keyword_changer_button.place(relx=.5, rely=.71385, anchor=CENTER)
        self.keyword_changer_button.configure(highlightbackground=bg)
        #import keywords.txt button
        #export keywords.txt button
        self.import_keywords_button = Button(self.settings_window, text="Import Keywords", font=medium_font, width=22, command=self.import_keywords)
        self.import_keywords_button.place(relx=.5, rely=.7944, anchor=CENTER)
        self.import_keywords_button.configure(highlightbackground=bg)
        self.export_keywords_button = Button(self.settings_window, text="Export Keywords", font=medium_font, width=22, command=self.export_keywords)
        self.export_keywords_button.place(relx=.5, rely=.87495, anchor=CENTER)
        self.export_keywords_button.configure(highlightbackground=bg)
        self.quit_button = Button(self.settings_window, text="Quit", font=normal_font, command=self.quit)
        self.quit_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.quit_button.configure(highlightbackground=bg)
        self.settings_window.protocol("WM_DELETE_WINDOW", self.quit)

    def reset_color(self):
        #Reset colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.settings_window.configure(background=bg)
        self.settings_window_main_label.configure(bg=bg, fg=fg)
        self.my_group_color_changer_button.configure(highlightbackground=bg)
        self.comment_color_changer_button.configure(highlightbackground=bg)
        self.keyword_color_changer_button.configure(highlightbackground=bg)
        self.builtin_color_changer_button.configure(highlightbackground=bg)
        self.string_color_changer_button.configure(highlightbackground=bg)
        self.definition_color_changer_button.configure(highlightbackground=bg)
        self.class_color_changer_button.configure(highlightbackground=bg)
        self.keyword_changer_button.configure(highlightbackground=bg)
        self.import_keywords_button.configure(highlightbackground=bg)
        self.export_keywords_button.configure(highlightbackground=bg)
        self.quit_button.configure(highlightbackground=bg)
        #Update fonts
        self.settings_window_main_label.configure(font=large_font)
        self.my_group_color_changer_button.configure(font=medium_font)
        self.comment_color_changer_button.configure(font=medium_font)
        self.keyword_color_changer_button.configure(font=medium_font)
        self.builtin_color_changer_button.configure(font=medium_font)
        self.string_color_changer_button.configure(font=medium_font)
        self.definition_color_changer_button.configure(font=medium_font)
        self.class_color_changer_button.configure(font=medium_font)
        self.keyword_changer_button.configure(font=medium_font)
        self.import_keywords_button.configure(font=medium_font)
        self.export_keywords_button.configure(font=medium_font)
        self.quit_button.configure(font=normal_font)

    def change_self_color(self):
        #Change color_mode and then reset colors
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def import_keywords(self):
        #Allow user to import keywords
        global keywords_list
        #Get the file path
        file_path = askopenfilename(initialdir="/", filetypes=([("Text files", "*.txt")]))
        #Check that the file path is not empty and the name is keywords.txt
        if file_path != "":
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
        #Allow user to export keywords
        file_path = asksaveasfilename(initialdir="/", filetypes=([("Text files", "*.txt")]))
        if file_path != "":
            #open the file
            with open(file_path, "w") as file:
                #write the keywords to the file
                for keyword in keywords_list:
                    file.write(keyword + "\n")

    def color_changer(self, index):
        #Allow user to change the color of the selected tag
        color = colorchooser.askcolor()
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
            self.function()
            showinfo("Syntax Color Reset Successful", "Syntax Color Reset Successful\n\nThe Syntax Highlighting Has Been Reset", parent=self.settings_window)

    def my_group_color_changer(self):
        #Allow user to change the color of the my group tag
        self.color_changer(0)

    def comment_color_changer(self):
        #Allow user to change the color of the comment tag
        self.color_changer(1)

    def keyword_color_changer(self):
        #Allow user to change the color of the keyword tag
        self.color_changer(2)

    def builtin_color_changer(self):
        #Allow user to change the color of the builtin tag
        self.color_changer(3)

    def string_color_changer(self):
        #Allow user to change the color of the string tag
        self.color_changer(4)

    def definition_color_changer(self):
        #Allow user to change the color of the definition tag
        self.color_changer(5)

    def class_color_changer(self):
        #Allow user to change the color of the class tag
        self.color_changer(6)

    def quit(self):
        #Close the settings window
        self.settings_window.destroy()
        self.destroy()

    def keyword_changer(self):
        #Open the keyword changer window
        keyword_change_page(color_mode = self.color_mode, x=self.window.winfo_x(), y=self.window.winfo_y())

#Create the bug report window
class report_bug(Frame):
    def __init__(self, *args, **kwargs):
        #Retrieve the necessary arguments
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create the frame
        Frame.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create the window
        self.report_bug_window = Toplevel()
        self.report_bug_window.configure(background=bg)
        self.report_bug_window.title("Report Bug")
        self.report_bug_window.geometry("410x350+{}+{}".format(self.x, self.y))
        self.report_bug_window.resizable(width=False, height=False)
        self.report_bug_window.attributes("-topmost", True)
        self.report_bug_window_main_label = Label(self.report_bug_window, text="Report Bug", font=large_font)
        self.report_bug_window_main_label.place(relx=.5, rely=.075, anchor=CENTER)
        self.report_bug_window_main_label.configure(bg=bg, fg=fg)
        self.report_bug_window_text_label = Label(self.report_bug_window, text="Subject:", font=normal_font)
        self.report_bug_window_text_label.place(relx=.5, rely=.175, anchor=CENTER)
        self.report_bug_window_text_label.configure(bg=bg, fg=fg)
        self.subject_entry = Entry(self.report_bug_window, borderwidth=3, relief=SUNKEN, width=40, justify=CENTER, font=normal_font)
        self.subject_entry.place(relx=.5, rely=.25, anchor=CENTER)
        self.subject_entry.configure(bg=bg, insertbackground=fg, fg=fg)
        self.message_text_label = Label(self.report_bug_window, text="Message:", font=normal_font)
        self.message_text_label.place(relx=.5, rely=.33, anchor=CENTER)
        self.message_text_label.configure(bg=bg, fg=fg)
        self.message_text = Text(self.report_bug_window, borderwidth=3, relief=SUNKEN, width=40, height=8.25, font=normal_font)
        self.message_text.place(relx=.5, rely=.6, anchor=CENTER)
        self.message_text.configure(bg=bg, insertbackground=fg, fg=fg)
        # self.message_text.insert(END, "This is meant for:\nA) A bug in the program\nB) A feature request\nC) A suggestion\n\nIf this is a bug report please give as much detail as possible and include the steps to reproduce the bug")
        self.report_bug_button = Button(self.report_bug_window, text="Report Bug", font=normal_font, command=self.report_bug)
        self.report_bug_button.place(relx=.5, rely=.875, anchor=CENTER)
        self.report_bug_button.configure(highlightbackground=bg)
        self.quit_button = Button(self.report_bug_window, text="Quit", font=normal_font, command=self.quit)
        self.quit_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.quit_button.configure(highlightbackground=bg)
        self.report_bug_window.protocol("WM_DELETE_WINDOW", self.quit)

    def reset_color(self):
        #Reset the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.report_bug_window.configure(background=bg)
        self.report_bug_window_main_label.configure(bg=bg, fg=fg)
        self.report_bug_window_text_label.configure(bg=bg, fg=fg)
        self.subject_entry.configure(bg=bg, insertbackground=fg, fg=fg)
        self.message_text_label.configure(bg=bg, fg=fg)
        self.message_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.report_bug_button.configure(highlightbackground=bg)
        self.quit_button.configure(highlightbackground=bg)
        #Update fonts
        self.report_bug_window_main_label.configure(font=large_font)
        self.report_bug_window_text_label.configure(font=normal_font)
        self.subject_entry.configure(font=normal_font)
        self.message_text_label.configure(font=normal_font)
        self.message_text.configure(font=normal_font)
        self.report_bug_button.configure(font=normal_font)
        self.quit_button.configure(font=normal_font)

    def change_self_color(self):
        #Change color_mode and then reset the colors
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def report_bug(self):
        #Send the bug report
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
        #Close the report bug window
        self.report_bug_window.destroy()
        self.destroy()

#Create the help window
class help_info(Frame):
    def __init__(self, *args, **kwargs):
        #Retrieve the necessary arguments
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create the frame
        Frame.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create the window
        self.help_info_window = Toplevel()
        self.help_info_window.title("Help")
        self.help_info_window.geometry("400x400+{}+{}".format(self.x, self.y))
        self.help_info_window.configure(background=bg)
        self.help_info_window.resizable(width=False, height=False)
        self.help_info_window.attributes("-topmost", True)
        self.help_info_window_main_label = Label(self.help_info_window, text="Help", font=large_font)
        self.help_info_window_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.help_info_window_main_label.configure(bg=bg, fg=fg)
        self.info_text = Text(self.help_info_window, borderwidth=3, relief=SUNKEN, width=40, height=18, font=normal_font)
        self.info_text.insert("1.0", "- Clear-CMD: Clears the terminal\n- StackOverflow: Opens StackOverflow\n- Create-Temp: Creates template\n- Open-Temp: Opens template\n- Delete-Temp: Deletes template")
        self.info_text.config(state=DISABLED)
        self.info_text.place(relx=.5, rely=.5, anchor=CENTER)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button = Button(self.help_info_window, text="Ok", font=normal_font, command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)
        self.help_info_window.protocol("WM_DELETE_WINDOW", self.ok)

    def reset_color(self):
        #Reset the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.help_info_window.configure(background=bg)
        self.help_info_window_main_label.configure(bg=bg, fg=fg)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button.configure(highlightbackground=bg)
        #Update fonts
        self.help_info_window_main_label.configure(font=large_font)
        self.info_text.configure(font=normal_font)
        self.ok_button.configure(font=normal_font)

    def change_self_color(self):
        #Change color_mode and then reset the colors
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def ok(self):
        #Close the help window
        self.help_info_window.destroy()
        self.destroy()

#Create the shortcut window
class shortcuts_page(Frame):
    def __init__(self, *args, **kwargs):
        #Retrieve the necessary arguments
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create the frame
        Frame.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create the window
        self.shortcuts_page_window = Toplevel()
        self.shortcuts_page_window.title("Shortcuts")
        self.shortcuts_page_window.geometry("400x400+{}+{}".format(self.x, self.y))
        self.shortcuts_page_window.configure(background=bg)
        self.shortcuts_page_window.resizable(width=False, height=False)
        self.shortcuts_page_window.attributes("-topmost", True)
        self.shortcuts_page_main_label = Label(self.shortcuts_page_window, text="Shortcuts", font=large_font)
        self.shortcuts_page_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.shortcuts_page_main_label.configure(bg=bg, fg=fg)
        self.info_text = Text(self.shortcuts_page_window, borderwidth=3, relief=SUNKEN, width=50, height=20)
        self.info_text.insert("1.0", "- Command + t: Creates a new tab\n- Command + O: Opens a file\n- Command + S: Saves a file\n- Command + F: Find and replace\n- Command + R / F5: Runs file\n- Command + /: Turns line(s) into comment(s)\n- Shift + Tab: Unindents line\n- Command + Shift + K: Deletes line\n- F1: Help menu\n- Command + B: Adds breakpoint to next line")
        self.info_text.config(state=DISABLED)
        self.info_text.place(relx=.5, rely=.5, anchor=CENTER)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button = Button(self.shortcuts_page_window, text="Ok", font=normal_font, command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)
        self.shortcuts_page_window.protocol("WM_DELETE_WINDOW", self.ok)

    def reset_color(self):
        #Reset the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Reset the window
        self.shortcuts_page_window.configure(background=bg)
        self.shortcuts_page_main_label.configure(bg=bg, fg=fg)
        self.info_text.configure(bg=bg, insertbackground=fg, fg=fg)
        self.ok_button.configure(highlightbackground=bg)
        #Update fonts
        self.shortcuts_page_main_label.configure(font=large_font)
        self.info_text.configure(font=normal_font)
        self.ok_button.configure(font=normal_font)

    def change_self_color(self):
        #Change the colors
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        #Call the reset color function
        self.reset_color()

    def ok(self):
        #Close the shortcuts window
        self.shortcuts_page_window.destroy()
        self.destroy()

#Create the keyword change window
class keyword_change_page(Frame):
    def __init__(self, *args, **kwargs):
        #Retrieve the necessary arguments
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        #Create the frame
        Frame.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.keyword_change_page_window = Toplevel()
        self.keyword_change_page_window.title("Keyword Change")
        self.keyword_change_page_window.geometry("400x500+{}+{}".format(self.x, self.y))
        self.keyword_change_page_window.configure(background=bg)
        self.keyword_change_page_window.resizable(width=False, height=False)
        self.keyword_change_page_window.attributes("-topmost", True)
        self.keyword_change_page_main_label = Label(self.keyword_change_page_window, text="Keyword Change", font=large_font)
        self.keyword_change_page_main_label.place(relx=.5, rely=.055, anchor=CENTER)
        self.keyword_change_page_main_label.configure(bg=bg, fg=fg)
        self.keyword_listbox = Listbox(self.keyword_change_page_window, width=30, height=10)
        self.keyword_listbox.place(relx=.5, rely=.325, anchor=CENTER)
        self.keyword_listbox.configure(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
        for item in keywords_list:
            self.keyword_listbox.insert(END, item)
        self.add_entry = Entry(self.keyword_change_page_window, width=30, borderwidth=3, relief=SUNKEN, justify=CENTER, font=normal_font)
        self.add_entry.place(relx=.5, rely=.525, anchor=CENTER)
        self.add_entry.configure(bg=bg, fg=fg, insertbackground=fg)
        self.add_button = Button(self.keyword_change_page_window, text="Add Item", font=normal_font, width=15, command=self.add)
        self.add_button.place(relx=.5, rely=.5786, anchor=CENTER)
        self.add_button.configure(highlightbackground=bg)
        self.remove_button = Button(self.keyword_change_page_window, text="Remove Item", font=normal_font, width=15, command=self.remove)
        self.remove_button.place(relx=.5, rely=.6322, anchor=CENTER)
        self.remove_button.configure(highlightbackground=bg)
        self.move_up_button = Button(self.keyword_change_page_window, text="Move Up", font=normal_font, width=15, command=self.move_up)
        self.move_up_button.place(relx=.5, rely=.6858, anchor=CENTER)
        self.move_up_button.configure(highlightbackground=bg)
        self.move_to_top_button = Button(self.keyword_change_page_window, text="Move to Top", font=normal_font, width=15, command=self.move_to_top)
        self.move_to_top_button.place(relx=.5, rely=.7394, anchor=CENTER)
        self.move_down_button = Button(self.keyword_change_page_window, text="Move Down", font=normal_font, width=15, command=self.move_down)
        self.move_down_button.place(relx=.5, rely=.793, anchor=CENTER)
        self.move_down_button.configure(highlightbackground=bg)
        self.move_to_bottom_button = Button(self.keyword_change_page_window, text="Move to Bottom", font=normal_font, width=15, command=self.move_to_bottom)
        self.move_to_bottom_button.place(relx=.5, rely=.8466, anchor=CENTER)
        self.move_to_middle_button = Button(self.keyword_change_page_window, text="Move to Middle", font=normal_font, width=15, command=self.move_to_middle)
        self.move_to_middle_button.place(relx=.5, rely=.9002, anchor=CENTER)
        self.move_to_middle_button.configure(highlightbackground=bg)
        self.ok_button = Button(self.keyword_change_page_window, text="Ok", font=normal_font, command=self.ok)
        self.ok_button.place(relx=.5, rely=.95, anchor=CENTER)
        self.ok_button.configure(highlightbackground=bg)
        self.keyword_change_page_window.protocol("WM_DELETE_WINDOW", self.ok)

    def reset_color(self):
        #Reset the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.keyword_change_page_window.configure(background=bg)
        self.keyword_change_page_main_label.configure(bg=bg, fg=fg)
        self.keyword_listbox.configure(bg=bg, fg=fg, selectbackground=bg, selectforeground=fg)
        self.add_entry.configure(bg=bg, fg=fg, insertbackground=fg)
        self.add_button.configure(highlightbackground=bg)
        self.remove_button.configure(highlightbackground=bg)
        self.move_up_button.configure(highlightbackground=bg)
        self.move_to_top_button.configure(highlightbackground=bg)
        self.move_down_button.configure(highlightbackground=bg)
        self.move_to_bottom_button.configure(highlightbackground=bg)
        self.move_to_middle_button.configure(highlightbackground=bg)
        self.ok_button.configure(highlightbackground=bg)
        #Update fonts
        self.keyword_change_page_main_label.configure(font=large_font)
        self.add_entry.configure(font=normal_font)
        self.add_button.configure(font=normal_font)
        self.remove_button.configure(font=normal_font)
        self.move_up_button.configure(font=normal_font)
        self.move_to_top_button.configure(font=normal_font)
        self.move_down_button.configure(font=normal_font)
        self.move_to_bottom_button.configure(font=normal_font)
        self.move_to_middle_button.configure(font=normal_font)
        self.ok_button.configure(font=normal_font)

    def change_self_color(self):
        #Change the colors and then call the reset_color function
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def add(self):
        #Add the item to the list
        if self.add_entry.get() != "":
            if " " not in self.add_entry.get():
                keywords_list.append(self.add_entry.get())
                update_list()
                self.keyword_listbox.insert(END, self.add_entry.get())
                self.add_entry.delete(0, END)
            else:
                showwarning("Error Found", "Keyword Insertion Error\n\nNo Spaces Allowed in Keyword")
        else:
            showwarning("Error Found", "Keyword Insertion Error\n\nPlease Enter A Keyword")

    def remove(self):
        #Remove the item from the list
        if self.keyword_listbox.curselection() != ():
            self.keyword_listbox.delete(self.keyword_listbox.curselection())
            keywords_list.remove(keywords_list[self.keyword_listbox.curselection()[0]])
            update_list()


    def move_up(self):
        #Move the item up in the list
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
        #Move the item to the top of the list
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
        #Move the item down in the list
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
        #Move the item to the bottom of the list
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
        #Move the item to the middle of the list
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
        #Close the window
        self.keyword_change_page_window.destroy()
        self.destroy()

#Create the extension class
class extension_page(Frame):
    def __init__(self, master, *args, **kwargs):
        #Retrieve the arguments
        self.reset_function = kwargs.pop("reset")
        self.text_boxes = kwargs.pop("text_boxes")
        self.function = kwargs.pop("function")
        self.change_color = kwargs.pop("change_color")
        self.color_mode = kwargs.pop("color_mode")
        self.x = kwargs.pop("x")
        self.y = kwargs.pop("y")
        self.window = master
        #Create the frame
        Frame.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create the window
        self.extension_page_window = Toplevel()
        self.extension_page_window.geometry("+{}+{}".format(self.x, self.y))
        self.extension_page_window.resizable(False, False)
        self.extension_page_window.title("Extensions")
        self.extension_page_window.attributes("-topmost", True)
        self.extensions_list = []
        #get extensions from extensions folder
        try:
            for file in get_list_items():
                file = file.split("/")[-1]
                if file.endswith(".xt"):
                    self.extensions_list.append(str(file).split(".")[0])
            self.extensions_list.sort()
            self.extension_page_window.configure(bg=bg)
            #Delete Josh's Choice Bundle from list
            self.extensions_list.remove("Josh's Choice Bundle")
            #Set to front
            self.extensions_list.insert(0, "Josh's Choice Bundle")
            #Put Defualt to front of list
            #Delete Default from list
            self.extensions_list.remove("Default")
            #Set to front
            self.extensions_list.insert(0, "Default")
            #Put Defualt to front of list
            self.search_var = StringVar()
            self.search_var.trace("w", self.update_listbox)
            self.searchbox = Entry(self.extension_page_window, textvariable=self.search_var, font=normal_font, relief=SUNKEN, borderwidth=3, justify=CENTER)
            self.searchbox.pack(fill=X, expand=False)
            self.searchbox.config(background=bg, foreground=fg, insertbackground=bg)
            self.extensions_listbox = Listbox(self.extension_page_window, font=normal_font, relief=SUNKEN, borderwidth=3, width=50, height=20)
            self.extensions_listbox.pack(fill=X)
            self.extensions_listbox.config(bg=bg, selectbackground=bg, selectforeground=fg, fg=fg)
            self.extensions_listbox.bind("<Double-Button-1>", self.inspect_extension)
            for extension in self.extensions_list:
                self.extensions_listbox.insert(END, extension)
            self.update_listbox()
            self.inpect_extension_button = Button(self.extension_page_window, text="Inspect Extension", command=self.inspect_extension, font=normal_font, relief=SUNKEN, width=20)
            self.inpect_extension_button.pack()
            self.inpect_extension_button.config(highlightbackground=bg)
            self.use_extension_button = Button(self.extension_page_window, text="Use Extension", command=self.use_extension, font=normal_font, relief=SUNKEN, width=20)
            self.use_extension_button.pack()
            self.use_extension_button.config(highlightbackground=bg)
            self.cancel_button = Button(self.extension_page_window, text="Cancel", command=self.cancel, font=normal_font, relief=SUNKEN, width=20)
            self.cancel_button.pack()
            self.cancel_button.config(highlightbackground=bg)
            self.extension_page_window.protocol("WM_DELETE_WINDOW", self.cancel)
        except:
            showwarning("Extension Error", "An Extension Loading Error Has Occured. Could Not Connect To The Extension Server\n\nPlease Try Again Later")
            self.extension_page_window.destroy()
            self.destroy()

    def update_listbox(self, *args):
        #Update the listbox
        search_term = self.search_var.get()
        self.extensions_listbox.delete(0, END)
        for item in self.extensions_list:
            if search_term.lower() in item.lower():
                self.extensions_listbox.insert(END, item)

    def reset_color(self):
        #Reset colors of all widgets to match the color mode
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.extension_page_window.configure(bg=bg)
        self.searchbox.config(background=bg, foreground=fg, insertbackground=bg)
        self.extensions_listbox.config(background=bg, foreground=fg, selectbackground=bg, selectforeground=fg)
        self.inpect_extension_button.config(highlightbackground=bg)
        self.use_extension_button.config(highlightbackground=bg)
        self.cancel_button.config(highlightbackground=bg)
        #Update fonts
        self.searchbox.config(font=normal_font)
        self.extensions_listbox.config(font=normal_font)
        self.inpect_extension_button.config(font=normal_font)
        self.use_extension_button.config(font=normal_font)
        self.cancel_button.config(font=normal_font)

    def change_self_color(self):
        #Change the color
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def inspect_extension(self, event=None):
        #Inspect the extension
        if self.extensions_listbox.get(ANCHOR) != "":
            extension = self.extensions_listbox.get(ANCHOR)
            try:
                self.function(extension)
                # self.extension_page_window.destroy()
            except:
                showwarning("Extension Error", "An Extension Loading Error Has Occured. Could Not Connect To The Extension Server\n\nPlease Try Again Later")
        else:
            showwarning("Extension Inspection Error", "An Extension Inspection Error Occurred\n\nPlease Select An Extension To Inspect")

    def use_extension(self):
        #Use the extension
        if self.extensions_listbox.get(ANCHOR) != "":
            try:
                extension = self.extensions_listbox.get(ANCHOR)
                details = open_extension("https://jde-org.github.io/extensions/{}.xt".format(extension))
                the_keywords = details[5]
                if the_keywords != None or "":
                    keywords = ""
                    for keyword in the_keywords:
                        keywords += keyword + "\n"
                    #Remove the last newline
                    keywords = keywords[:-1]
                    #Update folder / keywords.txt
                    with open(folder / "keywords.txt", "w") as f:
                        f.write(keywords)
                else:
                    keywords = None
                the_settings = details[6]
                if the_settings != None or "":
                    settings = ""
                    for setting in the_settings:
                        settings += setting + "\n"
                    #Remove the last newline
                    settings = settings[:-1]
                    #Update folder / settings.txt
                    with open(folder / "settings.txt", "w") as settings_file:
                        settings_file.write(settings)
                    current_mode = settings.split("\n")[-1]
                    if current_mode == "light" and self.color_mode == "light":
                        self.change_color()
                        self.change_color()
                        self.change_self_color()
                        self.change_self_color()
                    elif current_mode == "light" and self.color_mode == "Dark":
                        self.change_color()
                        self.change_self_color()
                    elif current_mode == "Dark" and self.color_mode == "Dark":
                        self.change_color()
                        self.change_color()
                        self.change_self_color()
                        self.change_self_color()
                    elif current_mode == "Dark" and self.color_mode == "light":
                        self.change_color()
                        self.change_color()
                else:
                    settings = None
                the_theme = details[7]
                if the_theme != None or "":
                    the_theme = the_theme[0] + "\n" + the_theme[1]
                    #Update folder / color_theme.txt
                    with open(folder / "color_theme.txt", "w") as color_theme:
                        color_theme.write(the_theme)
                else:
                    the_theme = None
                the_font = details[8]
                if the_font != None or "":
                    family = the_font[0]
                    family = family.split(": ")[1]
                    normal = the_font[1]
                    normal = normal.split(": ")[1]
                    with open(folder / "dilate_size.txt", "w") as dilate_size:
                        dilate_size.truncate()
                        dilate_size.seek(0)
                        dilate_size.truncate()
                        dilate_size.seek(0)
                        dilate_size.write(normal)
                    med = the_font[2]
                    med = med.split(": ")[1]
                    large = the_font[3]
                    large = large.split(": ")[1]
                    min = the_font[4]
                    min = min.split(": ")[1]
                    max = the_font[5]
                    max = max.split(": ")[1]
                    string_font = family + "\n" + normal + "\n" + med + "\n" + large + "\n" + min + "\n" + max
                    #Update folder / font.txt
                    with open(folder / "font.txt", "w") as font_file:
                        font_file.write(string_font)
                for text_box in self.text_boxes:
                    text_box.redraw()
                get_info_from_files()
                self.reset_function()
                self.searchbox.config(font=normal_font)
                self.searchbox.update()
                self.extensions_listbox.config(font=normal_font)
                self.extensions_listbox.update()
                self.inpect_extension_button.config(font=normal_font)
                self.inpect_extension_button.update()
                self.use_extension_button.config(font=normal_font)
                self.use_extension_button.update()
                self.cancel_button.config(font=normal_font)
                self.cancel_button.update()
                showinfo("Extension Applied", "Extension Applied Successfully\n\nThe Extension: \"{}\" Has Succesfully Been Applied".format(extension), parent=self.extension_page_window)
                self.extension_page_window.destroy()
                self.destroy()
            except:
                showwarning("Extension Error", "An Extension Loading Error Has Occured. Could Not Connect To The Extension Server\n\nPlease Try Again Later", parent=self.extension_page_window)
    def cancel(self):
        #Cancel the extension
        self.extension_page_window.destroy()
        self.destroy()

#Make a loading screen
class loading(Frame):
    def __init__(self, *args, **kwargs):
        #Initialize the loading screen
        Frame.__init__(self, *args, **kwargs)
        self.window = Toplevel()
        self.window.geometry("+0+0")
        self.window.resizable(False, False)
        self.window.iconify()
        #Make window indestructable
        Label(self.window, text="Loading...", font=normal_font, bg="white").pack()
        self.window.title("Loading...")
        p = Progressbar(self.window, orient=HORIZONTAL, length=200, mode='indeterminate')
        p.pack()
        p.start()

    def show(self):
        #Show the loading screen
        self.window.deiconify()

    def cancel (self):
        #Cancel the loading screen
        self.window.destroy()

#Make a go to line popup
class go_to_line(Toplevel):
    def __init__(self, x, y, *args, **kwargs):
        #Retrieve the necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.text = kwargs.pop("text")
        #Initialize the go to line popup
        Toplevel.__init__(self, *args, **kwargs)
        #Create the colors
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Set attributes
        self.title("Go To Line")
        self.geometry("575x150+{}+{}".format(x, y))
        self.configure(background=bg)
        self.resizable(width=False, height=False)
        self.attributes("-topmost", True)
        self.main_label = Label(self, text="Go To Line", font=large_font, bg=bg, fg=fg)
        self.main_label.place(relx=0.5, rely=.125, anchor="center")
        self.warning_label = Label(self, text="Enter A Positive Integer:", font=normal_font, bg=bg, fg=fg)
        self.warning_label.place(relx=0.5, rely=.275, anchor="center")
        self.secondary_warning_label = Label(self, text="(Use Start To Go To Start Of File And End To Go To End Of File)", font=normal_font, bg=bg, fg=fg)
        self.secondary_warning_label.place(relx=0.5, rely=.425, anchor="center")
        self.line_entry = Entry(self, font=normal_font, bg=bg, fg=fg, width=30, justify=CENTER, insertbackground=fg)
        self.line_entry.place(relx=0.5, rely=.6, anchor="center")
        self.line_entry.focus_force()
        #Create ok and cancel buttons
        self.ok_button = Button(self, text="Ok", font=normal_font, command=self.ok, highlightbackground=bg)
        self.ok_button.place(relx=0.25, rely=.825, anchor="center")
        self.cancel_button = Button(self, text="Cancel", font=normal_font, command=self.cancel, highlightbackground=bg)
        self.cancel_button.place(relx=0.75, rely=.825, anchor="center")

    def reset_color(self):
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.configure(background=bg)
        self.main_label.configure(bg=bg, fg=fg) 
        self.warning_label.configure(bg=bg, fg=fg)
        self.secondary_warning_label.configure(bg=bg, fg=fg)
        self.line_entry.configure(bg=bg, fg=fg)
        self.ok_button.configure(bg=bg, fg=fg)
        self.cancel_button.configure(bg=bg, fg=fg)
        #Update fonts
        self.main_label.config(font=large_font)
        self.warning_label.config(font=normal_font)
        self.secondary_warning_label.config(font=normal_font)
        self.line_entry.config(font=normal_font)
        self.ok_button.config(font=normal_font)
        self.cancel_button.config(font=normal_font)

    def change_self_color(self):
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def ok(self):
        #Check if the line is a positive integer
        if self.line_entry.get().isdigit() or self.line_entry.get() == "Start" or self.line_entry.get() == "End":
            #Get the line
            line = self.line_entry.get()
            if line == "Start":
                line = 1
            elif line == "End":
                line = self.text.count("\n")
            else:
                line = int(line)
            #If it is, go to the line
            self.text.text.mark_set("insert", "{}.end".format(line))
            self.text.text.see(INSERT)
            self.text.redraw()
            showinfo("Go To Line", "Go To Line Succesful\n\nSuccessfully Went To Line {}".format(line), parent=self)
            self.destroy()
        else:
            #If it is not, show a warning
            self.line_entry.delete(0, END)
            showerror("Line Error", "Line Go To Error\n\nPlease Enter A Positive Integer", parent=self)

    def cancel(self):
        #Cancel the go to line popup
        self.destroy()

#Create ExtensionText widget class
class ExtensionText(Frame):
    def __init__(self, *args, **kwargs):
        #Get necessary arguments
        self.window = kwargs.pop("window")
        self.color_mode = kwargs.pop("color_mode")
        #Set up Frame
        Frame.__init__(self, *args, **kwargs)
        #Set up color_mode
        if self.color_mode == "Dark":
            fg = dark_mode_fg
            bg = dark_mode_bg
        else:
            fg = light_mode_fg
            bg = light_mode_bg

        update_dilate_size()
        self.text_font = (font_name, dilate_size)

        #Create base text widget
        if "height" and "width" in kwargs:
            self.text = Text(self, height=kwargs["height"], width=kwargs["width"], borderwidth=2, relief=RIDGE, wrap=NONE, undo=True, font=self.text_font)
        else:
            #, width=130, height=29
            self.text = Text(self, font=self.text_font, wrap="none", undo=True, borderwidth=2, relief=RIDGE, width=95, height=25)
        
        #Create scrollbar
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        #Create numberLines
        self.numberLines = TextLineNumbers(self, width=40)
        self.numberLines.attach(self.text)

        #Pack widgets
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.numberLines.pack(side=LEFT, fill=Y, padx=(5, 0))
        self.text.pack(side=RIGHT, fill=BOTH, expand=True)

        #Create bindings
        self.window.bind("<Any>", self.redraw())
        self.window.bind("<BackSpace>", lambda x: self.after(1, (self.redraw())), add=True)
        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        self.text.bind("<less>", self.double_less_than)
        self.text.bind(">", self.close_less_than)
        self.text.bind("<BackSpace>", self.closing_backspace, add=True)
        self.text.bind("<KeyRelease-Return>", self.redraw(), add=True)
        self.text.bind("<Command-Shift-k>", self.delete_line)
        self.text.bind("<Command-a>", self.select_all)

        self.text.configure(bg=bg, fg=fg, insertbackground=fg)
        self.numberLines.configure(bg=bg)

    def change_color(self):
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        if self.color_mode == "Dark":
            fg = dark_mode_fg
            bg = dark_mode_bg
        else:
            fg = light_mode_fg
            bg = light_mode_bg
        self.text_font = (font_name, dilate_size)
        self.text.configure(bg=bg, fg=fg, insertbackground=fg, font=self.text_font)
        self.numberLines.config(bg=bg)

    def select_all(self, event=None):
        line_count = self.text.index("end-1c").split(".")[0]
        for i in range(int(line_count)):
            self.text.tag_add("sel", "{}.0".format(i+1), "{}.end".format(i+1))
            if self.text.get("{}.0".format(i+1), "{}.end".format(i+1)) == "":
                self.text.insert("{}.0".format(i+1), " ")
            self.text.tag_add("sel", "{}.0".format(i+1), "{}.end".format(i+1))
        length_of_line = self.text.index("end-1c").split(".")[1]
        self.text.mark_set("insert", "{}.{}".format(line_count, length_of_line))
        self.text.see("insert")
        return "break"

    def increase_font(self, event=None):
        if int(self.text_font[1])+1 <= int(max):
            self.text_font = (self.text_font[0], int(self.text_font[1]) + 1)
            self.text.config(font=self.text_font)
            self.numberLines.redraw()

    def decrease_font(self, event=None):
        if int(self.text_font[1])-1 >= int(min):
            self.text_font = (self.text_font[0], int(self.text_font[1]) - 1)
            self.text.config(font=self.text_font)
            self.numberLines.redraw()

    def close_less_than(self, event=None):
        #Check if the > is being pressed in front of a > and then remove the > if it is
        try:
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents[current_position] == ">":
                new_line_contents = current_line_contents[:current_position] + current_line_contents[current_position+1:]
                self.text.delete("insert linestart", "insert lineend")
                self.text.insert("insert", new_line_contents)
                self.text.mark_set("insert", pos)
        except:
            pass

    def closing_backspace(self, event):
        #Check if the backspace is being pressed in front of a < and then remove the > if it is to the right
        try:
            # global insert_char
            pos = self.text.index("insert")
            current_position = int((self.text.index(INSERT)).split(".")[1])
            current_line_contents = self.text.get("insert linestart", "insert lineend")
            if current_line_contents != "":
                if current_line_contents[current_position-1] == "<":
                    special_char = current_line_contents[current_position-1]
                    if special_char == "<":
                        insert_char = ">"
                    #Remove previous char to the left and add a closing parenthesis if it is to the right
                    new_line_contents = current_line_contents[:current_position-1] + insert_char + current_line_contents[current_position:]
                    if new_line_contents[current_position] == insert_char:
                        new_line_contents = new_line_contents[:current_position] + new_line_contents[current_position+1:]
                    self.text.delete("insert linestart", "insert lineend")
                    self.text.insert("insert", new_line_contents)
                    self.text.mark_set("insert", pos)
        except:
            pass

    def delete_line(self, event=None):
        #Deletes the current line
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

    def make_find_and_replace(self, x, y, event=None, **kwargs):
        #Creates a find and replace window
        color_mode = kwargs.pop("color_mode")
        self.search_bar = search_text(self, x=x, y=y, color_mode = color_mode)
        self.search_bar.attach(self.text, self)
        self.search_bar.focus_set()

    def double_less_than(self, event):
        #Inserts back parentheses when < is pressed
        self_anchor = str(self.text.index("insert")).split(".")
        self.text.insert(INSERT, ">")
        self.text.mark_set(INSERT, str(self_anchor[0]) + "." + str(int(self_anchor[1])))
    
    def onScrollPress(self, *args):
        #Scrolls the text when mouse wheel is used
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        #Unbinds the scrollbar when mouse wheel is released
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        #Delays the execution of the onPress function
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        #Allowws for the use of get
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        #Allows for the use of insert
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        #Allows for the use of delete
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        #Allows for the use of index
        return self.text.index(*args, **kwargs)

    def redraw(self):
        #Redraws the text
        try:
            self.numberLines.redraw()
        except:
            pass

#Get extension name with ExtensionNamer class
class ExtensionNamer(Toplevel):
    def __init__(self, master, x, y, callback, color_mode="Dark", *args, **kwargs):
        #Set color mode
        self.color_mode = color_mode
        if self.color_mode == "Dark":
            self.bg = dark_mode_bg
            self.fg = dark_mode_fg
        else:
            self.bg = light_mode_bg
            self.fg = light_mode_fg
        #Initialize the window
        Toplevel.__init__(self, master, *args, **kwargs)
        self.callback = callback
        #Set basic window properties
        self.title("Extension Naming")
        self.geometry("300x100+{}+{}".format(x, y))
        self.attributes("-topmost", True)
        self.resizable(False, False)
        #Create the widgets
        self.extension_name_label = Label(self, text="Extension Name:", font=medium_font)
        self.extension_name_label.place(relx=0.5, rely=.15, anchor=CENTER)
        self.extension_name_entry = Entry(self, font=normal_font, width=20, justify=CENTER)
        self.extension_name_entry.place(relx=0.5, rely=.5, anchor=CENTER)
        self.confirm_button = Button(self, text="Confirm", font=normal_font, command=self.confirm)
        self.confirm_button.pack(anchor=S, side=LEFT)
        self.cancel_button = Button(self, text="Cancel", font=normal_font, command=self.cancel)
        self.cancel_button.pack(anchor=S, side=RIGHT)
        self.extension_name_label.config(bg=self.bg, fg=self.fg)
        self.extension_name_entry.config(bg=self.bg, fg=self.fg, insertbackground=self.fg)
        self.confirm_button.config(highlightbackground=self.bg)
        self.cancel_button.config(highlightbackground=self.bg)
        self.config(bg=self.bg)
        self.protocol("WM_DELETE_WINDOW", self.cancel)


    def reset_color(self):
        #Resets the color of the text
        self.extension_name_entry.config(fg=self.fg)
        self.extension_name_label.config(fg=self.fg)
        self.confirm_button.config(highlightbackground=light_mode_bg)
        self.cancel_button.config(highlightbackground=self.fg)
        self.config(bg=self.fg)
        #Reset fonts
        self.extension_name_label.config(font=medium_font)
        self.extension_name_entry.config(font=normal_font)
        self.confirm_button.config(font=normal_font)
        self.cancel_button.config(font=normal_font)

    def change_self_color(self):
        #Change color_mode and then reset color
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def confirm(self):
        #Confirm the extension name
        self.extension_name = self.extension_name_entry.get()
        if self.extension_name == "" or self.extension_name == " ":
            showerror("Extension Naming Error", "Extension Naming Error\n\nExtension Name Was Blank. Please Enter A Name")
        else:
            if ".xt" not in self.extension_name:
                self.extension_name += ".xt"
            if self.extension_name in listdir(folder):
                showerror("Extension Naming Error", "Extension Naming Error\n\nThe Extension Name Given Is Already Taken")
            else:
                self.callback(self.extension_name)
                self.destroy()

    def cancel(self):
        #Cancel the extension name
        self.extension_name = None
        self.callback(self.extension_name)
        self.destroy()

#Class ExtensionOpener
class ExtensionOpener(Toplevel):
    def __init__(self, master, x, y, callback, color_mode="Dark", *args, **kwargs):
        #Set color mode
        self.color_mode = color_mode
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Initialize the window
        Toplevel.__init__(self, master, *args, **kwargs)
        self.callback = callback
        #Set basic window properties
        self.title("Extension Opener")
        self.geometry("300x250+{}+{}".format(x, y))
        self.attributes("-topmost", True)
        self.resizable(False, False)
        #Create the widgets
        self.extension_name_label = Label(self, text="Extension Opener", font=medium_font)
        self.extension_name_label.place(relx=0.5, rely=.05, anchor=CENTER)
        self.extensions = []
        for file in listdir(folder):
            if file.endswith(".xt"):
                self.extensions.append(file)
        self.extensions.sort()
        self.extension_listbox = Listbox(self, font=normal_font, width=30, height=10)
        for item in self.extensions:
            item = item.split(".xt")[0]
            self.extension_listbox.insert(END, item)
        self.extension_listbox.place(relx=0.5, rely=.5, anchor=CENTER)
        self.extension_listbox.bind("<Double-Button-1>", self.confirm)
        self.confirm_button = Button(self, text="Confirm", font=normal_font, command=self.confirm)
        self.confirm_button.pack(anchor=S, side=LEFT)
        self.cancel_button = Button(self, text="Cancel", font=normal_font, command=self.cancel)
        self.cancel_button.pack(anchor=S, side=RIGHT)
        self.extension_name_label.config(bg=bg, fg=fg)
        self.extension_listbox.config(bg=bg, fg=fg)
        self.confirm_button.config(highlightbackground=bg)
        self.cancel_button.config(highlightbackground=bg)
        self.config(bg=bg)
        self.protocol("WM_DELETE_WINDOW", self.cancel)

    def reset_color(self):
        #Resets the color of the text
        self.extension_name_label.config(fg=light_mode_fg)
        self.extension_listbox.config(fg=light_mode_fg)
        self.confirm_button.config(highlightbackground=light_mode_bg)
        self.cancel_button.config(highlightbackground=light_mode_bg)
        self.config(bg=light_mode_bg)
        #Reset fonts
        self.extension_name_label.config(font=medium_font)
        self.extension_listbox.config(font=normal_font)
        self.confirm_button.config(font=normal_font)
        self.cancel_button.config(font=normal_font)

    def change_self_color(self):
        #Change color_mode and then reset color
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def confirm(self, event=None):
        #Confirm the extension name
        self.extension_name = self.extension_listbox.get(ACTIVE) + ".xt"
        if self.extension_name == ".xt":
            self.extension_name = None
            showerror("Extension Opening Error", "Extension Opening Error\n\nNo Extension Was Selected")
        self.callback(self.extension_name)
        self.destroy()

    def cancel(self):
        #Cancel the extension name
        self.extension_name = None
        self.callback(self.extension_name)
        self.destroy()

#Create ExtensionDeleter class
class ExtensionDeleter(Toplevel):
    def __init__(self, master, x, y, color_mode="Dark", *args, **kwargs):
        #Set color mode
        self.color_mode = color_mode
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg

#Create ExtensionEditor class
class ExtensionEditor(Toplevel):
    def __init__(self, x=0, y=0, *args, **kwargs):
        #Get necessary variables
        self.color_mode = kwargs.pop("color_mode")
        self.change_color = kwargs.pop("change_color")
        self.text_boxes = kwargs.pop("text_boxes")
        self.reset_function = kwargs.pop("reset_function")
        #Get color
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        #Create window
        Toplevel.__init__(self, *args, **kwargs)
        self.withdraw()
        self.config(background=bg)
        self.sidebar_frame = Frame(self, bg="#e0dcd4", width=50)
        self.sidebar_frame.pack(side=LEFT, fill=Y)
        self.command_y_placement = []
        commands = 4
        y_per_command = 100/(commands+1)
        for i in range(commands):
            self.command_y_placement.append((y_per_command*(i+1))*.01)
        self.test_image = PhotoImage(file=(folder / "test.png"))
        self.test_button = Button(self.sidebar_frame, image=self.test_image, command=self.test)
        self.test_button.place(relx=.5, rely=self.command_y_placement[0], anchor=CENTER)
        ToolTip(self.test_button, text="Test the current extension", window=self)
        self.submit_image = PhotoImage(file=(folder / "submit.png"))
        self.submit_button = Button(self.sidebar_frame, image=self.submit_image, command=self.submit)
        self.submit_button.place(relx=.5, rely=self.command_y_placement[1], anchor=CENTER)
        ToolTip(self.submit_button, text="Submit the current extension", window=self)
        self.save_image = PhotoImage(file=(folder / "save.png"))
        self.save_button = Button(self.sidebar_frame, image=self.save_image, command=self.save_file)
        self.save_button.place(relx=.5, rely=self.command_y_placement[2], anchor=CENTER)
        ToolTip(self.save_button, text="Save the current extension", window=self)
        self.open_image = PhotoImage(file=(folder / "open.png"))
        self.open_button = Button(self.sidebar_frame, image=self.open_image, command=self.open_file)
        self.open_button.place(relx=.5, rely=self.command_y_placement[3], anchor=CENTER)
        ToolTip(self.open_button, text="Open past extension", window=self)
        self.notebook_frame = Frame(self, bg=bg, width=932, height=497)
        self.notebook_frame.pack(side=LEFT)
        self.notebook_frame.pack_propagate(False)
        self.main_notebook = Notebook(self.notebook_frame)
        self.main_notebook.pack(fill=BOTH, expand=True)
        self.main_notebook.bind("<Double-Button-1>", self.add_tab_start)
        self.bind("<Command-t>", self.add_tab_start)
        self.bind("<Command-w>", lambda: print("w"))
        self.text_boxes = []
        self.contents_list = []
        self.insert_string = "Lines 1-25 are reserved for comments\nThe comment lines do not require any special characters such as \"#\"\nAll other lines are for the legitimate extension\nExtensions cannot access files in real-time and do not run code\nThe structure of an extension is as follows:\nThe first line is the extesion type\nTypes include:\n- Syntax (Is used to edit keywords and settings)\n- Color Theme Changer (Is used to change the color theme)\n- Font (Is used to change the font size and family)\n- Hybrid (Is used to edit more than one of the above)\nThe second line is the permissions required to use the extension\nThese include:\n- keywords.txt\n- settings.txt\n- color_theme.txt\n- font.txt\nThese can be added together using the \"|\" character and can be in any order\nAn example of the second line would be \"color_theme.txt|settings.txt\"\nThe third line is the name of the extension\nThe fourth line is the description of the extension\nThe fifth line is the author of the extension\nThe lines thereafter contain the extension which are detailed in explanation blocks\nExplanation blocks start and end with block holders and start and end with \"<\" and \">\"\nSee the default extension as a reference!"
        self.finish_adding_tab("NewXT.xt")
        self.contents_list[-1] = self.insert_string
        self.update()
        self.update_idletasks() 
        self.notebook_frame.update()
        self.sidebar_frame.update()
        minimum_height = self.winfo_reqheight()
        minimum_width = self.winfo_reqwidth()
        self.geometry("{}x{}+{}+{}".format(minimum_width, minimum_height, x, y))
        self.resizable(False, False)
        self.deiconify()
        self.text_boxes[0].focus_set()
        self.text_boxes[0].redraw()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.bind("Command-s", self.save_file)

    def add_tab_start(self, event=None):
        #Adds a new tab
        ExtensionNamer(self, self.winfo_x(), self.winfo_y(), callback=self.finish_adding_tab, color_mode=self.color_mode)

    def finish_adding_tab(self, name):
        if name != None:
            text_box = ExtensionText(self.main_notebook, color_mode=self.color_mode, window=self)
            self.text_boxes.append(text_box)
            text_box.insert("1.0", self.insert_string)
            self.contents_list.append("")
            self.main_notebook.add(text_box, text=name)
            self.title("Extension Editor - {}".format(name))
            self.main_notebook.select(text_box)
            text_box.focus_set()
            text_box.text.mark_set("insert", "1.0")
            text_box.redraw()
            self.save_file()

    def remove_tab(self, event=None):
        #Removes a tab
        if len(self.text_boxes) > 1:
            #Get the index of the tab
            index = self.main_notebook.index("current")
            #Check for unsaved changes
            if self.contents_list[index] != self.text_boxes[index].get("1.0", "end-1c"):
                #Do close function procedure
                save = askyesno("Save Changes", "Save changes to {}?\n\nDo you want to save the changes to {}?".format(self.main_notebook.tab(index, "text"), self.main_notebook.tab(index, "text")), parent=self)
                if save:
                    self.save_file()
            #Remove the tab
            self.main_notebook.forget(self.text_boxes[index])
            #Remove the text box
            self.text_boxes.pop(index).destroy()
            #Remove the contents
            self.contents_list.pop(index)
            #Update the title
            self.title("Extension Editor - {}".format(self.main_notebook.tab(self.main_notebook.select(), "text")))
        else:
            showwarning("Tab Removal Error", "A Tab Removal Error Has Occured\n\nMust Have More Than One Tab To Remove Tabs", parent=self)

    def test(self):
        self.save_file()
        try:
            #Test the extension by passing the filename of the current extension to the extension opener
            details = open_test_extension(self.main_notebook.tab(self.main_notebook.select(), "text"))
            the_keywords = details[5]
            if the_keywords != None or "":
                keywords = ""
                for keyword in the_keywords:
                    keywords += keyword + "\n"
                #Remove the last newline
                keywords = keywords[:-1]
                #Update folder / keywords.txt
                with open(folder / "keywords.txt", "w") as f:
                    f.write(keywords)
            else:
                keywords = None
            the_settings = details[6]
            if the_settings != None or "":
                settings = ""
                for setting in the_settings:
                    settings += setting + "\n"
                #Remove the last newline
                settings = settings[:-1]
                #Update folder / settings.txt
                with open(folder / "settings.txt", "w") as settings_file:
                    settings_file.write(settings)
                current_mode = settings.split("\n")[-1]
                if current_mode == "light" and self.color_mode == "light":
                    self.change_color()
                    self.change_color()
                    self.change_self_color()
                    self.change_self_color()
                elif current_mode == "light" and self.color_mode == "Dark":
                    self.change_color()
                    self.change_self_color()
                elif current_mode == "Dark" and self.color_mode == "Dark":
                    self.change_color()
                    self.change_color()
                    self.change_self_color()
                    self.change_self_color()
                elif current_mode == "Dark" and self.color_mode == "light":
                    self.change_color()
                    self.change_color()
            else:
                settings = None
            the_theme = details[7]
            if the_theme != None or "":
                the_theme = the_theme[0] + "\n" + the_theme[1]
                #Update folder / color_theme.txt
                with open(folder / "color_theme.txt", "w") as color_theme:
                    color_theme.write(the_theme)
            else:
                the_theme = None
            the_font = details[8]
            if the_font != None or "":
                family = the_font[0]
                family = family.split(": ")[1]
                normal = the_font[1]
                normal = normal.split(": ")[1]
                with open(folder / "dilate_size.txt", "w") as dilate_size:
                    dilate_size.truncate()
                    dilate_size.seek(0)
                    dilate_size.truncate()
                    dilate_size.seek(0)
                    dilate_size.write(normal)
                med = the_font[2]
                med = med.split(": ")[1]
                large = the_font[3]
                large = large.split(": ")[1]
                min = the_font[4]
                min = min.split(": ")[1]
                max = the_font[5]
                max = max.split(": ")[1]
                string_font = family + "\n" + normal + "\n" + med + "\n" + large + "\n" + min + "\n" + max
                #Update folder / font.txt
                with open(folder / "font.txt", "w") as font_file:
                    font_file.write(string_font)
            for text_box in self.text_boxes:
                text_box.redraw()
            reset_fonts_colors()
            self.reset_function()
            showinfo("Extension Applied", "Extension Applied Successfully\n\nYour extension \"{}\" has been applied successfully.".format(self.main_notebook.tab(self.main_notebook.select(), "text")))
        except IndexError:
            showerror("Extension Application Error", "Extension Application Error\n\nThere Was An Error Applying The Extension. Extensions Must Not Be Empty.")
        except:
            showerror("Extension Application Error", "An Extension Application Error Has Occurred\n\nPlease Check Your Extension And Try Again.")

    def submit(self):
        #Submit the extension
        pass

    def open_file(self):
        #Open a file
        ExtensionOpener(self, self.winfo_x(), self.winfo_y(), callback=self.finish_opening, color_mode=self.color_mode)

    def finish_opening(self, name):
        if name != None:
            self.finish_adding_tab(name)
            with open((folder / name), "r") as file:
                contents = file.read()
                self.text_boxes[-1].text.delete("1.0", "end")
                self.text_boxes[-1].text.insert("1.0", contents)
                self.contents_list[-1] = contents
                self.text_boxes[-1].redraw()
                self.text_boxes[-1].focus_force()
                file.close()

    def reset_color(self):
        #Resets the color of the window
        if self.color_mode == "Dark":
            bg = dark_mode_bg
            fg = dark_mode_fg
        else:
            bg = light_mode_bg
            fg = light_mode_fg
        self.config(background=bg)
        self.notebook_frame.config(bg=bg)
        for text_box in self.text_boxes:
            text_box.change_color()

    def change_self_color(self):
        #Change the color_mode and then reset the color
        if self.color_mode == "Dark":
            self.color_mode = "light"
        else:
            self.color_mode = "Dark"
        self.reset_color()

    def save_file(self):
        with open(folder / self.main_notebook.tab(self.main_notebook.select(), "text"), "w") as file:
            file.truncate()
            file.seek(0)
            file.truncate()
            file.seek(0)
            file.write(self.text_boxes[self.main_notebook.index(self.main_notebook.select())].text.get("1.0", "end-1c"))
            self.contents_list[self.main_notebook.index(self.main_notebook.select())] = self.text_boxes[self.main_notebook.index(self.main_notebook.select())].text.get("1.0", "end-1c")

    def save_from_index(self, index):
        with open(folder / self.main_notebook.tab(index, "text"), "w") as file:
            file.truncate()
            file.seek(0)
            file.truncate()
            file.seek(0)
            file.write(self.text_boxes[index].text.get("1.0", "end-1c"))
            self.contents_list[index] = self.text_boxes[index].text.get("1.0", "end-1c")

    def close(self):
        #Closes the window
        current_contents = []
        for text_box in self.text_boxes:
            current_contents.append(text_box.text.get("1.0", "end-1c"))
        for i in range(len(current_contents)):
            if current_contents[i] != self.contents_list[i]:
                save = askyesno("Save Changes", "Save changes to {}?\n\nDo you want to save the changes to {}?".format(self.main_notebook.tab(i, "text"), self.main_notebook.tab(i, "text")), parent=self)
                if save:
                    self.save_from_index(i)
        self.destroy()


#Testing purposes
if __name__ == "__main__":
    root = Tk()
    s = Style()
    s.theme_use("clam")
    # root.title("Widget Testing")
    # width = root.winfo_screenwidth()
    # height = root.winfo_screenheight()
    # root.geometry("{}x{}+0+0".format(width, height))
    # def close_all():
    #     for child in root.winfo_children():
    #         # print(child)
    #         if isinstance(child, ExtensionEditor):
    #             child.close()
    #     root.destroy()
    # root.protocol("WM_DELETE_WINDOW", close_all)
    text = ultra_text(root, window=root, color_mode = "Dark", have_syntax=True)
    text.pack(fill="both", expand=True)
    x = ExtensionEditor(x=50, y=100, color_mode = "Dark", change_color=lambda: print("Changed"), text_boxes = [text], reset_function=lambda: print("Reset"))
    #self, self.winfo_x(), self.winfo_y(), callback=self.finish_adding_tab, color_mode=self.color_mode
    #self is toplevel
    root.mainloop()