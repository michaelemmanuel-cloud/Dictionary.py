# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# reversed_numbers = numbers [::-1]
# print(reversed_numbers)
# distance = 13.2
# time_taken = 2

# print(type(12.0))
# print(type(2))
# print('the data type for distance is',type(distance))
# print('the data type for time_taken',type(time_taken))

# height=float(input('enter height'))
# age= int(input('enter age'))
#
#
# if(height > 170 and age > 17):
#   print('welcome')
# else:
#     print('u are not qualified')
# for i in range(4):
#     print(i)
# for i in range (500, 0, -1):
#     print (i)
# names = [] #empty names list
# names.append('michael')
# names.append('john')
# names.append('people')
# names[2] = 'job'
# print (names)
# input('name')
# names = ['dorcas', 'peter']
# for name in names:
#     if (name == 'doracs'):
#         print('ive been looking for u')
#         break
#     else:
#         print('im looking for dorcas')

import tkinter as tk
from tkinter import ttk

def search_word():
    word = entry.get().lower()
    if word:
        result_label.config(text=f"Searching for: {word}")
    else:
        result_label.config(text="Word not found")

root = tk.Tk()
root.title("Dictionary Search")

entry = ttk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

search_button = ttk.Button(root, text="Search", command=search_word)
search_button.grid(row=0, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="", wraplength=300)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
