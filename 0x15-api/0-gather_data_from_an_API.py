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
    response = requests.get(api_url + '/users/' + employee_id + '/todos')
    todo_list = response.json()

    # User's data
    employee_name = user_info.get('name')
    tasks_done = []
    total_tasks_done = 0
    total_tasks = len(todo_list)

    # List of tasks done
    for task in todo_list:
        if task.get('completed') is True:
            tasks_done.append(task.get('title'))
            total_tasks_done += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, total_tasks_done, total_tasks))

    for task_done in tasks_done:
        print('\t{}'.format(task_done))
