import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from widgets import menu

root = Tk()
root.title("Список задач")
root.geometry("600x400")

frame = Frame(
   root,
   padx=10,
   pady=10,
   background= 'linen'
)
frame.pack(fill='both')


button_menu = Button(root, text='Меню', command=menu)
button_menu.place(x=300,y=0)

frame.pack(expand=True)

root.mainloop()
