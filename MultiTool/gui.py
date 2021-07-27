import tkinter as tk 
from tkinter import filedialog, Text
import os



root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=900, bg="#444444")
canvas.pack()

frame = tk.Frame(root, bg="#333333")
frame.place(relwidth=0.8, relheight=0.8, relx=0.4, rely=0.1)

openFile = tk.Button(root, text="Discord Tools", padx=10, fg="white", bg="#663a82")
openFile.pack()














root.mainloop()