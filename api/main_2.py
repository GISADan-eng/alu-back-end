#!/usr/bin/python3
import requests
import sys

employee_id = sys.argv[1]

user = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}"
).json()

todos = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
).json()

completed = [task for task in todos if task.get("completed")]

# ✅ Correct first line formatting
print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")

for task in completed:
    print(f"\t {task.get('title')}")