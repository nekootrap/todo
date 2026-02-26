import tkinter as tk
from widgets import show_menu, show_tasks

root = tk.Tk()
root.title("Список задач")
root.geometry("600x400")

header_frame = tk.Frame(root, background='gray25', height=50)
header_frame.pack(fill='x', side='top')

frame = tk.Frame(root, background='linen')
frame.pack(fill='both', expand=True)

btn_menu = tk.Button(header_frame,
                     text='Главное меню',
                     command=lambda: show_menu(frame))
btn_menu.pack(pady=10)

show_menu(frame)

root.mainloop()
