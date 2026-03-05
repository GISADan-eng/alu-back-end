#!/usr/bin/python3
"""
1-export_to_CSV.py
Exports all tasks of a given employee to a CSV file.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    # Fetch employee info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    # Fetch all TODOs for the employee
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    # CSV filename: <employee_id>.csv
    filename = f"{employee_id}.csv"

    # Write all tasks to CSV
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])
