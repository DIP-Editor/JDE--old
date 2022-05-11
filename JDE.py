#Use pytest
import platform
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from ttkScrollableNotebook import *
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
theme_style = open("color_theme.txt", "r").readlines()
light_mode_style = theme_style[0].split(";")
light_mode_bg = light_mode_style[0].split(": ")[1].split("=")[1]
light_mode_fg = light_mode_style[1].split("=")[1].split(";")[0]
dark_mode_style = theme_style[1].split(";")
dark_mode_bg = dark_mode_style[0].split(": ")[1].split("=")[1]
dark_mode_fg = dark_mode_style[1].split("=")[1].split(";")[0]
path_list = []
window = Tk()
current_version = "0.0.7"
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
    window.after(400, final_check)
except:
    def show_version_could_not_be_checked():
        showerror("Version Check", "Version Check Failed\n\nCould Not Connect To Server. Current Version: {}. Connect To The Internet To Check For Updates".format(current_version))
    window.after(400, show_version_could_not_be_checked)
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
#highlightbackground="#4e524f"
run_img = PhotoImage(file=str(folder / "run.png"))
s = Style(window)
s.theme_use("clam")
def about():
    showinfo("JDE", "JDE is an IDE for Python\n\nCreated by: Joshua R. Yacktman\nBeta Version: {}".format(current_version))
window.title("Josh's Development Environment")
main_label = Label(window, text="Josh's Development Environment", font=("Courier New bold", 35))
main_label.place(relx=0.525, y=30, anchor=CENTER)
main_notebook = Notebook(window)
main_notebook.place(relx=.525, rely=.4, anchor=CENTER)
text_boxes = []
main_text_box = ultra_text(window, window=window, color_mode = color_mode)
text_boxes.append(main_text_box)
path_list.append("")
main_notebook.add(main_text_box)
current_focus = main_notebook.index("current")
main_notebook.tab(text_boxes[current_focus], text="Untitled.py")
main_text_box.text.focus()
the_terminal = Terminal(window, font=("Courier New bold", 15), relief=SUNKEN, borderwidth=5, width=102, height=9)
the_terminal.place(relx=.525, rely=.865, anchor=CENTER)
the_terminal.shell = True
the_terminal.basename = "JDE: "
the_terminal.run_command("cd /")
the_terminal.clear()
commands_sidebar = Frame(window, bg="#e0dcd4", width=50)
commands_sidebar.pack(side=LEFT, fill=Y)
filetypes = (("Python Files", "*.py"), ("Text Files", "*.txt"))
def open_file(event=None):
    file_contents = filedialog.askopenfilename(title="Open a file", initialdir="/", filetypes=filetypes)
    window.focus_force()
    if file_contents == "":
        showerror("File Opening Error", "An Error Occurred While Opening File\n\nNo File Was Selected") 
    else:
        main_text_box = ultra_text(window, window=window, color_mode = color_mode)
        text_boxes.append(main_text_box)
        path_list.append(file_contents)
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
        text_boxes[current_focus].insert(1.0, actual_contents)
        #Check if last line is empty or a newline
        # last_line = text_boxes[current_focus].get("end-1l", END)
        # if last_line == "\n" or last_line == "":
        #     #Remove last line
        #     text_boxes[current_focus].delete("end-1l", END)
        #Parse_text
        # text_boxes[current_focus].parse_text()
        text_boxes[current_focus].text.focus()
        the_terminal.clear()
        the_terminal.run_command("cd {}".format(str(Path(file_contents).parent)))
        window.after(200, text_boxes[current_focus].redraw)
open_img = PhotoImage(file=str(folder / "open.png"))
open_button = Button(commands_sidebar, image=open_img, font=("Courier New bold", 20), command=open_file, width=25, highlightbackground="#4e524f")
open_button.place(relx=.5, rely=.1052, anchor=CENTER)
ToolTip(open_button, text="Open File", window=window)
window.bind("<Command-o>", open_file)
def create_new_tab(event=None):
    main_text_box = ultra_text(window, window=window, color_mode = color_mode)
    text_boxes.append(main_text_box)
    path_list.append("")
    main_notebook.add(main_text_box)
    current_focus = main_notebook.index("current")
    main_notebook.select(main_notebook.index(END)-1)
    current_focus = main_notebook.index("current")
    main_notebook.tab(text_boxes[current_focus], text="Untitled.py")
    text_boxes[current_focus].text.focus()
    for i in range(2):
        text_boxes[current_focus].configure(bg=bg)
        text_boxes[current_focus].change_color("{}".format(color_mode))
    text_boxes[current_focus].insert("insert",  "#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n\n# Welcome to Josh's Development Environment!")
    window.after(150, text_boxes[current_focus].redraw)
