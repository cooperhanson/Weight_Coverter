weight_type = input('Is your weight type "LB" or "KG"? ')
amount = input('Enter the numeric value of your weight: ')
if weight_type.upper() == 'LB':
	print('Weight in Kilograms: ', float(amount) * .454)
if weight_type.upper() == 'KG':
	print('Weight in Pounds: ', float(amount) * 2.205)
