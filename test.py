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


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
from tkinter import *
from collections import deque
 
 
class Window:
    def __init__(self, master):
        self.master = master
        self.master.option_add("*Font", "Verdana 12")
 
        self.Main = Frame(self.master)
 
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
 
        self.L1 = Label(self.Main, text = "This is my Code Editor")
        self.L1.pack(padx = 5, pady = 5)
 
 
        #---------
 
        self.T1 = Text(self.Main, width = 90, height = 25)
 
        self.T1.tag_configure("orange", foreground = "orange", font = "Verdana 12")
        self.T1.tag_configure("blue", foreground = "blue", font = "Verdana 12")
        self.T1.tag_configure("purple", foreground = "purple", font = "Verdana 12")
        self.T1.tag_configure("green", foreground = "green", font = "Verdana 12")
        self.T1.tag_configure("red", foreground = "red", font = "Verdana 12")
 
        self.tags = ["orange", "blue", "purple", "green", "red"]
 
        self.wordlist = [ ["class", "def", "for", "if", "else", "elif", "import", "from", "as", "break", "while"],
                          ["int", "string", "float", "bool", "__init__"],
                          ["pygame", "tkinter", "sys", "os", "mysql"],
                          ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] ]
 
        self.T1.bind("<Return>", lambda event: self.indent(event.widget))
         
        self.T1.pack(padx = 5, pady = 5)
 
        #---------
 
        self.menu = Menu(self.Main)
        self.menu.add_command(label = "Print", command = self.print_stack)
        self.menu.add_command(label = "Undo", command = self.undo)
        self.menu.add_command(label = "Redo", command = self.redo)
 
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Print", width = 8, command = self.display)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B2 = Button(self.Main, text = "Clear", width = 8, command = self.clear)
        self.B2.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B3 = Button(self.Main, text = "Undo", width = 8, command = self.undo)
        self.B3.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B4 = Button(self.Main, text = "Redo", width = 8, command = self.redo)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)
 
        self.Main.pack(padx = 5, pady = 5)
 
 
    def tagHighlight(self):
        start = "1.0"
        end = "end"
         
        for mylist in self.wordlist:
            num = int(self.wordlist.index(mylist))
 
            for word in mylist:
                self.T1.mark_set("matchStart", start)
                self.T1.mark_set("matchEnd", start)
                self.T1.mark_set("SearchLimit", end)
 
                mycount = IntVar()
                 
                while True:
                    index= self.T1.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
 
                    if index == "": break
                    if mycount.get() == 0: break
 
                    self.T1.mark_set("matchStart", index)
                    self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
 
                    preIndex = "%s-%sc" % (index, 1)
                    postIndex = "%s+%sc" % (index, mycount.get())
                     
                    if self.check(index, preIndex, postIndex):
                        self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")
                         
 
    def check(self, index, pre, post):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
 
        if self.T1.get(pre) == self.T1.get(index):
            pre = index
        else:
            if self.T1.get(pre) in letters:
                return 0
 
        if self.T1.get(post) in letters:
            return 0
 
        return 1
 
 
    def scan(self):
        start = "1.0"
        end = "end"
        mycount = IntVar()
 
        regex_patterns = [r'".*"', r'#.*']
 
        for pattern in regex_patterns:
            self.T1.mark_set("start", start)
            self.T1.mark_set("end", end)
 
            num = int(regex_patterns.index(pattern))
 
            while True:
                index = self.T1.search(pattern, "start", "end", count=mycount, regexp = True)
 
                if index == "": break
 
                if (num == 1):
                    self.T1.tag_add(self.tags[4], index, index + " lineend")
                elif (num == 0):
                    self.T1.tag_add(self.tags[3], index, "%s+%sc" % (index, mycount.get()))
 
                self.T1.mark_set("start", "%s+%sc" % (index, mycount.get()))
 
 
    def indent(self, widget):
 
        index1 = widget.index("insert")
        index2 = "%s-%sc" % (index1, 1)
        prevIndex = widget.get(index2, index1)
 
        prevIndentLine = widget.index(index1 + "linestart")
        print("prevIndentLine ",prevIndentLine)
        prevIndent = self.getIndex(prevIndentLine)
        print("prevIndent ", prevIndent)
 
 
        if prevIndex == ":":
            widget.insert("insert", "\n" + "    ")
            widget.mark_set("insert", "insert + 1 line + 4char")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "    ")
                widget.mark_set("insert", "insert + 4 chars")
                prevIndentLine += "+5c"
            return "break"
         
        elif prevIndent != prevIndentLine:
            widget.insert("insert", "\n")
            widget.mark_set("insert", "insert + 1 line")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "    ")
                widget.mark_set("insert", "insert + 4 chars")
                prevIndentLine += "+5c"
            return "break"
 
 
    def getIndex(self, index):
        while True:
            if self.T1.get(index) == " ":
                index = "%s+%sc" % (index, 1)
            else:
                return self.T1.index(index)
            
                    
    def update(self):
        self.stackify()
        self.tagHighlight()
        self.scan()
 
    def display(self):
        print(self.T1.get("1.0", "end"))     
 
    def clear(self):
        self.T1.delete("1.0", "end")
 
    def stackify(self):
        self.stack.append(self.T1.get("1.0", "end - 1c"))
        if self.stackcursor < 9: self.stackcursor += 1
 
    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def print_stack(self):
        i = 0
        for stack in self.stack:
            print(str(i) + " " + stack)
            i += 1
 
                      
root = Tk()
window = Window(root)
root.bind("<Key>", lambda event: window.update())
root.mainloop()