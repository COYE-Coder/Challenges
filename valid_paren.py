# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
#    determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


#Input: "()"
# Output: true


# Input: "([)]"
# Output: false

# Input: "{[]}"
# Output: true



def valid_paren(string):
	opens = ['(' , '{' , '[']
	closeds = [')' , '}' , ']']
	paren_list = []
	num_correct = 0
	check_index = 0

	#Iterate through input string
	for s in string:
		

		#Check if opened or closed
		if s in opens:
			paren_list.append(s)


		#if element is a closed bracket
		else:
			#Increment element to be checked in paren_list
			check_index -= 1

			#Last_added is last element of paren_list to begin with
			last_added = paren_list[check_index]

			#Make sure 

			#If the last element closes the correct bracket
			if opens.index(last_added) == closeds.index(s):
				
				#Inrement num_correct
				num_correct += 1
				print(num_correct)

	if num_correct == len(string)//2 or not string:
		return True

	return False



