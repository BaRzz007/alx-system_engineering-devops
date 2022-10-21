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
    
    for user in users:
        if user.get('id') == int(u_id):
            with open('USER_ID.csv', 'w', encoding='utf-8') as f:
                for todo in todos:
                    if todo.get('userId') == int(u_id):
                        f.write('"{}", "{}", "{}", "{}"\n'.format(
                            user.get('id'), 
                            user.get('username'), 
                            todo.get('completed'), 
                            todo.get('title')))
