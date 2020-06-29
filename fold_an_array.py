
#Fold an array

# In this kata you have to write a method that folds a given array of integers by the middle x-times.

# An example says more than thousand words:

# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]

# A little visualization (NOT for the algorithm but for the idea of folding):

#  Step 1         Step 2        Step 3       Step 4       Step5
#                      5/           5|         5\          
#                     4/            4|          4\      
# 1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
# ----*----      ----*          ----*        ----*        ----*


# Fold 2-times:
# [1,2,3,4,5] -> [9,6]
# As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

# The array will always contain numbers and will never be null. The parameter runs will always be a positive integer greater than 0 and says how many runs of folding your method has to do.

# If an array with one element is folded, it stays as the same array.

# The input array should not be modified!

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have created other katas. Have a look if you like coding and challenges





def fold_array(arr,times=1):

	if not arr:
		return [0]
	#First split the array using slices
	length = len(arr)
	is_even = True if (length%2) == 0 else False

	#Have to define "Mid index", otherwise 'left' would not contain the correct one
	mid_index = (length//2) if is_even else length//2 +1
	right = arr[mid_index:]
	left = arr[:mid_index]
	# print(left,right)

	leftover = None

	#If odd, have to remove the "leftover" so we can iterate
	if not is_even:
		leftover = left.pop()

	#Defines the number of "folds"
	iterations = 0


	#Empty array to pass values to
	result = []


	#Iterates through list pairwise
	for a,b in zip(left,right[::-1]):
		result.append(a+b)
		# print(a,b)

		#Appends leftover after summing
	if leftover:
		result.append(leftover)


	if times > 1:
		result = fold_array(result,times-1)


	return result





































