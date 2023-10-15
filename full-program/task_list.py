# task_list.py
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        raise NotImplementedError("Not yet implemented")

    def remove_task(self, task):
        # Implement removal logic
        raise NotImplementedError("Not yet implemented")

