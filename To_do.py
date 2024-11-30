import os
import tkinter as tk
from tkinter import messagebox, simpledialog


def show_tasks():
    task_list.delete(0, tk.END)
    if tasks:
        for task in tasks:
            task_list.insert(tk.END, task)
    else:
        task_list.insert(tk.END, "No tasks found.")


def add_task():
    new_task = simpledialog.askstring("Add Task", "Enter the task:")
    if new_task:
        tasks.append(new_task)
        save_tasks_to_file()
        show_tasks()
        messagebox.showinfo("Success", "Task added successfully!")


def update_task():
    try:
        selected_index = task_list.curselection()[0]
        if selected_index >= 0:
            updated_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if updated_task:
                tasks[selected_index] = updated_task
                save_tasks_to_file()
                show_tasks()
                messagebox.showinfo("Success", "Task updated successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")


def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        if selected_index >= 0:
            task_to_delete = tasks.pop(selected_index)
            save_tasks_to_file()
            show_tasks()
            messagebox.showinfo("Success", f"Task '{task_to_delete}' deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def save_tasks_to_file():
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def load_tasks_from_file():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    return []


file_path = "todo_list.txt"
tasks = load_tasks_from_file()

app = tk.Tk()
app.title("To-Do List Application")


frame = tk.Frame(app)
frame.pack(pady=10)

task_list = tk.Listbox(frame, width=50, height=15, selectmode=tk.SINGLE)
task_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)


button_frame = tk.Frame(app)
button_frame.pack(pady=10)

btn_show = tk.Button(button_frame, text="Show Tasks", command=show_tasks, width=20)
btn_show.pack(pady=5)

btn_add = tk.Button(button_frame, text="Add Task", command=add_task, width=20)
btn_add.pack(pady=5)

btn_update = tk.Button(button_frame, text="Update Task", command=update_task, width=20)
btn_update.pack(pady=5)

btn_delete = tk.Button(button_frame, text="Delete Task", command=delete_task, width=20)
btn_delete.pack(pady=5)

btn_exit = tk.Button(button_frame, text="Exit", command=app.quit, width=20)
btn_exit.pack(pady=5)

show_tasks()

app.mainloop()
