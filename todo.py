import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def add_task(self):
        task = self.entry_box.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry_box.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.list_box.curselection()[0]
            task = self.entry_box.get()
            if task:
                self.tasks[selected_index]["task"] = task
                self.tasks[selected_index]["completed"] = False
                self.update_listbox()
                self.entry_box.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.list_box.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.list_box.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def load_selected_task(self, event):
        try:
            selected_index = self.list_box.curselection()[0]
            task = self.tasks[selected_index]["task"]
            self.entry_box.delete(0, tk.END)
            self.entry_box.insert(tk.END, task)
        except IndexError:
            pass

    def clear_tasks(self):
        self.tasks = []
        self.update_listbox()

    def update_listbox(self):
        self.list_box.delete(0, tk.END)
        for task_info in self.tasks:
            task_text = task_info["task"]
            if task_info["completed"]:
                task_text = "[Completed] " + task_text
            self.list_box.insert(tk.END, task_text)

    def __init__(self, window):
        self.window = window
        self.window.title("To-Do App")

        # Create and place the Entry widget
        self.entry_box = tk.Entry(window, font=("Helvetica", 14))
        self.entry_box.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        # Create and place the Add Task button
        self.add_button = tk.Button(window, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        # Create and place the Listbox widget
        self.list_box = tk.Listbox(window, font=("Helvetica", 14), selectmode=tk.SINGLE)
        self.list_box.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")
        self.list_box.bind("<<ListboxSelect>>", self.load_selected_task)

        # Create and place the Scrollbar widget
        self.scrollbar = tk.Scrollbar(window, command=self.list_box.yview)
        self.scrollbar.grid(row=1, column=3, pady=10, sticky="ns")
        self.list_box.config(yscrollcommand=self.scrollbar.set)

        # Create and place the Update Task button
        self.update_button = tk.Button(window, text="Update Task", command=self.update_task, font=("Helvetica", 12))
        self.update_button.grid(row=2, column=0, pady=10, sticky="ew")

        # Create and place the Delete Task button
        self.delete_button = tk.Button(window, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        self.delete_button.grid(row=2, column=1, pady=10, sticky="ew")

        # Create and place the Mark Complete button
        self.complete_button = tk.Button(window, text="Mark Complete", command=self.mark_complete,
                                         font=("Helvetica", 12))
        self.complete_button.grid(row=2, column=2, pady=10, sticky="ew")

        # Create and place the Clear Tasks button
        self.clear_button = tk.Button(window, text="Clear Tasks", command=self.clear_tasks, font=("Helvetica", 12))
        self.clear_button.grid(row=2, column=3, pady=10, sticky="ew")

        # Initialize tasks list
        self.tasks = []



if __name__ == "__main__":
    window = tk.Tk()
    app = TodoListApp(window)
    window.mainloop()

