import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re

# функция очищения окна
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# функция вызова меню с необходимыми кнопками
def show_menu(frame):
    clear_frame(frame)
    
    btn_tack = tk.Button(frame, text='Показать все задачи',
                         command=lambda: show_tasks(frame))
    btn_tack.place(x=200, y=50, width=200)

    btn_add = tk.Button(frame, text='Добавить задачу',
                        command=lambda: add_tasks(frame))
    btn_add.place(x=200, y=100, width=200)

    btn_edit = tk.Button(frame, text='Редактировать задачу',
                         command=lambda: edit_task(frame))
    btn_edit.place(x=200, y=150, width=200)

    btn_mark = tk.Button(frame, text='Отметить как выполненную',
                         command=lambda: complete_task(frame))
    btn_mark.place(x=200, y=200, width=200)

    btn_del = tk.Button(frame, text='Удалить задачу',
                        command=lambda: delete_task(frame))
    btn_del.place(x=200, y=250, width=200)

# показать все задачи
def show_tasks(frame, sort_by_status=False):
    clear_frame(frame)
    
    # сортировка
    if sort_by_status:
        btn_sort = tk.Button(frame, text='Показать все',
                             command=lambda: show_tasks(frame, sort_by_status=False))
        btn_sort.place(x=400, y=10, width=150)
    else:
        btn_sort = tk.Button(frame, text='Сортировать',
                             command=lambda: show_tasks(frame, sort_by_status=True))
        btn_sort.place(x=400, y=10, width=150)
    
    with open('todo.txt', 'r', encoding='utf-8') as task_file:
        tasks = task_file.readlines()

    if not tasks:
        lbl = tk.Label(frame, text="Список задач пуст", background='linen')
        lbl.place(x=230, y=50)
    else:
        if sort_by_status:
            # Сортировка
            incomplete = [t for t in tasks if '[ ]' in t]
            completed = [t for t in tasks if '[X]' in t]
            tasks = incomplete + completed
            
        y_position = 50
        for task in tasks:
            task_lbl = tk.Label(frame, text=task.strip(), background='linen',
                                justify='left', anchor='w')
            task_lbl.place(x=150, y=y_position, width=350)
            y_position += 40
            
    
# добавить задачу
def add_tasks(frame):
    clear_frame(frame)
    
    lbl = tk.Label(frame, text="Введите новую задачу:", background='linen')
    lbl.place(x=200, y=50, width=200)

    entry_task = tk.Entry(frame, width=30)
    entry_task.place(x=200, y=80, width=200)
    entry_task.focus()

    # сохранение новой задачи
    def save_task():
        task = entry_task.get()
        if task.strip():
            with open('todo.txt', 'r', encoding='utf-8') as f:
                num_task = len(f.readlines()) + 1
            # дата
            current_date = datetime.now().strftime('%d.%m.%Y')
            
            with open('todo.txt', 'a', encoding='utf-8') as task_file:
                task_file.write(f'[ ] {num_task}. {task} ({current_date})\n')
            
            entry_task.delete(0, tk.END)
            show_menu(frame)

    btn_save = tk.Button(frame, text='Сохранить', command=save_task)
    btn_save.place(x=200, y=120, width=200)

# редактировать задачу
def edit_task(frame):
    clear_frame(frame)
    
    lbl = tk.Label(frame, text="Введите номер задачи для редактирования:", background='linen')
    lbl.place(x=175, y=50, width=250)

    entry_num = tk.Entry(frame, width=10)
    entry_num.place(x=275, y=80, width=50)
    entry_num.focus()

    lbl2 = tk.Label(frame, text="Введите новый текст задачи:", background='linen')
    lbl2.place(x=190, y=120, width=220)

    entry_task = tk.Entry(frame, width=30)
    entry_task.place(x=200, y=150, width=200)

    def save_edit():
        task_num = int(entry_num.get())
        new_text = entry_task.get()
            
        with open('todo.txt', 'r', encoding='utf-8') as f:
            tasks = f.readlines()
            
        if task_num < 1 or task_num > len(tasks):
            messagebox.showerror("Ошибка", "Неверный номер задачи!")
            return
    
        original = tasks[task_num - 1]
        status = '[X]' if '[X]' in original else '[ ]'
        
        # извлечение старой даты
        date_match = re.search(r'\(\d{2}\.\d{2}\.\d{4}\)', original)
        date_str = date_match.group() if date_match else f'({datetime.now().strftime("%d.%m.%Y")})'
            
        # сохранение    
        tasks[task_num - 1] = f'{status} {task_num}. {new_text} {date_str}\n'
            
        with open('todo.txt', 'w', encoding='utf-8') as f:
            f.writelines(tasks)
            
        show_menu(frame)

    btn_save = tk.Button(frame, text='Сохранить', command=save_edit)
    btn_save.place(x=200, y=190, width=200)


# отметить задачу как выполненную
def complete_task(frame):
    clear_frame(frame)
    
    with open('todo.txt', 'r', encoding='utf-8') as task_file:
        tasks = task_file.readlines()

    y_position = 50
    for i, task in enumerate(tasks):
        task_lbl = tk.Label(frame, text=task.strip(), background='linen')
        task_lbl.place(x=150, y=y_position, width=300)
                
        if '[ ]' in task:
            def mark_done(index=i):
                with open('todo.txt', 'r', encoding='utf-8') as f:
                    all_tasks = f.readlines()
                        
                all_tasks[index] = all_tasks[index].replace('[ ]', '[X]', 1)
                        
                with open('todo.txt', 'w', encoding='utf-8') as f:
                    f.writelines(all_tasks)
                        
                complete_task(frame) 
                    
            btn_done = tk.Button(frame, text='✓', width=3, command=mark_done)
            btn_done.place(x=460, y=y_position)
                
        y_position += 40

# удалить задачу
def delete_task(frame):
    clear_frame(frame)
    
    with open('todo.txt', 'r', encoding='utf-8') as task_file:
        tasks = task_file.readlines()

    y_position = 50
    for i, task in enumerate(tasks):
        task_lbl = tk.Label(frame, text=task.strip(), background='linen')
        task_lbl.place(x=150, y=y_position, width=300)
                
        def delete_one(index=i):
            with open('todo.txt', 'r', encoding='utf-8') as f:
                all_tasks = f.readlines()
                    
            all_tasks.pop(index)
                    
            with open('todo.txt', 'w', encoding='utf-8') as f:
                for num, t in enumerate(all_tasks, 1):
                    content = t.split('. ', 1)[1] if '. ' in t else t
                    f.write(f'[ ] {num}. {content}')
                    
            delete_task(frame) 
                
        btn_delete = tk.Button(frame, text='✕', width=3, command=delete_one)
        btn_delete.place(x=460, y=y_position)
                
        y_position += 40