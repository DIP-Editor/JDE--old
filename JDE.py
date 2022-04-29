#Use pytest
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
path_list = []
window = Tk()
current_version = "0.0.4"
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
    bg = "#4f4c4d"
    fg = "white"
else:
    bg = "white"
    fg = "#4f4c4d"
# window.resizable(0, 0)
run_img = PhotoImage(file=str(folder / "run.png"))
s = Style(window)
s.theme_use("clam")
def about():
    showinfo("JDE", "JDE is an IDE for Python\n\nCreated by: Joshua R. Yacktman\nBeta Version: {}".format(current_version))
# window.geometry("%dx%d+0+0" % (1110, 720))
# window.wm_minsize(1110, 720)
#Width, Height, X, Y
window.title("Josh's Development Environment")
main_label = Label(window, text="Josh's Development Environment", font=("Courier New bold", 35))
main_label.place(relx=0.5, y=30, anchor=CENTER)
main_notebook = Notebook(window)
main_notebook.place(relx=.575, rely=.4, anchor=CENTER)
text_boxes = []
main_text_box = ultra_text(window, window=window, color_mode = color_mode)
text_boxes.append(main_text_box)
path_list.append("")
main_notebook.add(main_text_box)
current_focus = main_notebook.index("current")
main_notebook.tab(text_boxes[current_focus], text="Untitled.py")
main_text_box.text.focus()
the_terminal = Terminal(window, font=("Courier New bold", 15), relief=SUNKEN, borderwidth=5, width=119, height=9)
the_terminal.place(relx=.5, rely=.85, anchor=CENTER)
the_terminal.shell = True
the_terminal.basename = "JDE: "
the_terminal.run_command("cd /")
the_terminal.clear()
commands_label = Label(window, text="Commands:", font=("Courier New bold", 25))
commands_label.place(relx=.0825, rely=.05, anchor=CENTER)
filetypes = (("Python Files", "*.py"), ("Text Files", "*.txt"))
def open_file(event=None):
    file_contents = filedialog.askopenfilename(title="Open a file", initialdir="/", filetypes=filetypes)
    window.focus_force()
    if file_contents == "":
        pass
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
        #Delete last line
        # if text_boxes[current_focus].text.get("end-1l") == "" or " " or "\n":
        #     text_boxes[current_focus].delete("end-1l", END)
        text_boxes[current_focus].text.focus()
        the_terminal.clear()
        the_terminal.run_command("cd {}".format(str(Path(file_contents).parent)))
        window.after(200, text_boxes[current_focus].redraw)
open_button = Button(window, text="Open", font=("Courier New bold", 20), command=open_file, width=12)
open_button.place(relx=.08, rely=.1, anchor=CENTER)
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
save_button = Button(window, text="Save", font=("Courier New bold", 20), command=save_file, width=12)
save_button.place(relx=.08, rely=.15, anchor=CENTER)
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
save_as_button = Button(window, text="Save As", font=("Courier New bold", 20), command=save_as_file, width=12)
save_as_button.place(relx=.08, rely=.2, anchor=CENTER)
def copy_contents():
    current_focus = main_notebook.index("current")
    contents = text_boxes[current_focus].get(1.0, END)
    copy(contents)
copy_button = Button(window, text="Copy", font=("Courier New bold", 20), command=copy_contents, width=12)
copy_button.place(relx=.08, rely=.25, anchor=CENTER)
def paste_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].insert(INSERT, paste())
    text_boxes[current_focus].redraw()
paste_button = Button(window, text="Paste", font=("Courier New bold", 20), command=paste_contents, width=12)
paste_button.place(relx=.08, rely=.3, anchor=CENTER)
def clear_contents():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].delete(1.0, END)
    text_boxes[current_focus].redraw()
clear_button = Button(window, text="Clear-Text", font=("Courier New bold", 20), command=clear_contents, width=12)
clear_button.place(relx=.08, rely=.35, anchor=CENTER)
def clear_terminal():
    the_terminal.clear()
clear_terminal_button = Button(window, text="Clear-CMD", font=("Courier New bold", 20), command=clear_terminal, width=12)
clear_terminal_button.place(relx=.08, rely=.4, anchor=CENTER)
def create_template():
    current_focus = main_notebook.index("current")
    temp_name_pop_up(text_boxes[current_focus], color_mode = color_mode)
create_template_button = Button(window, text="Create-Temp", font=("Courier New bold", 20), command=create_template, width=12)
create_template_button.place(relx=.08, rely=.45, anchor=CENTER)
def open_template():
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].open_template(color_mode = color_mode)
open_template_button = Button(window, text="Open-Temp", font=("Courier New bold", 20), command=open_template, width=12)
open_template_button.place(relx=.08, rely=.5, anchor=CENTER)
def delete_template():
    temp_destroy_pop_up(color_mode = color_mode)
