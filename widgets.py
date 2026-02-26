import tkinter as tk

tack_file = open('todo.txt')

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_menu(frame):
    clear_frame(frame)
    
    btn_tack = tk.Button(frame, text='Показать все задачи', command=lambda: show_tasks(frame))
    btn_tack.place(x=200, y=50, width=200)
    
    btn3 = tk.Button(frame, text='Добавить задачу')
    btn3.place(x=200, y=100, width=200)
    
    btn4 = tk.Button(frame, text='Отметить как выполненную')
    btn4.place(x=200, y=150, width=200)
    
    btn5 = tk.Button(frame, text='Удалить задачу')
    btn5.place(x=200, y=200, width=200)

def show_tasks(frame):
    clear_frame(frame)
    
    task_list = tack_file.readlines()
    lbl = tk.Label(frame, text=f"{task_list}", background='linen')
    lbl.place(x=200, y=50)