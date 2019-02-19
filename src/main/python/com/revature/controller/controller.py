#! /usr/bin/env python3
import sys
from getpass import getpass
import service.service as service
import re
def run():
    command = ''
    while command.lower() != 'q':
        print_menu()
        command = input("Enter number to perform action. Enter q to quit.\n")
        run_command(command)

def run_command(command):
    if service.current_user:
        if command == '1':
            balance_inquiry()
        elif command == '2':
            deposit()
        elif command == '3':
            withdraw()
        elif command == '4':
            service.history()
        elif command == '5':
            log_out()
        elif command == 'q':
            sys.exit()
        else:
            print('Unknown command: {}'.format(command))
    else:
        if command == '1':
            log_in()
        elif command == '2':
            register()
        elif command == 'q':
            sys.exit()
        else:
            print('Unknown command: {}'.format(command))

def print_menu():
    if service.current_user:
        print("Logged in as {}\n1:Balance Inquiry\n2:Deposit\n3:Withdraw\n4:History\n5:Log out\n".format(service.current_user))
    else:
        print("\n1:Log in\n2:Register\n")

def log_in():
    username = input('Enter a username:')
    password = getpass('Enter a password:')
    if service.log_in(username, password):
        service.current_user = username
    else:
        print('Invalid credentials')
def register():
    username = input('Enter a username:')
    while username.isnumeric() or not username.isalnum() or len(username) < 5:
        print('Username must be alphanumeric and at least 5 characters')
        username = input('Enter a username:')
    password = getpass('Enter a password:')
    if service.register(username, password):
        print('Registeration succesful')
        service.current_user = username
    else:
        print('Username already in use.')
def log_out():
    print('Logged out of {}'.format(service.current_user))
    service.current_user = ''
def balance_inquiry():
    print('Your current balance is {}'.format(service.balance_inquiry()))
def deposit():
    amount = input('Enter the amount you would like to deposit:')
    while not valid_amount(amount):
        print('Invalid amount')
        amount = input('Enter the amount you would like to deposit:')
    service.deposit(amount)
    balance_inquiry()
def withdraw():
    amount = input('Enter the amount you would like to withdraw:')
    while not valid_amount(amount):
        print('Invalid amount')
        amount = input('Enter the amount you would like to withdraw:')
    if service.withdraw(amount):
        balance_inquiry()
    else:
        print('Insuffcient funds')
def valid_amount(input):
    try:
        x = float(input)
    except ValueError:
        return False
    return True

