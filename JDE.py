from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from check_version import get_version
import webbrowser
from custom_widgets import *
from tkterminal import *
import sys
from pathlib import Path
from xerox import *
if getattr(sys, 'frozen', False):
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
normal_font = (font_name, normal_size)
medium_font = (font_name, medium_size)
large_font = (font_name, large_size)
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
    reset_syntax_colors()
dilate_size = int(open(folder / "dilate_size.txt", "r").readlines()[0])
path_list = []
have_syntax_list = []
contents_list = []
locked_list = []
window = Tk()
window.withdraw()
withdrawn = True
def about():
    if not withdrawn:
        showinfo("JDE", "JDE is an IDE for Python\n\nCreated by: Joshua R. Yacktman\nBeta Version: {}".format(current_version), parent=window)
menubar = Menu(window)
app_menu = Menu(menubar, name="apple")
menubar.add_cascade(menu=app_menu)
app_menu.add_command(label='About ' + "JDE", command=about)
app_menu.add_separator()
window.config(menu=menubar)
window.createcommand('::tk::mac::ShowPreferences', lambda: settings(color_mode=color_mode, x=window.winfo_x(), y=window.winfo_y(), window=window, function=reset_syntax_colors))
edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=edit_menu, label="Edit")
template_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=template_menu, label="Templates")
run_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=run_menu, label="Run")
help_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=help_menu, label="Help")
stack_menu = Menu(help_menu, tearoff=False)
help_menu.add_cascade(menu=stack_menu, label="Stackoverflow")
current_version = "0.0.8"
try:
    version = get_version()
    def final_check():
        version_split = version.split(".")
        current_version_split = current_version.split(".")
        for i in range(len(version_split)):
            if int(version_split[i]) < int(current_version_split[i]):
                pass
            elif int(version_split[i]) > int(current_version_split[i]):
                open_donwload = askyesno("Update Available", "A New Version Is Currently Available\n\nYour Version: {}\nCurrent Version: {}\nWould You Like To Download It?".format(current_version, get_version()))
                if open_donwload:
                    webbrowser.open("https://jde-org.github.io/")
                break
            else:
                pass
    window.after(1000, final_check)
except:
    def show_version_could_not_be_checked():
        showwarning("Version Check", "Version Check Failed\n\nCould Not Connect To Server. Current Version: {}. Connect To The Internet To Check For Updates".format(current_version))
    window.after(1000, show_version_could_not_be_checked)
color_mode_file = open((folder / "settings.txt"), "r+")
color_mode_soon = color_mode_file.readlines()
color_mode_soon = color_mode_soon[7]
if color_mode_soon == "":
    color_mode_soon = "dark"
color_mode = color_mode_soon
if color_mode == "Dark":
    bg = dark_mode_bg
    fg = dark_mode_fg
else:
    bg = light_mode_bg
    fg = light_mode_fg
#highlightbackground="#D4D2CB"
run_img = PhotoImage(file=str(folder / "run.png"))
s = Style(window)
s.theme_use("clam")
window.title("Josh's Development Environment")
notebook_frame = Frame(window, width=950, height=525)
commands_sidebar = Frame(window, bg="#e0dcd4", width=50, height=700)
commands_sidebar.pack(anchor=W, side=LEFT)
command_y_placement = []
commands = 19
y_per_command = 100/(commands+1)
for i in range(commands):
    command_y_placement.append((y_per_command*(i+1))*.01)
