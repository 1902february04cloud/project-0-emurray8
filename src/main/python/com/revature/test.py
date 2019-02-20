#!/usr/bin/env python3
import service_test
import dataaccess_test
'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
	service_test.run()
	dataaccess_test.run()

if __name__ == '__main__':
	main()