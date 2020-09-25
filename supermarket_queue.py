'''
There is a queue for the self-checkout tills at the supermarket. 
Your task is write a function to calculate the total time required 
for all the customers to check out!

input
customers: an array of positive integers representing the queue. 
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.
'''

# queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# should return 12

def queue_time(customers, n):
	# If there is only one till, it must serve each customer
	if n == 1 or len(customers) == 1:
		return sum(customers)

	elif n > len(customers):
		return max(customers)


	# First populate the tills  with the appropriate customers
	tills = [[customers[x]] for x in range(n)]
	tills_ = [[customers[x]] for x in range(n)]

	# Remove those customers from queue
	customers = customers[n:]
	
	def find_next_till(tills):
		vals = [till[0] for till in tills]
		min_val = min(vals)
		return [i for i, x in enumerate(vals) if x == min_val]

	# While any customers are still in the queue:
	while customers:
		# Find the till that should be filled next
		next_tills = find_next_till(tills)
		slow_tills = [i for i in range(n) if i not in next_tills]

		# Add new customers to the till which will be opened next
		for next_t, slow_t in zip(next_tills, slow_tills):

			# Subtract the remaining "time"
			tills = [[till_val - sum(tills[next_t]) for till_val in till] for till in tills]

			# Set the fastest till to be the next customer in line
			tills[next_t] = [customers[0]]

			# Store the history of each till in 'tills_'
			tills_[next_t].append(customers.pop(0))


	return max(sum(till) for till in tills_)












cust = [1,2,3,4,5]
print(queue_time(cust,3))
