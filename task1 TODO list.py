import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App")

        self.tasks = []

        # Create UI elements
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all_tasks)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def remove_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.listbox.delete(index)
            messagebox.showinfo("Task Removed", f"Task '{removed_task}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all_tasks(self):
        confirmed = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks = []
            self.listbox.delete(0, tk.END)
            messagebox.showinfo("Tasks Cleared", "All tasks cleared.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
