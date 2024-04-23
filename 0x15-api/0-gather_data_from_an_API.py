#!/usr/bin/python3
"""
Python script that returns information using REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    res_todos = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = res_todos.json()
    response_user = requests.get(url + "users/{}".format(employee_id))
    user_data = response_user.json()
    compl_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], len(compl_tasks), len(todos_data)))
    for task in compl_tasks:
        print("\t{}".format(task))
