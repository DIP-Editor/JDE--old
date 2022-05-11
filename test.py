# #Create a find and replace tool
# def find_string_indexes(string, substring):
#     indexes = []
#     for i in range(len(string)):
#         if string[i:i+len(substring)] == substring:
#             indexes.append(i)
#             length_of_substring = len(substring)
#             string = string[i+length_of_substring:] + string[:i]
#     return indexes
# run = input("Would you like to run the program? (y/n) ")
# if run == "y":
#     main_string = input("Enter a long string: ")
#     if "\\n" in main_string:
#         main_string = main_string.replace("\\n", "\n")
#     find_string = input("Enter a string to find with: ")
#     if "\\n" in find_string:
#         find_string = find_string.replace("\\n", "\n")
#     replace_string = input("Enter a string to replace with: ")
#     if "\\n" in replace_string:
#         replace_string = replace_string.replace("\\n", "\n")
#     indexes = []
#     spot_in_indexes = 0
#     is_first_search = False
#     indexes = find_string_indexes(main_string, find_string)
#     while True:
#         if indexes == []:
#             break
#         action = input("Would you like to find or replace or replace all? (use \"quit\" to exit)")
#         if action == "find":
#             if is_first_search == False:
#                 is_first_search = True
#             else:
#                 spot_in_indexes += 1
#             indexes = find_string_indexes(main_string, find_string)
#             print(indexes[spot_in_indexes])
#         elif action == "replace":
#             main_string = main_string[:indexes[spot_in_indexes]] + replace_string + main_string[indexes[spot_in_indexes]+len(find_string):]
#             print(main_string)
#         elif action == "replace all":
#             for i in range(len(indexes)):
#                 main_string = main_string[:indexes[i]] + replace_string + main_string[indexes[i]+len(find_string):]
#             print(main_string)
#         elif action == "quit":
#             break




# from tkinter import *
# from custom_widgets import *

# root = Tk()
# root.geometry("500x500")
# font = Font(family="Courier New bold", size=15)

# def zoom(new_size):
#     new_size = int(new_size)
#     global size
#     if new_size < 25 and new_size > 13:
#         font.configure(size=new_size)
#         size = new_size

# text = Text(root, font=font)

# text.pack(side="left", fill="both", expand=True)

# size = 15

# root.bind("<Command-=>", lambda event: zoom(int(size)+1))
# root.bind("<Command-Key-minus>", lambda event: zoom(int(size)-1))

# root.mainloop()


# import tkinter as tk
# from tkinter.font import Font

# root = tk.Tk()
# root.geometry("500x500")
# font = Font(family="Courier", size=10)

# def zoom(size):
#     font.configure(size=size)

# zoom_scale = tk.Scale(root, orient='vertical', from_=1, to=500)
# zoom_scale.config(command=zoom)
# text = tk.Text(root, font=font)

# zoom_scale.pack(fill='y', side='right')
# text.pack(side="left", fill="both", expand=True)

# zoom_scale.set(10)

# root.mainloop()
from tkinter import *

def add_image():
    text.image_create(1.0, image = img, justify=CENTER) # Example 1

root = Tk()

text = Text(root)
text.pack(padx = 20, pady = 20)

Button(root, text = "Insert", command = add_image).pack()
img = PhotoImage(file = "extensions.png")
root.mainloop()