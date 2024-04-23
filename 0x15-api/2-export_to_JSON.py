#!/usr/bin/python3
"""
A script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    todos_response = requests.get(
            f"{base_url}/todos",
            params={"userId": employee_id}
            )
    todos_data = todos_response.json()
    json_data = {employee_id: []}
    for todo in todos_data:
        json_data[employee_id].append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_data["username"]
        })
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {filename}")
