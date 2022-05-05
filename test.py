# from tkinter import *
# from tkinter.ttk import *
# from custom_widgets import *
# from ttkScrollableNotebook import *
# import os
# import sys

# if __name__ == "__main__":
#     root = Tk()
#     # Set style as clam
#     style = Style()
#     style.theme_use('clam')
#     root.title("Test")
#     root.geometry("800x600+0+0")
#     # Create a scrollable notebook
#     notebook = ScrollableNotebook(root, tabmenu=True, wheelscroll=True)
#     notebook.pack(fill=BOTH, expand=True)
#     #Create restart button
#     def restart():
#         os.execv(sys.executable, ['python'] + sys.argv)
#     restart_button = Button(root, text="Restart", command=restart)
#     restart_button.pack(side=BOTTOM)
#     # Create a frame for each tab
#     for i in range(14):
#         frame = ultra_text(notebook, color_mode = "Light", window = notebook)
#         # Add the frame to the notebook
#         notebook.add(frame, text="Tab %d" % i)
#         # Create a label in the frame
#     root.after(100, lambda: notebook.select(0))
#     root.mainloop()

# from tkinter import *

# window = Tk()
# window.title("Test after loop idea")
# #Create 3 after loops that are recursive
# #create a window that allows the user to cancel the after loops
# loop_list = []
# def create_loop(loop_count):
#     global loop_list
#     for i in range(3):
#         the_loop = window.after(5000, lambda:keep_loop(i))
#         loop_list.append(the_loop)
#         #Update the command in the_loop
#         the_loop.config(command=lambda:keep_loop(i))
# def keep_loop(index):
#     #Issue: doesn't update the index num when canceled
#     print(index)
#     loop_list.__delitem__(index)
#     loop_list.append(window.after(5000, lambda:keep_loop(index)))
# def cancel(index):
#     global loop_list
#     print(loop_list)
#     window.after_cancel(loop_list[index])
#     loop_list.__delitem__(index)
#     print(loop_list)
# cancel_button = Button(window, text="Cancel", command=lambda:cancel(1))
# cancel_button.pack()
# window.after(1, lambda:create_loop(3))
# window.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()
# root.geometry('600x600')

# min_w = 50 # Minimum width of the frame
# max_w = 200 # Maximum width of the frame
# cur_width = min_w # Increasing width of the frame
# expanded = False # Check if it is completely exanded

# def expand():
#     global cur_width, expanded
#     cur_width += 10 # Increase the width by 10
#     rep = root.after(5,expand) # Repeat this func every 5 ms
#     frame.config(width=cur_width) # Change the width to new increase width
#     if cur_width >= max_w: # If width is greater than maximum width 
#         expanded = True # Frame is expended
#         root.after_cancel(rep) # Stop repeating the func
#         fill()

# def contract():
#     global cur_width, expanded
#     cur_width -= 10 # Reduce the width by 10 
#     rep = root.after(5,contract) # Call this func every 5 ms
#     frame.config(width=cur_width) # Change the width to new reduced width
#     if cur_width <= min_w: # If it is back to normal width
#         expanded = False # Frame is not expanded
#         root.after_cancel(rep) # Stop repeating the func
#         fill()

# def fill():
#     if expanded: # If the frame is exanded
#         # Show a text, and remove the image
#         home_b.config(text='Home',image='',font=(0,21))
#         set_b.config(text='Settings',image='',font=(0,21))
#         ring_b.config(text='Bell Icon',image='',font=(0,21))
#     else:
#         # Bring the image back
#         home_b.config(image=home,font=(0,21))
#         set_b.config(image=settings,font=(0,21))
#         ring_b.config(image=ring,font=(0,21))

# # Define the icons to be shown and resize it
# home = PhotoImage(file='Run.png') # Make sure the image size is comparable to the minimum frame width
# settings = PhotoImage(file='Run.png')
# ring = PhotoImage(file='Run.png')

# root.update() # For the width to get updated
# frame = Frame(root,bg='orange',width=50,height=root.winfo_height())
# frame.grid(row=0,column=0) 

# # Make the buttons with the icons to be shown
# home_b = Button(frame,image=home,bg='orange',relief='flat')
# set_b = Button(frame,image=settings,bg='orange',relief='flat')
# ring_b = Button(frame,image=ring,bg='orange',relief='flat')

# # Put them on the frame
# home_b.grid(row=0,column=0,pady=10)
# set_b.grid(row=1,column=0,pady=50)
# ring_b.grid(row=2,column=0)

# # Bind to the frame, if entered or left
# frame.bind('<Enter>',lambda e: expand())
# frame.bind('<Leave>',lambda e: contract())

# # So that it does not depend on the widgets inside the frame
# frame.grid_propagate(False)

# root.mainloop()


# import tkinter as tk

# class ToolTipLabel(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         self.l1 = tk.Label(self, text="Hover over me")
#         self.l2 = tk.Label(self, text="", width=40)
#         self.l1.pack(side="top")
#         self.l2.pack(side="top", fill="x")

#         self.l1.bind("<Enter>", self.on_enter)
#         self.l1.bind("<Leave>", self.on_leave)

#     def on_enter(self, event):
#         self.l2.configure(text="Hello world")

#     def on_leave(self, enter):
#         self.l2.configure(text="")

# if __name__ == "__main__":
#     root = tk.Tk()
#     ToolTipLabel(root).pack(side="top", fill="both", expand="true")
#     root.mainloop()


from tkinter import *
from custom_widgets import *
root = Tk()
root.title("Test")
root.geometry("800x600+0+0")
a_button = Button(root, text="Button", font=("Courier New bold", 25), command=lambda:print("Button pressed"))
a_button.pack()
ToolTip(a_button, text="This is a button", window=root)
run_img = PhotoImage(file="Run.png")
run_button = Button(root, image=run_img, command=lambda:print("Run"))
run_button.pack()
ToolTip(run_button, text="Runs file", window=root)
#create 5 buttons with tooltips
for i in range(5):
    button = Button(root, text=f"Button {i}", font=("Courier New bold", 25), command=lambda:print(f"Button {i} pressed"))
    button.pack()
    ToolTip(button, text=f"Button {i}", window=root)
root.mainloop()