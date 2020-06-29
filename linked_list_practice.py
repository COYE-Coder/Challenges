"""You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.="""

def loop_size(node):
	size = 1
	current = node.next
	ahead = node.next.next


	while current != ahead:
		current = current.next
		ahead = ahead.next.next

	ahead = ahead.next

	while current != ahead:
		ahead = ahead.next
		size += 1

	return size



