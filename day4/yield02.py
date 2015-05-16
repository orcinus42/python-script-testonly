#!/usr/bin/env python
#

def get_primes(input_list):
	result_list = list()
	for element in input_list:
		if is_prime(element):
			result_list.append()
	return result_list

def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0:
				return False
		return True
	return False

get_primes([1,2,3,4,5,6,7,8,9])
