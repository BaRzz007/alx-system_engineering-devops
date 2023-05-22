#!/usr/bin/env python3
from fabric.api import run, env

env.hosts = ['18.206.192.187']
env.user = 'ubuntu'

def create_db_user(username, password):
    run(f'echo "CREATE USER \'{username}\'@\'localhost\' IDENTIFIED BY \'{password}\'" | sudo mysql')

def grant_permission(username, permission):
    run(f'echo "GRANT {permission} ON *.* TO \'{username}\'@\'localhost\'" | sudo mysql')

def create_db(db_name):
    run(f'echo "CREATE DATABASE IF NOT EXISTS {db_name}" | sudo mysql')

def create_table(db, tbl_name):
    run(f'echo "CREATE TABLE {tbl_name} (id INT AUTO_INCREMENT PRIMARY KEY, name CHAR(255))" | sudo mysql {db}')

def insert_data(db, tbl_name, name):
    run(f'echo "INSERT INTO {tbl_name} (name) VALUES({name})" | sudo mysql {db}')
