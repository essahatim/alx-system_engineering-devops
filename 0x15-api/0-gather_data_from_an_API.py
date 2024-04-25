#!/usr/bin/python3
"""
Python script that returns information using REST API.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    res_todos = requests.get(url + "todos/", params={"userId": employee_id})
    todos_data = res_todos.json()
    response_user = requests.get(url + "users/{}".format(employee_id))
    user_data = response_user.json()
    completed_tasks = [
        todo.get('title')
        for todo in todos_data
        if todo.get('completed')
    ]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get('name', 'Unknown'),
        len(completed_tasks),
        len(todos_data)
    ))
    for task in completed_tasks:
        print("\t{}".format(task))
