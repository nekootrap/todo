import tkinter as tk
from tkinter import * 

def menu():
    button_tack = Button(text='Показать все задачи', command=menu)
    button_tack.place(x=300, y=100)
    
    btn3 = Button(text='Добавить задачу', command=menu)
    btn3.place(x=300, y=150)
    
    btn4 = Button(text='Отметить задачу как выполненную', command=menu)
    btn4.place(x=300, y=200)
    
    btn5 = Button( text='Удалить задачу', command=menu)
    btn5.place(x=300, y=250)
    