# test_task_list.py
from unittest.mock import patch
from task_list import TaskList

def test_add_task():
    task_list = TaskList()
    task_list.add_task("Task 1")
    task_list.add_task("Task 2")
    assert task_list.tasks == ["Task 1", "Task 2"]


def test_complete_task():
    # Create an instance of TaskList
    task_list = TaskList()

    # Add a task to the list
    task_list.add_task("Task 1")

    # Mock the input function to simulate user input
    with patch("builtins.input", return_value="Task 1"):
        # Call the complete_task method
        task_list.complete_task()

    # Verify that the task has been marked as completed
    assert "Task 1 (completed)" in task_list.tasks
