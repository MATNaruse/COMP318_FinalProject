class ToDoList:
    tasks = []

    class ToDoTask:
        def __init__(self, task):
            self.desc = task
            self.completed = False

        def toggle_complete(self):
            self.completed = not self.completed

    def __init__(self):
        self.tasks = []

    def add_task(self, task_desc):
        self.tasks.append(self.ToDoTask(task_desc))

    def rem_task(self, idx):
        self.tasks.pop(idx)

    def __str__(self):
        out_msg = ""
        for task in self.tasks:
            x_or_o = "[X]" if task.completed else "[ ]"
            out_msg += f"- {x_or_o} {task.desc} \n"
        return out_msg
