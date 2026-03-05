#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
import sys


def main(employee_id):
    """Fetch employee info and TODO progress"""

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