window.bind("<Command-t>", create_new_tab)
def close_tab(event=None):
    if len(main_notebook.tabs()) > 1:
        current_focus = main_notebook.index("current")
        text_boxes.pop(current_focus)
        path_list.pop(current_focus)
        main_notebook.forget(current_focus)
    else:
        showerror("Tab Removal Error", "A Tab Removal Error Has Occured\n\nMust Have More Than One Tab To Remove Tabs")
def save_file(event=None):
    current_focus = main_notebook.index(CURRENT)
    if path_list[current_focus] == "":
        save_as_file()
    else:
        path = path_list[current_focus]
        open(path, "r+").truncate()
        open(path, "r+").seek(0)
        open(path, "r+").truncate()
        open(path, "r+").seek(0)
        contents = text_boxes[current_focus].get(1.0, END)
        open(path, "r+").write(contents)
save_img = PhotoImage(file=str(folder / "save.png"))
save_button = Button(commands_sidebar, image=save_img, font=("Courier New bold", 20), command=save_file, width=25, highlightbackground="#4e524f")
save_button.place(relx=.5, rely=.1578, anchor=CENTER)
ToolTip(save_button, text="Save", window=window)
window.bind("<Command-s>", save_file)
def save_as_file():
    window.focus_force()
    new_path = filedialog.asksaveasfilename(initialfile = "Untitled.py", filetypes=filetypes)
    main_text_box.focus()
    if new_path == "":
        pass
    else:
        with open(new_path, "w") as file:
            current_focus = main_notebook.index("current")
            contents = text_boxes[current_focus].get(1.0, END)
            file.write(contents)
        current_focus = main_notebook.index("current")
        global path
        path_list[current_focus] = new_path
        the_terminal.clear()
        the_terminal.run_command("cd {}".format(str(Path(new_path).parent)))
        main_notebook.tab(text_boxes[current_focus], text="{}".format(new_path.split("/")[-1]))
save_as_img = PhotoImage(file=(folder / "save_as.png"))
save_as_button = Button(commands_sidebar, image=save_as_img, font=("Courier New bold", 20), command=save_as_file, width=25, highlightbackground="#4e524f")
save_as_button.place(relx=.5, rely=.2104, anchor=CENTER)
ToolTip(save_as_button, text="Save As", window=window)
def copy_contents():
    current_focus = main_notebook.index("current")
    contents = text_boxes[current_focus].get(1.0, END)
    copy(contents)
copy_img = PhotoImage(file=(folder / "copy.png"))
copy_button = Button(commands_sidebar, image=copy_img, font=("Courier New bold", 20), command=copy_contents, width=25, highlightbackground="#4e524f") 
copy_button.place(relx=.5, rely=.263, anchor=CENTER)
ToolTip(copy_button, text="Copy Contents of File", window=window)
def paste_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].insert(INSERT, paste())
    text_boxes[current_focus].redraw()
paste_img = PhotoImage(file=(folder / "paste.png"))
paste_button = Button(commands_sidebar, image=paste_img, font=("Courier New bold", 20), command=paste_contents, width=25, highlightbackground="#4e524f")
paste_button.place(relx=.5, rely=.3156, anchor=CENTER)
ToolTip(paste_button, text="Paste Clipboard Into File", window=window)
def clear_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].delete(1.0, END)
    text_boxes[current_focus].redraw()
clear_img = PhotoImage(file=(folder / "clear_text.png"))
clear_button = Button(commands_sidebar, image=clear_img, font=("Courier New bold", 20), command=clear_contents, width=25, highlightbackground="#4e524f")
clear_button.place(relx=.5, rely=.3682, anchor=CENTER)
ToolTip(clear_button, text="Clear Contents of File", window=window)
def clear_terminal():
    the_terminal.clear()
clear_terminal_img = PhotoImage(file=(folder / "clear_terminal.png"))
clear_terminal_button = Button(commands_sidebar, image=clear_terminal_img, font=("Courier New bold", 20), command=clear_terminal, width=25, highlightbackground="#4e524f")
clear_terminal_button.place(relx=.5, rely=.4208, anchor=CENTER)
ToolTip(clear_terminal_button, text="Clear Terminal", window=window)
def create_template():
    current_focus = main_notebook.index("current")
    temp_name_pop_up(text_boxes[current_focus], x=window.winfo_x(), y=window.winfo_y(), color_mode = color_mode)
