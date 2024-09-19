import unittest
from unittest.mock import patch
from io import StringIO

# Import the functions from your task manager program
from main import add_task, show_tasks, remove_task, tasks

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Clear the tasks list before each test
        tasks.clear()

    def test_add_task(self):
        # Test adding a single task
        with patch('builtins.input', return_value="Test Task"):
            add_task()
            self.assertEqual(tasks, ["Test Task"])

        # Test adding multiple tasks
        with patch('builtins.input', side_effect=["Task 1", "Task 2"]):
            add_task()
            add_task()
            self.assertEqual(tasks, ["Test Task", "Task 1", "Task 2"])

    def test_show_tasks(self):
        # Test showing tasks when the list is empty
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            show_tasks()
            self.assertEqual(mock_stdout.getvalue().strip(), "No tasks available.")

        # Test showing tasks when the list has tasks
        tasks.extend(["Task 1", "Task 2"])
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            show_tasks()
            expected_output = (
                "\nYour current tasks:\n"
                "1. Task 1\n"
                "2. Task 2\n"
            )
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    def test_remove_task(self):
        # Test removing a task when the list is empty
        with patch('builtins.input', return_value="1"), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            remove_task()
            # Check only the first line of the output
            self.assertEqual(mock_stdout.getvalue().splitlines()[0], "No tasks available.")

        # Test removing a task when the list has tasks
        tasks.extend(["Task 1", "Task 2"])
        with patch('builtins.input', return_value="1"), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            remove_task()
            self.assertEqual(tasks, ["Task 2"])
            self.assertIn("Task 'Task 1' has been removed.", mock_stdout.getvalue())

        # Test removing a task with an invalid number
        with patch('builtins.input', return_value="3"), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            remove_task()
            self.assertEqual(tasks, ["Task 2"])
            self.assertIn("Invalid task number.", mock_stdout.getvalue())

        # Test removing a task with non-numeric input
        with patch('builtins.input', return_value="invalid"), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            remove_task()
            self.assertEqual(tasks, ["Task 2"])
            self.assertIn("Please enter a valid number.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()