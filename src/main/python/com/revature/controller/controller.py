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
            print('\n\nUnknown command: {}'.format(command))
    else:
        if command == '1':
            log_in()
        elif command == '2':
            register()
        elif command == 'q':
            sys.exit()
        else:
            print('\n\nUnknown command: {}'.format(command))

def print_menu():
    if service.current_user:
        print("\n\nLogged in as {}\n1:Balance Inquiry\n2:Deposit\n3:Withdraw\n4:History\n5:Log out\n".format(service.current_user))
    else:
        print("\n1:Log in\n2:Register\n")

def log_in():
    username = input('Enter a username:')
    password = getpass('Enter a password:')
    if service.log_in(username, password):
        service.current_user = username
    else:
        print('\n\nInvalid credentials')
def register():
    username = input('Enter a username:')
    while username.isnumeric() or not username.isalnum() or len(username) < 5:
        print('\n\nUsername must be alphanumeric and at least 5 characters')
        username = input('Enter a username:')
    password = getpass('Enter a password:')
    if service.register(username, password):
        print('\n\nRegisteration successful')
        service.current_user = username
    else:
        print('\n\nUsername already in use.')
def log_out():
    print('\n\nLogged out of {}'.format(service.current_user))
    service.current_user = ''
def balance_inquiry():
    print('\n\nYour current balance is {}'.format(service.balance_inquiry()))
def deposit():
    amount = input('Enter the amount you would like to deposit:')
    while not valid_amount(amount):
        print('\n\nInvalid amount')
        amount = input('Enter the amount you would like to deposit:')
    service.deposit(amount)
    balance_inquiry()
def withdraw():
    amount = input('Enter the amount you would like to withdraw:')
    while not valid_amount(amount):
        print('\n\nInvalid amount')
        amount = input('Enter the amount you would like to withdraw:')
    if service.withdraw(amount):
        balance_inquiry()
    else:
        print('\n\nInsuffcient funds')
def valid_amount(input):
    try:
        x = float(input)
    except ValueError:
        return False
    return True

