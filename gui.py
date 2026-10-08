import tkinter as tk
from tkinter import ttk, messagebox
from classes import Task, TaskManager


class TaskManagerApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Менеджер задач")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Название").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.root, text="Описание").grid(row=1, column=0, sticky="nw", padx=5, pady=2)
        self.desc_text = tk.Text(self.root, height=3, width=38)
        self.desc_text.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(self.root, text="Срок выполнения (ГГГГ-ММ-ДД)").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.date_entry = tk.Entry(self.root, width=40)
        self.date_entry.grid(row=2, column=1, padx=5, pady=2)

        tk.Button(self.root, text="Добавить", command=self.add_task).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(self.root, text="Удалить", command=self.delete_task).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.tasks_listbox = tk.Listbox(self.root, width=60)
        self.tasks_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.update_listbox()

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get().strip()
        if title and description and due_date:
            task = Task(title, description, due_date)
            self.manager.add_task(task)
            self.update_listbox()
            self.clear_inputs()
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля!")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            self.manager.delete_task(selected[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Ошибка", "Выберите задачу в списке!")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.tasks_listbox.insert(tk.END, f"{task.title} (до {task.due_date})")

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
