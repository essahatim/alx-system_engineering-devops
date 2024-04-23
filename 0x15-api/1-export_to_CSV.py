#!/usr/bin/python3
"""
A script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        f"{base_url}/users/{employee_id}",
        verify=True)
    user_data = user_response.json()

    todos_response = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id},
        verify=True)
    todos_data = todos_response.json()

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            taskwriter.writerow([int(employee_id), user_data.get('username'),
                                 todo.get('completed'), todo.get('title')])
    print(f"Data exported to {filename}")