notebook_frame.pack(anchor=N, side=TOP)
notebook_frame.pack_propagate(False)
main_notebook = Notebook(notebook_frame)
main_notebook.pack(fill=BOTH, expand=True)
text_boxes = []
main_text_box = ultra_text(window, window=window, color_mode = color_mode, have_syntax=True)
main_text_box.callback("from")
have_syntax_list.append(True)
text_boxes.append(main_text_box)
path_list.append("")
locked_list.append(False)
contents_list.append("#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n \n# Welcome to Josh's Development Environment!")
main_notebook.add(main_text_box)
current_focus = main_notebook.index("current")
main_notebook.tab(text_boxes[current_focus], text="Untitled.py")
main_text_box.text.focus()
terminal_frame = Frame(window, width=950, height=175)
#Pack under the main text box
terminal_frame.pack(anchor=N, side=TOP)
terminal_frame.pack_propagate(False)
the_terminal = Terminal(terminal_frame, font=normal_font, relief=RIDGE, borderwidth=5, width=120, height=9)
the_terminal.pack(fill=BOTH, expand=True)
the_terminal.shell = True
the_terminal.basename = "JDE: "
the_terminal.linebar = True
filetypes = (("Python Scripts", "*.py"), ("Text Files", "*.txt"))
def open_file(event=None, path=None):
    if path == None:
        file_contents = filedialog.askopenfilename(initialdir="/", filetypes=filetypes, parent=window)
    else:
        file_contents = path
    if file_contents == "":
        showwarning("File Opening Error", "An Error Occurred While Opening File\n\nNo File Was Selected", parent=window)
    else:
        #Check if file is a txt file
        if file_contents.split(".")[-1] == "txt":
            have_syntax = False
        else:
            have_syntax = True
        main_text_box = ultra_text(window, window=window, color_mode = color_mode, have_syntax=have_syntax)
        have_syntax_list.append(have_syntax)
        text_boxes.append(main_text_box)
        path_list.append(file_contents)
        locked_list.append(False)
        main_notebook.add(main_text_box)
        current_focus = main_notebook.index("current")
        main_notebook.select(main_notebook.index(END)-1)
        current_focus = main_notebook.index("current")
        file_name = file_contents.split("/")
        file_name = file_name[-1]
        main_notebook.tab(text_boxes[current_focus], text="{}".format(file_name))
        for i in range(2):
            change_color_mode()
        text_boxes[current_focus].delete(1.0, END)
        actual_contents = (open(file_contents, "r")).read()
        contents_list.append(actual_contents)
        text_boxes[current_focus].insert(1.0, actual_contents)
        text_boxes[current_focus].parse_text()
        #Check if last line is empty or a newline
        # last_line = text_boxes[current_focus].get("end-1l", END)
        # if last_line == "\n" or last_line == "":
        #     #Remove last line
        #     text_boxes[current_focus].delete("end-1l", END)
        #Parse_text
        # text_boxes[current_focus].parse_text()
        text_boxes[current_focus].text.focus()
        window.after(1, text_boxes[current_focus].redraw)
open_img = PhotoImage(file=str(folder / "open.png"))
open_button = Button(commands_sidebar, image=open_img, font=medium_font, command=open_file, width=25, highlightbackground="#D4D2CB")
open_button.place(relx=.5, rely=command_y_placement[1], anchor=CENTER)
ToolTip(open_button, text="Open File", window=window)
window.bind("<Command-o>", open_file)
def create_new_tab(event=None, have_syntax=True, extension=False):
    main_text_box = ultra_text(window, window=window, color_mode = color_mode, have_syntax=have_syntax)
    have_syntax_list.append(have_syntax)
    text_boxes.append(main_text_box)
    path_list.append("")
    if extension == False:
        locked_list.append(False)
    else:
        locked_list.append(True)
    contents_list.append("#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n \n# Welcome to Josh's Development Environment!")
    main_notebook.add(main_text_box)
    current_focus = main_notebook.index("current")
    main_notebook.select(main_notebook.index(END)-1)
    current_focus = main_notebook.index("current")
    main_notebook.tab(text_boxes[current_focus], text="Untitled.py")
    text_boxes[current_focus].text.focus()
    for i in range(2):
        text_boxes[current_focus].configure(bg=bg)
        text_boxes[current_focus].change_color("{}".format(color_mode))
    text_boxes[current_focus].insert("insert",  "#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n \n# Welcome to Josh's Development Environment!")
    text_boxes[current_focus].select_all()
    window.after(1, text_boxes[current_focus].redraw)