create_template_img = PhotoImage(file=(folder / "create_template.png"))
create_template_button = Button(commands_sidebar, image=create_template_img, font=("Courier New bold", 20), command=create_template, width=25, highlightbackground="#4e524f")
create_template_button.place(relx=.5, rely=.4734, anchor=CENTER)
ToolTip(create_template_button, text="Create Template", window=window)
def open_template():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].open_template(window.winfo_x(), window.winfo_y(), color_mode = color_mode)
open_template_img = PhotoImage(file=(folder / "open_template.png"))
open_template_button = Button(commands_sidebar, image=open_template_img, font=("Courier New bold", 20), command=open_template, width=25, highlightbackground="#4e524f")
open_template_button.place(relx=.5, rely=.526, anchor=CENTER)
ToolTip(open_template_button, text="Open Template", window=window)
def delete_template():
    temp_destroy_pop_up(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
delete_template_img = PhotoImage(file=(folder / "delete_template.png"))
delete_template_button = Button(commands_sidebar, image=delete_template_img, font=("Courier New bold", 20), command=delete_template, width=25, highlightbackground="#4e524f")
delete_template_button.place(relx=.5, rely=.5786, anchor=CENTER)
ToolTip(delete_template_button, text="Delete Template", window=window)
def find_replace(event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].make_find_and_replace(window.winfo_x(), window.winfo_y(), color_mode = color_mode)
find_replace_img = PhotoImage(file=(folder / "find_and_replace.png"))
find_replace_button = Button(commands_sidebar, image=find_replace_img, font=("Courier New bold", 20), command=find_replace, width=25, highlightbackground="#4e524f")
find_replace_button.place(relx=.5, rely=.6312, anchor=CENTER)
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
def reset_syntax_colors(event=None):
    global text_boxes
    global path_list
    current_focus = main_notebook.index("current")
    #Get all info from the tabs
    yviews = []
    xviews = []
    text_names = []
    content = []
    paths = []
    mark_sets = []
    # temp_autocompletes = []
    for i in range(len(text_boxes)):
        yviews.append(text_boxes[i].text.yview())
        xviews.append(text_boxes[i].text.xview())
        #get name of i in notebook
        text_names.append(main_notebook.tab(i, "text"))
        content.append(text_boxes[i].text.get(1.0, END))
        #if last line of content is empty, remove it
        if content[i][-1] == "\n":
            content[i] = content[i][:-1]
        paths.append((path_list[i]))
        mark_sets.append(text_boxes[i].index(INSERT))
        # temp_autocompletes.append(text_boxes[i].temporary_autocomplete_list)
    for i in range(len(text_boxes)):
        path_list[i] = paths[i]
    #destroy all text boxes
    for i in range(len(text_boxes)):
        main_notebook.forget(len(text_boxes)-i-1)
    text_boxes = []
    for i in range(len(content)):
        text_boxes.append(ultra_text(main_notebook, window=window, color_mode = color_mode))
        main_notebook.add(text_boxes[i], text=text_names[i])
        text_boxes[i].text.insert(INSERT, content[i])
        text_boxes[i].redraw()
        text_boxes[i].text.yview(MOVETO, yviews[i][0])
        text_boxes[i].text.xview(MOVETO, xviews[i][1])
        text_boxes[i].text.focus_set()
        text_boxes[i].text.mark_set(INSERT, mark_sets[i])
        # text_boxes[i].temporary_autocomplete_list = temp_autocompletes[i]
    #Set the current tab to current_focus
    main_notebook.select(current_focus)
    text_boxes[current_focus].text.focus_set()
    #Redraw current tab
    window.after(150, text_boxes[current_focus].redraw)
    text_boxes[current_focus].text.mark_set(INSERT, mark_sets[current_focus])
    return "Reset"
reset_img = PhotoImage(file=(folder / "reset.png"))
reset_syntax_button = Button(commands_sidebar, image=reset_img, font=("Courier New bold", 20), command=reset_syntax_colors, width=25, highlightbackground="#4e524f")
reset_syntax_button.place(relx=.5, rely=.6838, anchor=CENTER)
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
        reset_syntax_colors()
        text_boxes[i].configure(bg=bg)
        text_boxes[i].change_color("{}".format(color_mode))
    with open(folder / "settings.txt", "r+") as file:
        info = file.read().split("\n")
        info[7] = color_mode
        file.truncate()
        file.seek(0)
        file.truncate()
        file.seek(0)
        file.write("\n".join(info))
    window.configure(bg=bg)
    main_label.configure(bg=bg, fg=fg)
    the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
color_mode_img = PhotoImage(file=(folder / "color_mode.png"))
change_color_mode_button = Button(commands_sidebar, image=color_mode_img, font=("Courier New bold", 20), command=change_color_mode, width=25, highlightbackground="#4e524f")
change_color_mode_button.place(relx=.5, rely=.7364, anchor=CENTER)
ToolTip(change_color_mode_button, text="Change Color Mode", window=window)
def show_extension(extension_name):
    base_name = extension_name
    extension_name = (folder / "extensions/{}.xt".format(extension_name))
    extension_path = str(folder / extension_name)
    details = open_extension(extension_path)
    create_new_tab()
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
    text_boxes[current_focus].insert(1.0, "Extension Name: {}\nExtension Type: {}\nExtension Accesses: {}\nExtension Description: {}\nExtension Author: {}\nExtension Keywords: {}\n\nExtension Settings: {}\n\nExtension Theme: {}".format(name, type, accesses, description, author, keywords, the_settings, the_theme))
    text_boxes[current_focus].redraw()
    text_boxes[current_focus].text.focus()
show_extension_img = PhotoImage(file=(folder / "extensions.png"))
show_extension_button = Button(commands_sidebar, image=show_extension_img, font=("Courier New bold", 20), command= lambda: extension_page(window, color_mode="light", x=window.winfo_x(), y=window.winfo_y(), function=show_extension), width=25, highlightbackground="#4e524f")
show_extension_button.place(relx=.5, rely=.789, anchor=CENTER)
ToolTip(show_extension_button, text="Open Extensions", window=window)
def report_a_bug(event=None):
    report_bug(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
report_bug_img = PhotoImage(file=(folder / "report_bug.png"))
report_a_bug_button = Button(commands_sidebar, image=report_bug_img, font=("Courier New bold", 20), command=report_a_bug, width=25, highlightbackground="#4e524f")
report_a_bug_button.place(relx=.5, rely=.8416, anchor=CENTER)
ToolTip(report_a_bug_button, text="Report A Bug", window=window)
def run_file(event=None):
    if event != None:
        current_focus = main_notebook.index("current")
        line_contents = text_boxes[current_focus].get("insert linestart", "insert lineend")
        current_insert = int(text_boxes[current_focus].index("insert").split(".")[1])
        edited_line = line_contents[current_insert:] + line_contents[:current_insert-1]
        text_boxes[current_focus].delete("insert linestart", "insert lineend")
        text_boxes[current_focus].insert("insert linestart", edited_line)
        run_file()
    else:
        current_focus = main_notebook.index("current")
        path = path_list[current_focus]
        if path == "":
            showerror("Runtime Error", "Can Not Run File\n\nNo File Has Been Selected Or Opened")
        else:
            save_file()
            file_type = path.split(".")
            file_type = file_type[(len(file_type)-1)]
            if file_type == "py":
                the_terminal.run_command("python3 {}".format(path))
            else:
                showerror("Runtime Error", "Runtime Error\n\nFile Type Incompatible. File Could Not Be Run")
run_button = Button(commands_sidebar, image=run_img, font=("Courier New bold", 25), command=run_file, width=25, height=25, highlightbackground="#4e524f")
run_button.place(relx=.5, rely=.0526, anchor=CENTER)
run_button.configure(highlightbackground="#4e524f")
ToolTip(run_button, text="Runs File", window=window)
window.bind("<Command-r>", run_file)
window.bind("<F5>", run_file)
def window_destroy(event=None):
    window.destroy()
window.bind("<Command-w>", close_tab)
settings_img = PhotoImage(file=(folder / "settings.png"))
settings_button = Button(commands_sidebar, image=settings_img, font=("Courier New bold", 20), command= lambda: settings(color_mode=color_mode, x=window.winfo_x(), y=window.winfo_y(), window=window), width=25, highlightbackground="#4e524f")
settings_button.place(relx=.5, rely=.8942, anchor=CENTER)
ToolTip(settings_button, text="Settings", window=window)
quit_img = PhotoImage(file=(folder / "quit.png"))
quit_button = Button(commands_sidebar, image=quit_img, font=("Courier New bold", 15), width=25, highlightbackground="#4e524f", command=window_destroy)
quit_button.place(relx=.5, rely=.9468, anchor=CENTER)
ToolTip(quit_button, text="Quit", window=window)
menubar = Menu(window)
app_menu = Menu(menubar, name="apple")
menubar.add_cascade(menu=app_menu)
edit_menu = Menu(menubar, tearoff=False)
app_menu.add_command(label='About ' + "JDE", command=about)
app_menu.add_separator()
edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=edit_menu, label="Edit")
edit_menu.add_command(label="Open File", command=open_file, accelerator="Command+o")
edit_menu.add_command(label="Save File", command=save_file, accelerator="Command+s")
edit_menu.add_command(label="Save As File", command=save_as_file)
edit_menu.add_cascade(label="Clear Text", command= lambda: clear_contents(None))
edit_menu.add_command(label="Copy", command= copy_contents)
edit_menu.add_command(label="Paste", command= paste_contents)
edit_menu.add_command(label="Find and Replace", command=find_replace, accelerator="Command+f")
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
template_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=template_menu, label="Templates")
template_menu.add_command(label="Create Template", command=create_template)
template_menu.add_command(label="Open Template", command=open_template)
template_menu.add_command(label="Delete Template", command=delete_template)
run_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=run_menu, label="Run")
run_menu.add_command(label="Run File", command=run_file, accelerator="Command+r")
window.createcommand('::tk::mac::ShowPreferences', lambda: settings(color_mode=color_mode, x=window.winfo_x(), y=window.winfo_y()))
window.config(menu=menubar)
help_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=help_menu, label="Help")
help_menu.add_command(label= "Shortcuts", command= lambda: shortcuts_page(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y()))
def open_python_docs():
    webbrowser.open("https://docs.python.org/3/library/")
