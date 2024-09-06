# List to store the tasks
tasks = []

# Function to add a new task
def add_task():
    # Prompt the user to enter a task
    task_description = input("Please enter a new task: ")
    # Add the task to the list
    tasks.append(task_description)
    print(f"Task '{task_description}' has been added.")

# Function to display all tasks
def show_tasks():
    # Check if the task list is empty
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        # If tasks exist, display them with their index
        print("\nYour current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")  # Print each task with its number
        print()  # Add a blank line for better readability

# Function to remove a task by its index
def remove_task():
    # Show current tasks first
    show_tasks()
    try:
        # Ask the user for the task number they want to delete
        task_number = int(input("Enter the task number to remove: "))
        # Check if the entered number is valid
        if 1 <= task_number <= len(tasks):
            # Remove the selected task
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            # Error message if the task number is out of range
            print("Invalid task number.")
    except ValueError:
        # Error message if the user enters something that's not a number
        print("Please enter a valid number.")

# Function to display the menu options
def menu():
    print("\nTask Manager")  # Title
    # Display the available options
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Quit")

# Main function that runs the program
def main():
    print("Welcome to the Task Manager!")  # Welcome message
    while True:
        menu()  # Show the menu
        # Prompt the user to make a choice
        choice = input("Choose an option: ")

        # Check the user's choice and call the appropriate function
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            # Exit the program if the user selects "4"
            print("Exiting the program. Goodbye!")
            break
        else:
            # Error message for invalid choices
            print("Invalid choice, please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
