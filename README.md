# Task Manager

This is a simple command-line Task Manager application written in Python. It allows users to manage their tasks by adding, removing, and viewing them.

## Features

- Add new tasks
- Remove existing tasks
- View all tasks
- Simple command-line interface

## How to Use

1. Run the script in a Python environment.
2. You will be presented with a menu of options:
   1. Add a new task
   2. Remove a task
   3. Show all tasks
   4. Quit
3. Enter the number corresponding to your desired action.

### Adding a Task

- Select option 1 from the menu.
- Enter the description of your task when prompted.

### Removing a Task

- Select option 2 from the menu.
- You will see a list of your current tasks.
- Enter the number of the task you wish to remove.

### Viewing Tasks

- Select option 3 from the menu to see all your current tasks.

### Quitting the Program

- Select option 4 to exit the Task Manager.

## Code Structure

- `tasks`: A list to store all tasks.
- `add_task()`: Function to add a new task.
- `show_tasks()`: Function to display all tasks.
- `remove_task()`: Function to remove a task by its index.
- `menu()`: Function to display the menu options.
- `main()`: The main function that runs the program loop.

## Requirements

- Python 3.x

## Running the Program

To run the Task Manager, execute the script in a Python environment: