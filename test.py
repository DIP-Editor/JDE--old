# from tkinter import *
# from tkinter.ttk import *
# from custom_widgets import *
# from ttkScrollableNotebook import *


# if __name__ == "__main__":
#     root = Tk()
#     # Set style as clam
#     style = Style()
#     style.theme_use('clam')
#     root.title("Test")
#     root.geometry("800x600")
#     # Create a scrollable notebook
#     notebook = ScrollableNotebook(root, tabmenu=True, wheelscroll=True)
#     notebook.pack(fill=BOTH, expand=True)
#     # Create a frame for each tab
#     for i in range(14):
#         frame = Frame(notebook)
#         # Add the frame to the notebook
#         notebook.add(frame, text="Tab %d" % i)
#         # Create a label in the frame
#         label = Label(frame, text="Tab %d" % i)
#         label.pack(fill=BOTH, expand=True)
#     root.after(100, notebook.tabs())
#     root.mainloop()


from tkinter import *
from tkinter.ttk import *
keywords_list = ["from", "tkinter", "import", "Label", "Button", "Entry"]
class specialText(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = Text(self, width=50, height=10)
        self.text.pack(fill=BOTH, expand=True)
        self.text.insert(END, "# This is a test. Autocomplete works")
        self.text.bind("<Any-KeyRelease>", self._autocomplete)
        self.text.bind("<Tab>", self._handle_tab, add=True)

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
            self.text.insert("    ")
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

if __name__ == "__main__":
    window = Tk()
    window.title("Autocomplete")
    window.geometry("500x500")
    text = specialText(window)
    text.pack(fill=BOTH, expand=True)
    window.mainloop()