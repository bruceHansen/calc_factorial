def factorial(some_number):	

	my_num = 1

	try:
		if some_number > 0:
			my_num = some_number * factorial(some_number - 1) 

		return my_num
	
	except: 
		return

fac_numbers = [5, 8, 20, 100, 999]

for num in fac_numbers:
	my_number = factorial(num)

	if my_number:
		print ('The factorial for ', num, " is: ", my_number)
	else:
		print('Not able to calculate factorial for', num)
	