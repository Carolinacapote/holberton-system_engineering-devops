#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    employee_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    # Getting the user's info
    response = requests.get(api_url + '/users/' + employee_id)
    user_info = response.json()
    # Getting the user's to do list
    response_2 = requests.get(api_url + '/users/' + employee_id + '/todos')
    todo_list = response_2.json()

    # User's data
    employee_name = user_info.get('name')

    with open(employee_id + '.csv', 'w') as file:
        user_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            user_file.writerow([employee_id, employee_name,
                                task.get('completed'), task.get('title')])
