#! /usr/bin/env python3
import data_access.dataaccess as data_access
import datetime
import logging
import hashlib

current_user = ''
def register(username, password):
    if not data_access.read_user_data(username):
        hasher = hashlib.sha1()
        hasher.update((username + password).encode('utf-8'))
        hashed_password = hasher.hexdigest()
        data_access.create_user([username, hashed_password, 0])
        logging.debug(username + ' True' )
        return True
    else:
        logging.debug(username + ' False' )
        logging.error(username + ' > registration rejected. username already in use')
        return False
def log_in(username, password):
    query = data_access.read_user_data(username)
    if query:
        hasher = hashlib.sha1()
        hasher.update((username + password).encode('utf-8'))
        hashed_password = hasher.hexdigest()
        if query['password'] == hashed_password:
            return True
    logging.error(username + ' > failed login.')
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
        logging.error('invalid withdrawal operation. amount: ' + str(amount) + ' balance: ' + str(balance))
        return False
def history():
    data_access.read_history(current_user)
def delete_user(username):
    data_access.delete_user(username)
