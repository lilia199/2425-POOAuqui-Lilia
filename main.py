import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear el campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Crear la lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Funciones para manejar las tareas
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} - Completada")
        task_listbox.itemconfig(tk.END, {'bg':'light green'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para completar")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

# Crear los botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Completar Tarea", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Asignar atajos de teclado
root.bind('<Return>', lambda event: add_task())
root.bind('<c>', lambda event: complete_task())
root.bind('<Delete>', lambda event: delete_task())
root.bind('<Escape>', lambda event: root.quit)

# Ejecutar la aplicación
root.mainloop()
