#!/usr/bin/env python3
import data_access.dataaccess as data_test

def run():
    tests = [False, False, False, False]
    data_test.create_user(['testing123', 'password', 0])
    if data_test.read_user_data('testing123'):
        tests[0] = True
        tests[1] = True
    data_test.update_user('testing123', 1000)
    data = data_test.read_user_data('testing123')
    if data['balance'] != 0:
        tests[2] = True
    data_test.delete_user('testing123')
    if not data_test.read_user_data('testing123'):
        tests[3] = True
    count = 0
    total = len(tests)
    for item in tests:

        if item:
            count += 1
    print('file operations tests passed [{}/{}]'.format(count, total))
