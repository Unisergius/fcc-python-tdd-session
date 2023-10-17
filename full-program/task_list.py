# task_list.py
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self):
        task_to_complete = input("Enter the task to mark as complete: ")
        if task_to_complete in self.tasks:
            self.tasks.remove(task_to_complete)
            completed_task = f"{task_to_complete} (completed)"
            self.tasks.append(completed_task)
        else:
            raise ValueError("Task not found in the task list")

    def remove_task(self, task):
        # Implement removal logic
        self.tasks.remove(task)

