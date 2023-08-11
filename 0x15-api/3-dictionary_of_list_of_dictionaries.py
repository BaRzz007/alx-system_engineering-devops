#!/usr/bin/python3
""" Gather data from an API """

import json
import requests


def to_json():
    url = 'https://jsonplaceholder.typicode.com/'

    try:
        users = requests.get('{}users'.format(url)).json()
        todos = requests.get('{}todos'.format(url)).json()
    except Exception as e:
        print('Not successful')
        quit()

    users_dict = {}

    for user in users:
        task_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                task = {"username": user.get('username'),
                        "task": todo.get('title'),
                        "completed": todo.get('completed')}
                task_list.append(task)

        users_dict[user.get('id')] = task_list

    _file = 'todo_all_employees.json'
    with open(_file, 'w', encoding='utf-8') as f:
        json.dump(users_dict, f)
    f.close()


if __name__ == "__main__":
    to_json()