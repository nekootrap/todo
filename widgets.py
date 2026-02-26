import tkinter as tk

#функция очищения окна
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#функция вызова меню с необходимыми кнопками
def show_menu(frame):
    clear_frame(frame)
    
    btn_tack = tk.Button(frame, text='Показать все задачи', command=lambda: show_tasks(frame))
    btn_tack.place(x=200, y=50, width=200)
    
    btn3 = tk.Button(frame, text='Добавить задачу', command=lambda: add_tasks(frame))
    btn3.place(x=200, y=100, width=200)
    
    btn4 = tk.Button(frame, text='Отметить как выполненную')
    btn4.place(x=200, y=150, width=200)
    
    btn5 = tk.Button(frame, text='Удалить задачу')
    btn5.place(x=200, y=200, width=200)

#показать все задачи
def show_tasks(frame):
    clear_frame(frame)
    
    task_list = ''
    with open('todo.txt', encoding='utf-8') as task_file:
        for i in task_file:
            task_list += i
    
    lbl = tk.Label(frame, text=f"{task_list}", background='linen')
    lbl.place(x=250, y=50, width=100)
    
    
#добавить задачу
def add_tasks(frame):
    clear_frame(frame)
    
    lbl = tk.Label(frame, text="Введите новую задачу:", background='linen')
    lbl.place(x=200, y=50, width=200)
    
    entry_task = tk.Entry(frame, width=30)
    entry_task.place(x=200, y=80, width=200)
    entry_task.focus()
    
    with open('todo.txt', 'r', encoding='utf-8') as f:
        num_task = len(f.readlines())
    
    # сохранение новой задачи
    def save_task(num_task):
        task = entry_task.get()
        with open('todo.txt', 'a', encoding='utf-8') as task_file:
            task_file.write('[ ] ' + str(num_task) + '. ' + task + '\n')
        entry_task.delete(0, tk.END)
        show_menu(frame)
    
    btn_save = tk.Button(frame,
                         text='Сохранить',
                         command=lambda: save_task(num_task))
    btn_save.place(x=200, y=120, width=200)