window.bind("<Command-t>", create_new_tab)
def close_tab(event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus-1].text.focus_force()
    if len(main_notebook.tabs()) > 1:
        name = main_notebook.tab(current_focus)["text"]
        if name.startswith("Extension") and (".py" not in name) and (".txt" not in name):
            text_boxes.pop(current_focus)
            path_list.pop(current_focus)
            contents_list.pop(current_focus)
            locked_list.pop(current_focus)
            main_notebook.forget(current_focus)
            text_boxes[current_focus-1].text.focus_force()
        else:
            if contents_list[current_focus] != text_boxes[current_focus].text.get(1.0, "end-1c"):
                ask_save = askyesno("Save File", "Save File Before Closing\n\nWould You Like To Save This File Before Closing?", parent=window)
                if ask_save == True:
                    save_file()
            text_boxes.pop(current_focus)
            path_list.pop(current_focus)
            contents_list.pop(current_focus)
            main_notebook.forget(current_focus)
            locked_list.pop(current_focus)
            have_syntax_list.pop(current_focus)
    else:
        close()
def save_file(event=None, text_index=None):
    if text_index == None:
        current_focus = main_notebook.index(CURRENT)
    else:
        current_focus = text_index
    if path_list[current_focus] == "":
        save_as_file(text_index=current_focus)
    else:
        path = path_list[current_focus]
        open(path, "r+").truncate()
        open(path, "r+").seek(0)
        open(path, "r+").truncate()
        open(path, "r+").seek(0)
        contents = text_boxes[current_focus].get(1.0, "end-1c")
        open(path, "r+").write(contents)
        contents_list[current_focus] = contents
def save_all():
    for i in range(len(text_boxes)):
        if path_list[i] == "":
            save_as_file(text_index=i)
        else:
            save_file(text_index=i)
def change_tab(event):
    number = int(event.keysym)-1
    if len(main_notebook.tabs()) > number:
        main_notebook.select(number)
window.bind("<Command-Key-1>", change_tab)
window.bind("<Command-Key-2>", change_tab)
window.bind("<Command-Key-3>", change_tab)
window.bind("<Command-Key-4>", change_tab)
window.bind("<Command-Key-5>", change_tab)
window.bind("<Command-Key-6>", change_tab)
window.bind("<Command-Key-7>", change_tab)
window.bind("<Command-Key-8>", change_tab)
window.bind("<Command-Key-9>", change_tab)
save_img = PhotoImage(file=str(folder / "save.png"))
save_button = Button(commands_sidebar, image=save_img, font=medium_font, command=save_file, width=25, highlightbackground="#D4D2CB")
save_button.place(relx=.5, rely=command_y_placement[2], anchor=CENTER)
ToolTip(save_button, text="Save", window=window)
window.bind("<Command-s>", save_file)
def save_as_file(text_index=None):
    new_path = filedialog.asksaveasfilename(initialfile = "Untitled.py", filetypes=filetypes, parent=window)
    main_text_box.focus()
    if new_path == "":
        pass
    else:
        if text_index == None:
            current_focus = main_notebook.index("current")
        else:
            current_focus = text_index
        with open(new_path, "w") as file:
            contents = text_boxes[current_focus].get(1.0, END)
            file.write(contents)
        current_focus = main_notebook.index("current")
        global path
        path_list[current_focus] = new_path
        main_notebook.tab(text_boxes[current_focus], text="{}".format(new_path.split("/")[-1]))
save_as_img = PhotoImage(file=(folder / "save_as.png"))
save_as_button = Button(commands_sidebar, image=save_as_img, font=medium_font, command=save_as_file, width=25, highlightbackground="#D4D2CB")
save_as_button.place(relx=.5, rely=command_y_placement[3], anchor=CENTER)
ToolTip(save_as_button, text="Save As", window=window)
def copy_contents():
    current_focus = main_notebook.index("current")
    contents = text_boxes[current_focus].get(1.0, END)
    copy(contents)
copy_img = PhotoImage(file=(folder / "copy.png"))
copy_button = Button(commands_sidebar, image=copy_img, font=medium_font, command=copy_contents, width=25, highlightbackground="#D4D2CB") 
copy_button.place(relx=.5, rely=command_y_placement[4], anchor=CENTER)
ToolTip(copy_button, text="Copy Contents of File", window=window)
def paste_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].insert(INSERT, paste())
    text_boxes[current_focus].redraw()
