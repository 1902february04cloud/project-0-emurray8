#! /usr/bin/env python3
import data_access.dataaccess as data_access
import datetime
current_user = ''

def register(username, password):
    if not data_access.read_user_data(username):
        data_access.create_user([username, password, 0])
        return True
    else:
        return False
def log_in(username, password):
    query = data_access.read_user_data(username)
    if query:
        if query['password'] == password:
            return True
    return False
def balance_inquiry():
    query = data_access.read_user_data(current_user)
    return query['balance']
def deposit(amount):
    query = data_access.read_user_data(current_user)
    balance = float(query['balance'])
    balance += float(amount)
    data_access.update_user(current_user, str(round(balance, 2)))
    data_access.write_history(current_user, 'deposit', str(amount), datetime.datetime.today())
def withdraw(amount):
    query = data_access.read_user_data(current_user)
    balance = float(query['balance'])
    balance -= float(amount)
    if balance >= 0:
        data_access.update_user(current_user, str(round(balance, 2)))
        data_access.write_history(current_user, 'withdrawal', '-'+str(amount), datetime.datetime.today())
        return True
    else:
        return False
def history():
    data_access.read_history(current_user)