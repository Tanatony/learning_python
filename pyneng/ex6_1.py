#! /usr/bin/env python3

a = int(input('Please input number: '))

if a == 10:
	print('a = 10')
elif a < 10:
	print('a < 10')
else:
	print('a > 10')

list_to_test = [1, 2, 3]

if list_to_test:
	print('List has objects')