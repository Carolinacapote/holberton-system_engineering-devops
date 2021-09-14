#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
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

    # dictionary with key=employee_id, value=todo_list-> list of dicts
    new_list = []
    for task in todo_list:
        task_dict = {'task': task.get('title'),
                     'completed': task.get('completed'), 'username': user_name}
        new_list.append(task_dict)

    user_dict = {employee_id: new_list}

    with open(employee_id + '.json', 'w') as new_file:
        json.dump(user_dict, new_file)
