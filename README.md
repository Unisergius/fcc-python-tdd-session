# fcc-python-tdd-session

Session about TDD in Python for FCC Algarve

## Workshop Objectives

In this hands-on workshop, participants will:

- Gain practical experience applying TDD principles to a Python project.
- Build a simple todo list application using the TDD methodology.
- Understand the Red-Green-Refactor cycle and its importance in the development process.

## Workshop Structure

The workshop will be divided into the following segments:

1. Introduction to TDD and its benefits.
2. Overview of the Red-Green-Refactor cycle.
3. Hands-on coding session: Building a todo list with TDD.
4. Open discussion and Q&A.

## Coding Exercise Overview

Participants will be guided through the process of building a simple todo list using TDD. Each step of the TDD cycle will be explained, demonstrated, and practiced.

## Q&A

Feel free to ask questions and seek clarification during the session. We encourage an interactive and engaging learning experience.

## FCC - Test Driven Development

We've been solving problems for half a century resorting to algorithms and programming languages. We evolve our own programming style to overcome known problems faster. We build new programming languages that deal with memory management and encapsulate entities into classes, packages to solve common problems like access to accessories connected to our device or quickly sort our lists, package managers for quick access to packages in our application, frameworks for our apps to specialize into web, desktop or mobile sections. Objects and Classes from OOP to help us read and vizualise what we need to develop.

We've also came up with many software development methodologies to dictate the course of your work, giving us a easy pattern to agilize the course of our project.

Many of these methodologies surface. Today we're touching one of them: Test-Driven Development.

Test-Driven Development (TDD) is a software development approach that emphasizes writing tests before writing the actual code.

## Red-Green-Refactor

The process typically follows a simple, iterative cycle known as the "Red-Green-Refactor" cycle.

### Red

Our first step. Creating a test for the feature we want to do and watching it fail. Hence Red, because red is related to a failed task in usual UI design choices.

Developers write a test that defines a specific functionality or improvement without implementing that same functionality. This initial test naturally fails since the corresponding code is not yet written, creating a "Red" state.

### Green

Next, developers write the minimum amount of code necessary to make the test pass, moving the system into a "Green" state.

This step ensures that the implemented code fulfills the requirements set by the test.

### Refactor

Once the test passes, developers move to the "Refactor" phase, where they clean up and optimize the code without changing its behavior. Any change to its behavior that will cause an error to its test, will immediatly be seen and dealt with. This visibility gives you more confidence on your code while you will be able to provide more stability and reliabilty on your tasks.

### Rince-Repeat

Now developers focus on the next feature to implement and put that feature in the "Red" State. GOTO "RED".

## Pros of using TDD

TDD offers several advantages, including the early detection of bugs, improved code design, and increased confidence in code changes.

By continuously writing tests and refining code, developers create a suite of tests that serve as documentation and safety nets during the development process.

TDD encourages a disciplined and incremental approach to coding, leading to more maintainable and reliable software.

## "Enough of your ChatGPT verbosed mumbo-jumbo. How do I jump into TDD?"

Glad you asked.

For this session, we're going to do a simple Python project and see how TDD's phylosophy is going to help you plan your task list project.

## Tools and Setup

Here's the list of tools we need for setting our project up.

### 1. Python

We'll use Python as the programming language. Ensure that you have Python installed. If you don't have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Text Editor or IDE

You'll need a text editor or integrated development environment (IDE) of your preference. Popular choices include:

- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

### 3. Git

We'll be working with version control using Git. If you don't have Git installed, you can download it from the official [Git website](https://git-scm.com/downloads).

### 4. Workshop Repository

Clone this workshop repository to your local machine. You can use the following command in your terminal or command prompt:

```bash
git clone https://github.com/unisergius/fcc-python-tdd-session.git

cd fcc-python-tdd-session
cd your-program
```

Set up virtual environment for python - [Reference](https://docs.python.org/3/library/venv.html)

```sh
# mac
source <venv directory>/bin/activate
```

#### Replace 'pip3' with 'pip' if you're using Python previous to version 3

```sh
pip3 install -r requirements.txt
````

This will install you the necessary packages, specially pytest.

Pytest allows you to run your tests.

### Task List

We need to do a Task List project.
After a meeting we decided that it's important to start with the basic functionality.

We should be able to have an array of tasks. Each task is represented only by its name as a string.

Our program can:

- add tasks to the task list.
- mark tasks as completed by just adding the suffix (completed) at the end of the task's name
- Remove tasks from the task list.

But remember, we're doing it resorting to the TDD pattern.

Let's try it for the Add Task.

#### 1st Red Step

- Write a failing task.

Create a file called test_task_list.py (or task_list_test.py depending on your team's naming convention)
In here we're going to import two objects:

```py
from unittest.mock import patch
from task_list import TaskList
```

From here we can define our tests as python functions and use the assert function to test if they're equal to a certain value.

Note: train yourself from the start to use test naming patterns like this one:

- (from C#) MethodName_StateUnderTest_ExpectedBehavior

```py

def test_add_task__AddingNewTask_TaskAddedToList():
    # Create an instance of TaskList
    task_list = TaskList()

    # Call the add_task method
    task_list.add_task("Task 1")

    # Verify that the task has been added to the tasks list
    assert "Task 1" in task_list.tasks

```

Now you run pytest on the command line and watch it fail. Good! Next Step.

#### 1st Green Step

Now we need to implement the minimal functionality to make the test pass. We already have a list of tasks, we just need to add the task to that list.

```py

# task_list.py
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

```

Now let's check if the test passes:

- It does, Go to Refactor phase.
- It doesn't, fix your function.

#### 1st Step Refactor

Now we need to think if we need to refactor our code, optimize it, improve structure, improve readability. Since we have tests, refactoring our code becomes safer. Most bugs will be catched by your battery of tests (or single test).

#### NEXT ITERATION - 2nd Step Red

Now we write another failing test. Should we write another test for an edge case to the function add_task? Should we go for the next function complete task?
