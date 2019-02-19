#!/usr/bin/env python3
from tempfile import NamedTemporaryFile
import csv
import shutil
import os
file_path = "../../../resources/data.csv"
fieldnames = ['username', 'password', 'balance']
def create_user(data):
	with open(file_path, 'a', newline='') as data_file:
		writer = csv.DictWriter(data_file, fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow({fieldnames[0]: data[0], fieldnames[1]: data[1], fieldnames[2]: data[2]})
def read_user_data(username):
	with open(file_path, newline='') as data_file:
		reader = csv.DictReader(data_file, fieldnames=fieldnames)
		for row in reader:
			if username == row['username']:
				return row
def update_user(username, balance):
	temp_file = NamedTemporaryFile(mode='w', delete=False)
	with open(file_path, 'r', newline='') as data_file, temp_file:
		writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
		reader = csv.DictReader(data_file, fieldnames=fieldnames)
		for row in reader:
			if username == row['username']: 
				row = {'username':row['username'],'password':row['password'],'balance':balance}
			writer.writerow(row)
	shutil.move(temp_file.name, file_path)
def delete_user(username):
	temp_file = NamedTemporaryFile(mode='w', delete=False)
	with open(file_path, 'r', newline='') as data_file, temp_file:
		writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
		reader = csv.DictReader(data_file, fieldnames=fieldnames)
		for row in reader:
			if username != row['username']: 
				writer.writerow(row)
	shutil.move(temp_file.name, file_path)
def write_history(username, transaction, amount, date):
	history_file_path = '../../../resources/history/'+ username + '.csv'
	history_fields = ['type', 'amount', 'date']
	try:
		with open(history_file_path, 'a', newline='') as data_file:
			writer = csv.DictWriter(data_file, fieldnames=history_fields)
			writer.writerow({history_fields[0]: transaction, history_fields[1]: amount, history_fields[2]: date})
	except:
		os.system('touch ../../../resources/history/'+ username + '.csv')
		with open(history_file_path, 'a', newline='') as data_file:
			writer = csv.DictWriter(data_file, fieldnames=history_fields)
			writer.writerow({history_fields[0]: transaction, history_fields[1]: amount, history_fields[2]: date})
def read_history(username):
	history_file_path = '../../../resources/history/'+ username + '.csv'
	history_fields = ['type', 'amount', 'date']
	try:
		with open(history_file_path, newline='') as data_file:
			reader = csv.DictReader(data_file, fieldnames=history_fields)
			for row in reader:
				print('{} {} {}'.format(row['type'], row['amount'], row['date']))
	except:
		print('No transaction history found')