paste_img = PhotoImage(file=(folder / "paste.png"))
paste_button = Button(commands_sidebar, image=paste_img, font=medium_font, command=paste_contents, width=25, highlightbackground="#D4D2CB")
paste_button.place(relx=.5, rely=command_y_placement[5], anchor=CENTER)
ToolTip(paste_button, text="Paste Clipboard Into File", window=window)
def clear_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].delete(1.0, END)
    text_boxes[current_focus].redraw()
clear_img = PhotoImage(file=(folder / "clear_text.png"))
clear_button = Button(commands_sidebar, image=clear_img, font=medium_font, command=clear_contents, width=25, highlightbackground="#D4D2CB")
clear_button.place(relx=.5, rely=command_y_placement[6], anchor=CENTER)
ToolTip(clear_button, text="Clear Contents of File", window=window)
def clear_terminal():
    the_terminal.clear()
clear_terminal_img = PhotoImage(file=(folder / "clear_terminal.png"))
clear_terminal_button = Button(commands_sidebar, image=clear_terminal_img, font=medium_font, command=clear_terminal, width=25, highlightbackground="#D4D2CB")
clear_terminal_button.place(relx=.5, rely=command_y_placement[7], anchor=CENTER)
ToolTip(clear_terminal_button, text="Clear Terminal", window=window)
def create_template():
    current_focus = main_notebook.index("current")
    temp_name_pop_up(text_boxes[current_focus], x=window.winfo_x(), y=window.winfo_y(), color_mode = color_mode)
create_template_img = PhotoImage(file=(folder / "create_template.png"))
create_template_button = Button(commands_sidebar, image=create_template_img, font=medium_font, command=create_template, width=25, highlightbackground="#D4D2CB")
create_template_button.place(relx=.5, rely=command_y_placement[8], anchor=CENTER)
ToolTip(create_template_button, text="Create Template", window=window)
def open_template():
    current_focus = main_notebook.index("current")
    temp_open_pop_up(x=window.winfo_x(), y=window.winfo_y(), color_mode = color_mode, text=text_boxes[current_focus])
