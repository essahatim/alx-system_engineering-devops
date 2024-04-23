#!/usr/bin/python3
"""
Script that exports data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"
    all_data = {}

    for employee_id in range(1, 11):
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()

        todos_response = requests.get(
            f"{base_url}/todos",
            params={"userId": employee_id}
        )
        todos_data = todos_response.json()
        all_data[str(employee_id)] = []
        for todo in todos_data:
            all_data[str(employee_id)].append({
                "username": user_data["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            })
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_data, json_file, indent=4)

    print(f"Data exported to {filename}")
