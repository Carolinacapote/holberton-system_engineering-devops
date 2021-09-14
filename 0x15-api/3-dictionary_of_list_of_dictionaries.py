#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import json
import requests


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com'
    # Getting all users info
    response = requests.get(api_url + '/users')
    users_info = response.json()

    # iterating into users list and saving in dictionary
    users_dict = {}
    for user in users_info:
        response = requests.get(api_url + '/users/{}/todos'.
                                format(user.get('id')))
        todo_list = response.json()
        new_list = []
        for task in todo_list:
            task_dict = {'username': user.get('username'),
                         'task': task.get('title'),
                         'completed': task.get('completed')}

            new_list.append(task_dict)

        users_dict[user.get('id')] = new_list

    with open('todo_all_employees.json', 'w') as new_file:
        json.dump(users_dict, new_file)
