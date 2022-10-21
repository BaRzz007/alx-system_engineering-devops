#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    try:
        users = requests.get('{}users'.format(url)).json()
        todos = requests.get('{}todos'.format(url)).json()
    except Exception as e:
        print('Not successful')

    done_tasks = []
    done = total = 0
    for todo in todos:
        if todo.get('userId') == int(u_id) and todo.get('completed') is True:
            done_tasks.append(todo.get('title'))
            done = done + 1
        if todo.get('userId') == int(u_id):
            total = total + 1

    for user in users:
        if user.get('id') == int(u_id):
            print('Employee {} is done with tasks({}/{}):'.format(
                user.get('name'), done, total))

    for tasks in done_tasks:
        print('\t {}'.format(tasks))