open_template_img = PhotoImage(file=(folder / "open_template.png"))
open_template_button = Button(commands_sidebar, image=open_template_img, font=medium_font, command=open_template, width=25, highlightbackground="#D4D2CB")
open_template_button.place(relx=.5, rely=command_y_placement[9], anchor=CENTER)
ToolTip(open_template_button, text="Open Template", window=window)
def delete_template():
    temp_destroy_pop_up(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
delete_template_img = PhotoImage(file=(folder / "delete_template.png"))
delete_template_button = Button(commands_sidebar, image=delete_template_img, font=medium_font, command=delete_template, width=25, highlightbackground="#D4D2CB")
delete_template_button.place(relx=.5, rely=command_y_placement[10], anchor=CENTER)
ToolTip(delete_template_button, text="Delete Template", window=window)
def find_replace(event=None):
    search_bar = search_text(x=window.winfo_x(), y=window.winfo_y(), color_mode = color_mode)
    search_bar.attach(text_boxes[main_notebook.index("current")].text, text_boxes[main_notebook.index("current")])
    search_bar.focus_set()
find_replace_img = PhotoImage(file=(folder / "find_and_replace.png"))
find_replace_button = Button(commands_sidebar, image=find_replace_img, font=medium_font, command=find_replace, width=25, highlightbackground="#D4D2CB")
find_replace_button.place(relx=.5, rely=command_y_placement[11], anchor=CENTER)
ToolTip(find_replace_button, text="Find and Replace", window=window)
window.bind("<Command-f>", find_replace)
def stackoverflow(event=None):
    webbrowser.open("https://stackoverflow.com/")
def ask_StackOverflow_question(event=None):
    webbrowser.open("https://stackoverflow.com/questions/ask")
def redraw_all(event=None):
    for i in range(len(text_boxes)):
        text_boxes[i].redraw()
window.bind("<Button-1>", redraw_all)
def reset():
    try:
        reset_fonts_colors()
        for i in range(len(text_boxes)):
            text_boxes[i].update()
            text_boxes[i].text.config(font=normal_font)
            text_boxes[i].redraw()
        the_terminal.update()
        the_terminal.config(font=normal_font)
        main_notebook.update()
    except:
        pass
def reset_syntax_colors(event=None):
    for i in range(len(text_boxes)):
        text_boxes[i].reset_syntax()
reset_img = PhotoImage(file=(folder / "reset.png"))
reset_syntax_button = Button(commands_sidebar, image=reset_img, font=medium_font, command=reset_syntax_colors, width=25, highlightbackground="#D4D2CB")
reset_syntax_button.place(relx=.5, rely=command_y_placement[12], anchor=CENTER)
ToolTip(reset_syntax_button, text="Reset Syntax Highlighting", window=window)
def change_color_mode(event=None):
    global color_mode
    if color_mode == "Dark":
        color_mode = "light"
        bg = light_mode_bg
        fg = light_mode_fg
    else:
        color_mode = "Dark"
        bg = dark_mode_bg
        fg = dark_mode_fg
    for i in range(len(text_boxes)):
        text_boxes[i].configure(bg=bg)
        text_boxes[i].change_color("{}".format(color_mode))
    window.configure(bg=bg)
    the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
    get_info_from_files()
    for child in window.winfo_children():
        print(child)
        if isinstance(child, extension_page):
            child.change_self_color()
        elif isinstance(child, go_to_line):
            child.change_self_color()
        elif isinstance(child, keyword_change_page):
            child.change_self_color()
        elif isinstance(child, shortcuts_page):
            child.change_self_color()
        elif isinstance(child, search_text):
            child.change_self_color()
        elif isinstance(child, temp_name_pop_up):
            child.change_self_color()
        elif isinstance(child, temp_open_pop_up):
            child.change_self_color()
        elif isinstance(child, temp_destroy_pop_up):
            child.change_self_color()
        elif isinstance(child, settings):
            child.change_self_color()
        elif isinstance(child, report_bug):
            child.change_self_color()
        elif isinstance(child, help_info):
            child.change_self_color()
        elif isinstance(child, ExtensionEditor):
            child.change_self_color()
        elif isinstance(child, ExtensionNamer):
            child.change_self_color()
        elif isinstance(child, ExtensionOpener):
            child.change_self_color()
    with open(folder / "settings.txt", "r+") as file:
        info = file.read().split("\n")
        info[7] = color_mode
        file.truncate()
        file.seek(0)
        file.truncate()
        file.seek(0)
        file.write("\n".join(info))
color_mode_img = PhotoImage(file=(folder / "color_mode.png"))
change_color_mode_button = Button(commands_sidebar, image=color_mode_img, font=medium_font, command=change_color_mode, width=25, highlightbackground="#D4D2CB")
change_color_mode_button.place(relx=.5, rely=command_y_placement[13], anchor=CENTER)
ToolTip(change_color_mode_button, text="Change Color Mode", window=window)
def zoom_in(event):
    global dilate_size
    if dilate_size+1 <= int(max):
        for text_box in text_boxes:
            text_box.increase_font()
        with open(folder / "dilate_size.txt", "r+") as file:
            new_file_contents = dilate_size + 1
            if new_file_contents >= int(max):
                new_file_contents = int(max)
            file.truncate()
            file.seek(0)
            file.truncate()
            file.seek(0)
            file.write(str(new_file_contents))
        dilate_size = new_file_contents
        update_dilate_size()
def zoom_out(event):
    global dilate_size
    if dilate_size-1 >= int(min):
        for text_box in text_boxes:
            text_box.decrease_font()
        with open(folder / "dilate_size.txt", "r+") as file:
            new_file_contents = dilate_size - 1
            if new_file_contents <= int(min):
                new_file_contents = int(min)
            file.truncate()
            file.seek(0)
            file.truncate()
            file.seek(0)
            file.write(str(new_file_contents))
        dilate_size = new_file_contents
        update_dilate_size()
window.bind("<Command-=>", zoom_in)
window.bind("<Command-Key-minus>", zoom_out)
def show_extension(extension_name):
    base_name = extension_name
    extension_name = ("https://jde-org.github.io/extensions/{}.xt".format(extension_name))
    extension_path = extension_name
    details = open_extension(extension_path)
    create_new_tab(have_syntax=False, extension=True)
    current_focus = main_notebook.index("current")
    main_notebook.tab(text_boxes[current_focus], text="{}".format("Extension: {}".format(base_name)))
    #Remove everything from the text box
    text_boxes[current_focus].delete(1.0, END)
    #Insert the extension details
    type = details[0]
    accesses = details[1]
    name = details[2]
    description = details[3]
    author = details[4]
    keywords = details[5]
    the_settings = details[6]
    the_theme = details[7]
    the_font = details[8]
    insert_string = "Extension Name: {}\nExtension Type: {}\nExtension Accesses: {}\nExtension Description: {}\nExtension Author: {}\nExtension Keywords: {}\nExtension Settings: {}\nExtension Theme: {}\nExtension Font: {}".format(name, type, accesses, description, author, keywords, the_settings, the_theme, the_font)
    text_boxes[current_focus].insert(1.0, insert_string)
    # text_boxes[current_focus].text.image_create(1.0, image=show_extension_img)
    text_boxes[current_focus].redraw()
    text_boxes[current_focus].text.configure(state=DISABLED)
    contents_list[current_focus] = text_boxes[current_focus].text.get(1.0, END)
show_extension_img = PhotoImage(file=(folder / "extensions.png"))
show_extension_button = Button(commands_sidebar, image=show_extension_img, font=medium_font, command= lambda: extension_page(window, color_mode=color_mode, x=window.winfo_x(), y=window.winfo_y(), function=show_extension, reset=reset, change_color=change_color_mode, text_boxes = text_boxes), width=25, highlightbackground="#D4D2CB")
show_extension_button.place(relx=.5, rely=command_y_placement[14], anchor=CENTER)
ToolTip(show_extension_button, text="Open Extensions", window=window)
def create_extension():
    ExtensionEditor(x=window.winfo_x(), y=window.winfo_y(), color_mode=color_mode, change_color=change_color_mode, text_boxes=text_boxes, reset_function=reset)
create_extension_img = PhotoImage(file=(folder / "create_extension.png"))
create_extension_button = Button(commands_sidebar, image=create_extension_img, font=medium_font, command=create_extension, width=25, highlightbackground="#D4D2CB")
create_extension_button.place(relx=.5, rely=command_y_placement[15], anchor=CENTER)
ToolTip(create_extension_button, text="Create Extension", window=window)
def report_a_bug(event=None):
    report_bug(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
report_bug_img = PhotoImage(file=(folder / "report_bug.png"))
report_a_bug_button = Button(commands_sidebar, image=report_bug_img, font=medium_font, command=report_a_bug, width=25, highlightbackground="#D4D2CB")
report_a_bug_button.place(relx=.5, rely=command_y_placement[16], anchor=CENTER)
ToolTip(report_a_bug_button, text="Report A Bug", window=window)
def run_file(event=None):
    # if event != None:
    #     current_focus = main_notebook.index("current")
    #     line_contents = text_boxes[current_focus].get("insert linestart", "insert lineend")
    #     current_insert = int(text_boxes[current_focus].index("insert").split(".")[1])
    #     edited_line = line_contents[current_insert:] + line_contents[:current_insert-1]
    #     text_boxes[current_focus].delete("insert linestart", "insert lineend")
    #     text_boxes[current_focus].insert("insert linestart", edited_line)
    #     run_file()
    # else:
    current_focus = main_notebook.index("current")
    path = path_list[current_focus]
    if path == "":
        showwarning("Runtime Error", "Can Not Run File\n\nNo File Has Been Selected Or Opened", parent=window)
    else:
        save_file()
        file_type = path.split(".")
        file_type = file_type[(len(file_type)-1)]
        if file_type == "py":
            dir = (path.split("/")[:-1])
            dir = "/".join(dir)
            file = path.split("/")[-1]
            the_terminal.run_command("cd \"{}\"; /usr/local/bin/python3 \"{}\"".format(dir, file))
        else:
            showwarning("Runtime Error", "Runtime Error\n\nFile Type Incompatible. File Could Not Be Run", parent=window)
run_button = Button(commands_sidebar, image=run_img, font=medium_font, command=run_file, highlightbackground="#D4D2CB")
run_button.place(relx=.5, rely=command_y_placement[0], anchor=CENTER)
run_button.configure(highlightbackground="#D4D2CB")
ToolTip(run_button, text="Runs File", window=window)
window.bind("<Command-r>", run_file)
window.bind("<F5>", run_file)
window.bind("<Command-w>", close_tab)
settings_img = PhotoImage(file=(folder / "settings.png"))
settings_button = Button(commands_sidebar, image=settings_img, font=medium_font, command= lambda: settings(color_mode=color_mode, x=window.winfo_x(), y=window.winfo_y(), window=window, function=reset_syntax_colors), width=25, highlightbackground="#D4D2CB")
settings_button.place(relx=.5, rely=command_y_placement[17], anchor=CENTER)
ToolTip(settings_button, text="Settings", window=window)
def close():
    current_contents = []
    for i in range(len(text_boxes)):
        name = main_notebook.tab(i)["text"]
        if name.startswith("Extension: "):
            if (".py" not in name) and (".txt" not in name):
                current_contents.append(contents_list[i])
            else:
                current_contents.append(text_boxes[i].get("1.0", "end-1c"))
        else:
            current_contents.append(text_boxes[i].get("1.0", "end-1c"))
    for i in range(len(current_contents)):
        if current_contents[i] != contents_list[i]:
            save_no_save = askquestion("Save Files", "Save Files Before Closing\n\nDo You Want To Save All Files Before Closing?", parent=window)
            if save_no_save == "yes":
                save_all()
            break
    for child in window.winfo_children():
        if isinstance(child, ExtensionEditor):
            child.close()
        # elif 
    window.destroy()
quit_img = PhotoImage(file=(folder / "quit.png"))
quit_button = Button(commands_sidebar, image=quit_img, font=normal_font, width=25, highlightbackground="#D4D2CB", command=close)
quit_button.place(relx=.5, rely=command_y_placement[18], anchor=CENTER)
window.protocol("WM_DELETE_WINDOW", close)
ToolTip(quit_button, text="Quit", window=window)
#
#
#
#
#
#
edit_menu.add_command(label="Open File", command=open_file, accelerator="Command+o")
edit_menu.add_command(label="Save File", command=save_file, accelerator="Command+s")
edit_menu.add_command(label="Save As File", command=save_as_file)
edit_menu.add_cascade(label="Clear Text", command= lambda: clear_contents(None))
edit_menu.add_command(label="Copy", command= copy_contents)
edit_menu.add_command(label="Paste", command= paste_contents)
edit_menu.add_command(label="Find and Replace", command=find_replace, accelerator="Command+f")
edit_menu.add_command(label="Go To Line", command=go_to_line, accelerator="Command+g")
def tabs_to_spaces (event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].tabs_to_spaces()
def spaces_to_tabs (event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].spaces_to_tabs()
edit_menu.add_command(label="Tabs to Spaces", command=tabs_to_spaces)
edit_menu.add_command(label="Spaces to Tabs", command=spaces_to_tabs)
edit_menu.add_command(label="Create Tab", command=create_new_tab, accelerator="Command+t")
edit_menu.add_command(label="Close Tab", command=close_tab, accelerator="Command+w")
template_menu.add_command(label="Create Template", command=create_template)
template_menu.add_command(label="Open Template", command=open_template)
template_menu.add_command(label="Delete Template", command=delete_template)
run_menu.add_command(label="Run File", command=run_file, accelerator="Command+r")
help_menu.add_command(label= "Shortcuts", command= lambda: shortcuts_page(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y()))
def open_python_docs():
    webbrowser.open("https://docs.python.org/3/library/")
def help(event=None):
    help_info(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
window.bind("<F1>", help)
def open_github():
    webbrowser.open("https://github.com/")
help_menu.add_command(label="JDE Help", command=help, accelerator="F1")
help_menu.add_command(label="Python Documentation", command=open_python_docs)
stack_menu.add_command(label="Open StackOverflow", command=stackoverflow)
stack_menu.add_command(label="Ask StackOverflow Question", command=ask_StackOverflow_question)
help_menu.add_command(label="Open GitHub", command=open_github)
help_menu.add_command(label="Report A Bug", command=report_a_bug)
# window.config(menu=menubar)
#
#
#
#
window.configure(bg=bg)
main_text_box.configure(bg=bg)
main_text_box.change_color("{}".format(color_mode))
the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
main_notebook.bind('<Double-Button-1>', create_new_tab)
text_boxes[0].insert("insert",  "#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n \n# Welcome to Josh's Development Environment!")
upon_open_paths = sys.argv[1:]
#Append 5 paths
# upon_open_paths += ["/Users/joshyacktman/Desktop/JDE/extension_handler.py", "/Users/joshyacktman/Desktop/JDE/check_version.py", "/Users/joshyacktman/Desktop/JDE/custom_widgets.py", "/Users/joshyacktman/Desktop/JDE/settings.txt", "/Users/joshyacktman/Desktop/JDE/JDE.py"]
def argv_open_files():
    for i in range(len(upon_open_paths)):
        path = upon_open_paths[i]
        if path.endswith(".py"):
            create_new_tab()
            text_boxes[-1].text.delete("1.0", "end")
            text_boxes[-1].text.insert("insert", open(path, "r").read())
            main_notebook.select(main_notebook.tabs()[-1])
            current_focus = main_notebook.index("current")
            text_boxes[current_focus].text.mark_set("insert", "1.0")
            name = path.split("/")[-1]
            main_notebook.tab(main_notebook.tabs()[-1], text=name)
            path_list[current_focus] = path
            save_file(text_index=current_focus)
        elif path.endswith(".txt"):
            create_new_tab(have_syntax=False)
            text_boxes[-1].text.delete("1.0", "end")
            text_boxes[-1].text.insert("insert", open(path, "r").read())
            main_notebook.select(main_notebook.tabs()[-1])
            current_focus = main_notebook.index("current")
            text_boxes[current_focus].text.mark_set("insert", "1.0")
            name = path.split("/")[-1]
            main_notebook.tab(main_notebook.tabs()[-1], text=name)
            path_list[current_focus] = path
            save_file(text_index=current_focus)
    upon_open_paths.clear()
    main_notebook.select(0)
    text_boxes[0].redraw()
    text_boxes[0].select_all()
    text_boxes[0].redraw()
    main_notebook.select(len(text_boxes)-1)
text_boxes[0].select_all()
window.title("Josh's Development Environment - Untitled.py")
def update_titlebar(event):
    current_focus = main_notebook.index("current")
    if path_list[current_focus] == "":
        window.title("Josh's Development Environment - Untitled.py")
    else:
        file_name = path_list[current_focus].split("/")[-1]
        window.title("Josh's Development Environment - {}".format(file_name))
main_notebook.bind("<<NotebookTabChanged>>", update_titlebar)
def open_future_argv(*args):
    for i in range(len(args)):
        upon_open_paths.append(str(args[i]))
    argv_open_files()
    window.focus_force()
    main_notebook.select(len(main_notebook.tabs())-1)
window.createcommand("::tk::mac::OpenDocument", open_future_argv)
window.after(1, text_boxes[0].redraw)
height_widget_list = [main_notebook, the_terminal, quit_button]
width_widget_list = [the_terminal, commands_sidebar]
widget_list = [main_notebook, the_terminal, quit_button, settings_button]
window.update_idletasks()
# for widget in widget_list:
#     widget.update()
# height_required_list = []
# width_required_list = []
# for widget in height_widget_list:
#     height_required_list.append(int(widget.winfo_height()))
# for widget in width_widget_list:
#     width_required_list.append(int(widget.winfo_width()))
# minimum_height = 0
# for height in height_required_list:
#     minimum_height += height
# minimum_width = 0
# for width in width_required_list:
#     minimum_width += width
minimum_width = window.winfo_reqwidth()
minimum_height = window.winfo_reqheight()
x_coords = int(window.winfo_screenwidth()/2 - minimum_width/2)
y_coords = int(window.winfo_screenheight()/2 - minimum_height/2)-20
window.geometry("{}x{}+{}+{}".format(minimum_width, minimum_height, x_coords, y_coords))
window.resizable(False, False)
window.deiconify()
withdrawn = False
window.after(10, argv_open_files())
window.mainloop()