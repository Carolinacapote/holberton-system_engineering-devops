#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv


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
    user_name = user_info.get('username')

    with open(employee_id + '.csv', 'w') as new_file:
        for task in todo_list:
            new_file.write('"{}","{}","{}","{}"\n'.
                           format(employee_id, user_name,
                                  task.get('completed'), task.get('title')))
