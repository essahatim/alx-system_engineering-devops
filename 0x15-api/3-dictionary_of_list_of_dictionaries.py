#!/usr/bin/python3
"""
A script to export data in the JSON format for all employees.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(base_url + "users")
    users_data = users_response.json()

    todo_data_all_employees = {}
    for user in users_data:
        user_id = user.get("id")
        todos_response = requests.get(
                base_url + "todos",
                params={"userId": user_id}
                )
        todos_data = todos_response.json()
        user_todos = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        } for todo in todos_data]
        todo_data_all_employees[user_id] = user_todos

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data_all_employees, jsonfile)
