from tkinter import *
from tkinter.ttk import *
from custom_widgets import *
from ttkScrollableNotebook import *
import os
import sys

if __name__ == "__main__":
    root = Tk()
    # Set style as clam
    style = Style()
    style.theme_use("clam")
    root.title("Test")
    root.geometry("800x600+0+0")
    # Create a scrollable notebook
    notebook = ScrollableNotebook(root, tabmenu=True, wheelscroll=True)
    notebook.pack(fill=BOTH, expand=True)
    #Create restart button
    def restart():
        os.execv(sys.executable, ["python"] + sys.argv)
    restart_button = Button(root, text="Restart", command=restart)
    restart_button.pack(side=BOTTOM)
    # Create a frame for each tab
    for i in range(14):
        frame = ultra_text(notebook, color_mode = "Light", window = notebook)
        # Add the frame to the notebook
        notebook.add(frame, text="Tab %d" % i)
        # Create a label in the frame
    root.after(100, lambda: notebook.select(0))
    root.mainloop()