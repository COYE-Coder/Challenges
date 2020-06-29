# The rgb function is incomplete. 
# Complete it so that passing in RGB decimal values 
# will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


#For practice, I will manually convert to Hexadecimal
def rgb(r,g,b):

	input_list = [r,g,b]
	digit_list = []

	#Create key:value pairs for dictionary
	nums = list(range(1,16))
	hexs = [str(h) for h in list(range(1,10))]
	hexs.extend([l for l in 'ABCDEF'])

	#Instantiate dictionary
	HEX_dict = dict(zip(nums,hexs))

	for c in input_list:
		#First truncate rgb values
		if c < 0:
			c = 0
		elif c > 255:
			c = 255

		#Then find base 16 analogues
		first_digit = c//16
		second_digit = c - (16*first_digit)

		if first_digit == 0 and second_digit == 0:
			first_hex = '0'
			second_hex = '0'
		
		elif first_digit > 1:
			first_hex = HEX_dict[first_digit]
			second_hex = HEX_dict[second_digit]

		else:
			first_hex = '0'
			second_hex = HEX_dict[second_digit]

		digit_list.append(first_hex+second_hex)

	return ''.join(digit_list)
		


y = [l for l in 'ABCDEF']
x = [str(h) for h in list(range(1,10))]
x.extend(y)
# x.extend([l for l in 'ABCDEF'])

b = rgb(0,2,3)
print(b)
	

