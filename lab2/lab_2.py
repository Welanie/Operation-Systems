import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

# выбор файла
def choose_file():
    f = filedialog.askopenfilename()
    if f:
        path.set(f)

# копирование
def copy_file():
    if not path.get():
        return
    dest = filedialog.asksaveasfilename()
    if dest:
        shutil.copy(path.get(), dest)
        messagebox.showinfo("OK", "Файл скопирован")

# перемещение файла
def move_file():
    if not path.get():
        return
    folder = filedialog.askdirectory()
    if folder:
        shutil.move(path.get(), folder)
        messagebox.showinfo("OK", "Файл перемещён")

# размер файла
def get_size():
    if path.get():
        size = os.path.getsize(path.get())
        messagebox.showinfo("Размер", f"{size} байт")

# удаление
def delete_file():
    if path.get():
        os.remove(path.get())
        messagebox.showinfo("OK", "Файл удалён")

# интерфейс
root = tk.Tk()
root.title("Лабораторная 2 - Файлы")
root.geometry("450x250")

path = tk.StringVar()

tk.Label(root, text="Файл:").pack(pady=5)
tk.Entry(root, textvariable=path, width=55).pack()

tk.Button(root, text="Выбрать", command=choose_file).pack(pady=5)
tk.Button(root, text="Копировать", command=copy_file).pack(pady=5)
tk.Button(root, text="Переместить", command=move_file).pack(pady=5)
tk.Button(root, text="Размер", command=get_size).pack(pady=5)
tk.Button(root, text="Удалить", command=delete_file).pack(pady=5)

root.mainloop()