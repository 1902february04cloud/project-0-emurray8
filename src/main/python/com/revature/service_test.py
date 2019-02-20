#!/usr/bin/env python3
import service.service as service_tester

def run():
    registration_tests = [False, False]
    login_tests = [False, False]
    withdraw_tests = [False, False]
    deposit_tests = [False]
    #test for succesful creation of the user
    if service_tester.register('test_user_123', 'password'):
        registration_tests[0] = True
    #user exists now, this should fail
    if not service_tester.register('test_user_123', 'password'):
        registration_tests[1] = True
    #test for succesful login
    if service_tester.log_in('test_user_123', 'password'):
        login_tests[0] = True
    #incorrect password, this should fail
    if not service_tester.log_in('test_user_123', 'psswd'):
        login_tests[1] = True
    #invalid withdrawal, negative balance, this should fail
    service_tester.current_user = 'test_user_123'
    if not service_tester.withdraw(100):
        withdraw_tests[0] = True
    #deposit test
    balance = service_tester.balance_inquiry()
    service_tester.deposit(100)
    after_balance = service_tester.balance_inquiry()
    if after_balance > balance:
        deposit_tests[0] = True

    #withdraw success test
    if service_tester.withdraw(50):
        withdraw_tests[1] = True
    
    service_tester.delete_user('test_user_123')


    print_test_results('registration', registration_tests)
    print_test_results('login', login_tests)
    print_test_results('deposit', deposit_tests)
    print_test_results('withdrawal', withdraw_tests)
def print_test_results(test_name, collection):
    pass_count = 0
    total = len(collection)
    for item in collection:
        if item:
            pass_count+=1
    print('{} tests passed [{}/{}]'.format(test_name, pass_count, total))
