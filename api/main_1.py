#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get employee info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    # Get todos
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    # Filter completed tasks
    completed = [task for task in todos if task.get("completed")]

    # Print first line
    print(
        f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):"
    )

    # Print completed task titles
    for task in completed:
        print(f"\t {task.get('title')}")