delete_template_button = Button(window, text="Delete-Temp", font=("Courier New bold", 20), command=delete_template, width=12)
delete_template_button.place(relx=.08, rely=.55, anchor=CENTER)
def find_replace(event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].make_find_and_replace(color_mode = color_mode)
find_replace_button = Button(window, text="Find/Replace", font=("Courier New bold", 20), command=find_replace, width=12)
find_replace_button.place(relx=.08, rely=.6, anchor=CENTER)
window.bind("<Command-f>", find_replace)
def stackoverflow(event=None):
    webbrowser.open("https://stackoverflow.com/")
def ask_StackOverflow_question(event=None):
    webbrowser.open("https://stackoverflow.com/questions/ask")
def reset_syntax_colors(event=None):
    main_text_box.reset_syntax(color_mode = color_mode)
def change_color_mode(event=None):
    global color_mode
    if color_mode == "Dark":
        color_mode = "light"
        bg = "white"
        fg = "#4f4c4d"
    else:
        color_mode = "Dark"
        bg = "#4f4c4d"
        fg = "white"
    for i in range(len(text_boxes)):
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
    commands_label.configure(bg=bg, fg=fg)
    the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
    open_button.configure(highlightbackground=bg)
    save_button.configure(highlightbackground=bg)
    save_as_button.configure(highlightbackground=bg)
    copy_button.configure(highlightbackground=bg)
    paste_button.configure(highlightbackground=bg)
    clear_button.configure(highlightbackground=bg)
    clear_terminal_button.configure(highlightbackground=bg)
    create_template_button.configure(highlightbackground=bg)
    open_template_button.configure(highlightbackground=bg)
    delete_template_button.configure(highlightbackground=bg)
    find_replace_button.configure(highlightbackground=bg)
    change_color_mode_button.configure(highlightbackground=bg)
    report_a_bug_button.configure(highlightbackground=bg)
    run_button.configure(highlightbackground=bg)
    quit_button.configure(highlightbackground=bg)
    settings_button.configure(highlightbackground=bg)
change_color_mode_button = Button(window, text="Change-Color", font=("Courier New bold", 20), command=change_color_mode, width=12)
change_color_mode_button.place(relx=.08, rely=.65, anchor=CENTER)
def report_a_bug(event=None):
    report_bug(color_mode = color_mode)
report_a_bug_button = Button(window, text="Report A Bug", font=("Courier New bold", 20), command=report_a_bug, width=12)
report_a_bug_button.place(relx=.08, rely=.7, anchor=CENTER)
def run_file(event=None):
    if event != None:
        if event.keysym == "F5":
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
run_button = Button(window, text="▶", image= run_img, font=("Courier New bold", 25), command=run_file)
run_button.place(relx=.975, rely=.035, anchor=CENTER)
window.bind("<Command-r>", run_file)
window.bind("<F5>", run_file)
def window_destroy(event=None):
    window.destroy()
window.bind("<Command-w>", close_tab)
quit_button = Button(window, text="Quit", font=("Courier New bold", 15), command=window_destroy)
quit_button.pack(anchor="s", side="right")
menubar = Menu(window)
app_menu = Menu(menubar, name="apple")
menubar.add_cascade(menu=app_menu)
edit_menu = Menu(menubar, tearoff=False)
app_menu.add_command(label='About ' + "JDE", command=about)
app_menu.add_separator()
edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=edit_menu, label="Edit")
edit_menu.add_command(label="Open File", command=open_file)
edit_menu.add_command(label="Save File", command=save_file)
edit_menu.add_command(label="Save As File", command=save_as_file)
edit_menu.add_cascade(label="Clear Text", command= lambda: clear_contents(None))
edit_menu.add_command(label="Copy", command= lambda: copy_contents(None))
edit_menu.add_command(label="Paste", command= lambda: paste_contents(None))
def tabs_to_spaces (event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].tabs_to_spaces()
def spaces_to_tabs (event=None):
    current_focus = main_notebook.index("current")
    text_boxes[current_focus].spaces_to_tabs()
edit_menu.add_command(label="Tabs to Spaces", command=tabs_to_spaces)
edit_menu.add_command(label="Spaces to Tabs", command=spaces_to_tabs)
edit_menu.add_command(label="Create Tab", command=create_new_tab)
edit_menu.add_command(label="Close Tab", command=close_tab)
template_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=template_menu, label="Templates")
template_menu.add_command(label="Create Template", command=create_template)
template_menu.add_command(label="Open Template", command=open_template)
template_menu.add_command(label="Delete Template", command=delete_template)
run_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=run_menu, label="Run")
run_menu.add_command(label="Run File", command=run_file)
window.config(menu=menubar)
help_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=help_menu, label="Help")
help_menu.add_command(label= "Shortcuts", command= lambda: shortcuts_page(color_mode = color_mode))
def open_python_docs():
    webbrowser.open("https://docs.python.org/3/library/")
