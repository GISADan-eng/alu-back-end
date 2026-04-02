#!/usr/bin/python3
"""
Python script to export TODO list data for a given employee to CSV
"""
import csv
import requests
import sys


def main(employee_id):
    """Fetch employee info and export all tasks to CSV"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