def help(event=None):
    current_focus = main_notebook.index("current")
    line_contents = text_boxes[current_focus].get("insert linestart", "insert lineend")
    current_insert = int(text_boxes[current_focus].index("insert").split(".")[1])
    edited_line = line_contents[current_insert:] + line_contents[:current_insert-1]
    text_boxes[current_focus].delete("insert linestart", "insert lineend")
    text_boxes[current_focus].insert("insert linestart", edited_line)
    help_info(color_mode = color_mode, x=window.winfo_x(), y=window.winfo_y())
window.bind("<F1>", help)
def open_github():
    webbrowser.open("https://github.com/")
help_menu.add_command(label="Main Help", command=help, accelerator="F1")
help_menu.add_command(label="Python Documentation", command=open_python_docs)
stack_menu = Menu(help_menu, tearoff=False)
help_menu.add_cascade(menu=stack_menu, label="Stackoverflow")
stack_menu.add_command(label="Open StackOverflow", command=stackoverflow)
stack_menu.add_command(label="Ask StackOverflow Question", command=ask_StackOverflow_question)
help_menu.add_command(label="Open GitHub", command=open_github)
help_menu.add_command(label="Report A Bug", command=report_a_bug)
window.configure(bg=bg)
main_text_box.configure(bg=bg)
main_text_box.change_color("{}".format(color_mode))
main_label.configure(bg=bg, fg=fg)
the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
main_notebook.bind('<Double-Button-1>', create_new_tab)
text_boxes[0].insert("insert",  "#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n\n# Welcome to Josh's Development Environment!")
window.after(150, text_boxes[0].redraw)
height_widget_list = [main_label, main_notebook, the_terminal, quit_button]
width_widget_list = [the_terminal, settings_button, quit_button, quit_button]
widget_list = [main_label, main_notebook, the_terminal, quit_button, settings_button]
for widget in widget_list:
    widget.update()
height_required_list = []
width_required_list = []
for widget in height_widget_list:
    height_required_list.append(int(widget.winfo_height()))
for widget in width_widget_list:
    width_required_list.append(int(widget.winfo_width()))
minimum_height = 0
for height in height_required_list:
    minimum_height += height
minimum_width = 0
for width in width_required_list:
    minimum_width += width
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
# x_coords = int((width/2) - (minimum_width/2))
# y_coords = int((height/2) - (minimum_height/2))
# window.geometry("{}x{}+{}+{}".format(minimum_width, minimum_height, x_coords, y_coords))
window.geometry("{}x{}+0+0".format(minimum_width, minimum_height))
window.resizable(False, False)
window.mainloop()