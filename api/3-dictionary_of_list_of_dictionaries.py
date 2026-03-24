#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
Exports all tasks from all employees to a JSON file.
"""
import json
import requests


def export_all_to_json():
    """Exports all employee tasks to JSON"""
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    all_tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_tasks[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