def help(event=None):
    if event != None:
        if event.keysym == "F1":
            current_focus = main_notebook.index("current")
            line_contents = text_boxes[current_focus].get("insert linestart", "insert lineend")
            current_insert = int(text_boxes[current_focus].index("insert").split(".")[1])
            edited_line = line_contents[current_insert:] + line_contents[:current_insert-1]
            text_boxes[current_focus].delete("insert linestart", "insert lineend")
            text_boxes[current_focus].insert("insert linestart", edited_line)
            help_info(color_mode = color_mode)
window.bind("<F1>", help)
window.bind("<Alt_L>", help)
window.bind("<Alt_R>", help)
def open_github():
    webbrowser.open("https://github.com/")
help_menu.add_command(label="Main Help", command=help)
help_menu.add_command(label="Python Documentation", command=open_python_docs)
stack_menu = Menu(help_menu, tearoff=False)
help_menu.add_cascade(menu=stack_menu, label="Stackoverflow")
stack_menu.add_command(label="Open StackOverflow", command=stackoverflow)
stack_menu.add_command(label="Ask StackOverflow Question", command=ask_StackOverflow_question)
help_menu.add_command(label="Open GitHub", command=open_github)
help_menu.add_command(label="Report A Bug", command=report_a_bug)
settings_button = Button(window, text="Settings", font=("Courier New bold", 15), command= lambda: settings(color_mode=color_mode))
settings_button.pack(anchor="s", side="left")
window.configure(bg=bg)
main_text_box.configure(bg=bg)
main_text_box.change_color("{}".format(color_mode))
main_label.configure(bg=bg, fg=fg)
commands_label.configure(bg=bg, fg=fg)
the_terminal.configure(bg=bg, fg=fg, insertbackground=fg)
open_button.configure(highlightbackground=bg)
save_button.configure(highlightbackground=bg)
save_as_button.configure(highlightbackground=bg)
copy_button.configure(highlightbackground=bg)
paste_button.configure(highlightbackground=bg)
clear_button.configure(highlightbackground=bg)
clear_terminal_button.configure(highlightbackground=bg)
create_template_button.configure(highlightbackground=bg)
open_template_button.configure(highlightbackground=bg)
delete_template_button.configure(highlightbackground=bg)
find_replace_button.configure(highlightbackground=bg)
change_color_mode_button.configure(highlightbackground=bg)
report_a_bug_button.configure(highlightbackground=bg)
run_button.configure(highlightbackground=bg)
quit_button.configure(highlightbackground=bg)
settings_button.configure(highlightbackground=bg)
main_notebook.bind('<Double-Button-1>', create_new_tab)
text_boxes[0].insert("insert",  "#  .----------------.  .----------------.  .----------------. \n# | .--------------. || .--------------. || .--------------. |\n# | |     _____    | || |  ________    | || |  _________   | |\n# | |    |_   _|   | || | |_   ___ `.  | || | |_   ___  |  | |\n# | |      | |     | || |   | |   `. \ | || |   | |_  \_|  | |\n# | |   _  | |     | || |   | |    | | | || |   |  _|  _   | |\n# | |  | |_' |     | || |  _| |___.' / | || |  _| |___/ |  | |\n# | |  `.___.'     | || | |________.'  | || | |_________|  | |\n# | |              | || |              | || |              | |\n# | '--------------' || '--------------' || '--------------' |\n#  '----------------'  '----------------'  '----------------' \n\n# Welcome to Josh's Development Environment!")
window.after(150, text_boxes[0].redraw)
height_widget_list = [main_label, main_notebook, the_terminal, quit_button, settings_button]
width_height_list = [commands_label, main_notebook, quit_button]
widget_list = [main_label, main_notebook, the_terminal, quit_button, settings_button, commands_label]
for widget in widget_list:
    widget.update()
height_required_list = []
width_required_list = []
for widget in height_widget_list:
    height_required_list.append(int(widget.winfo_height()))
for widget in width_height_list:
    width_required_list.append(int(widget.winfo_width()))
minimum_height = 0
for height in height_required_list:
    minimum_height += height
minimum_width = 0
for width in width_required_list:
    minimum_width += width
window.geometry("{}x{}".format(minimum_width, minimum_height))
window.resizable(False, False)
window.mainloop()
