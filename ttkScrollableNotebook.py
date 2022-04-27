from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.ttk import Style
from custom_widgets import *

class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index = self.index("@%d,%d" % (event.x, event.y))
        tab_count = self.index(END)
        if self._active == index:
            if tab_count > 1:
                self.forget(index)
                self.event_generate("<<NotebookTabClosed>>")
            else:
                showerror("Tab Error", "Tab Error Found\n\nLast Tab Cannot Be Closed")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])


class ScrollableNotebook(Frame):
    def __init__(self,parent,wheelscroll=False,tabmenu=False,*args,**kwargs):
        ttk.Frame.__init__(self, parent, *args)
        self.xLocation = 0
        self.notebookContent = ttk.Notebook(self,**kwargs)
        self.notebookContent.pack(fill="both", expand=True)
        self.notebookTab = ttk.Notebook(self,**kwargs)
        self.notebookTab.bind("<<NotebookTabChanged>>",self._tabChanger)
        if wheelscroll==True: self.notebookTab.bind("<MouseWheel>", self._wheelscroll)
        slideFrame = ttk.Frame(self)
        slideFrame.place(relx=1.0, x=0, y=1, anchor=NE)
        self.menuSpace=30
        if tabmenu==True:
            self.menuSpace=50
            bottomTab = ttk.Label(slideFrame, text=" \u2630 ")
            bottomTab.bind("<1>",self._bottomMenu)
            bottomTab.pack(side=RIGHT)
        leftArrow = ttk.Label(slideFrame, text=" \u276E")
        leftArrow.bind("<1>",self._leftSlide)
        leftArrow.pack(side=LEFT, ipady=3)
        rightArrow = ttk.Label(slideFrame, text=" \u276F")
        rightArrow.bind("<1>",self._rightSlide)
        rightArrow.pack(side=RIGHT)
        self.notebookContent.bind("<Configure>", self._resetSlide)

    def _wheelscroll(self, event):
        if event.delta > 0:
            self._leftSlide(event)
        else:
            self._rightSlide(event)

    def _bottomMenu(self,event):
        tabListMenu = Menu(self, tearoff = 0)
        for tab in self.notebookTab.tabs():
            tabListMenu.add_command(label=self.notebookTab.tab(tab, option="text"),command= lambda temp=tab: self.select(temp))
        try: 
            tabListMenu.tk_popup(event.x_root, event.y_root) 
        finally: 
            tabListMenu.grab_release()

    def _tabChanger(self,event):
        try: self.notebookContent.select(self.notebookTab.index("current"))
        except: pass

    def _rightSlide(self,event):
        if self.notebookTab.winfo_width()>self.notebookContent.winfo_width()-self.menuSpace:
            if (self.notebookContent.winfo_width()-(self.notebookTab.winfo_width()+self.notebookTab.winfo_x()))<=self.menuSpace+5:
                self.xLocation-=20
                self.notebookTab.place(x=self.xLocation,y=0)
    def _leftSlide(self,event):
        if not self.notebookTab.winfo_x()== 0:
            if self.xLocation >20:
                self.xLocation=0
                self.notebookTab.place(x=self.xLocation,y=0)
            else:
                self.xLocation+=20
                self.notebookTab.place(x=self.xLocation,y=0)

    def _resetSlide(self,event=None):
        self.notebookTab.place(x=0,y=0)
        self.xLocation = 0

    def add(self,frame,**kwargs):
        if len(self.notebookTab.winfo_children())!=0:
            self.notebookContent.add(frame, text="",state="hidden")
        else:
            self.notebookContent.add(frame, text="")
        self.notebookTab.add(ttk.Frame(self.notebookTab),**kwargs)

    def forget(self,tab_id):
        self.notebookContent.forget(self.__ContentTabID(tab_id))
        self.notebookTab.forget(tab_id)

    def hide(self,tab_id):
        self.notebookContent.hide(self.__ContentTabID(tab_id))
        self.notebookTab.hide(tab_id)

    def identify(self,x, y):
        return self.notebookTab.identify(x,y)

    def index(self,tab_id):
        return self.notebookTab.index(tab_id)

    def __ContentTabID(self,tab_id):
        return self.notebookContent.tabs()[self.notebookTab.tabs().index(tab_id)]

    def insert(self,pos,frame, **kwargs):
        self.notebookContent.insert(pos,frame, **kwargs)
        self.notebookTab.insert(pos,frame,**kwargs)

    def select(self,tab_id):
##        self.notebookContent.select(self.__ContentTabID(tab_id))
        self.notebookTab.select(tab_id)

    def tab(self,tab_id, option=None, **kwargs):
        kwargs_Content = kwargs.copy()
        kwargs_Content["text"] = "" # important
        self.notebookContent.tab(self.__ContentTabID(tab_id), option=None, **kwargs_Content)
        return self.notebookTab.tab(tab_id, option=None, **kwargs)

    def tabs(self):
##        return self.notebookContent.tabs()
        return self.notebookTab.tabs()

    def enable_traversal(self):
        self.notebookContent.enable_traversal()
        self.notebookTab.enable_traversal()


if __name__ == "__main__":
    root = Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (width, height))
    s = Style(root)
    s.theme_use("clam")
    #, tabmenu=True, wheelscroll=True
    notebook = ScrollableNotebook(root, wheelscroll=True, tabmenu=True)
    notebook.place(relx=.5675, rely=.55, anchor=CENTER)
    text_box_list = []
    for i in range(165):
        text_piece = ultra_text(notebook, window=root, color_mode = "Light", width=130, height=30)
        text_box_list.append(text_piece)
        notebook.add(text_piece, text="Number: {}".format(i))
        #, text='Another text')
    current_focus = notebook.index("current")
    # notebook.tab(notebook.index("current"), text_box_list[current_focus].insert("end", "New Tab"))
    root.mainloop()