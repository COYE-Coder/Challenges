

'''
Given two cells on the standard chess board, determine whether they have the same color or not.

For cell1 = "A1" and cell2 = "C3", the output should be true.

'''

def chess_board_cell_color(cell1,cell2):
	c_1 = sum([ord(c) for c in cell1])
	c_2 = sum([ord(c) for c in cell2])
	
	#If both even:
	if c_1%2 == 0 and c_2%2==0:
		return True
	#If both odd:
	elif c_1%2 ==1 and c_2%2 ==1:
		return True

	return False


cell1 = "A1"
cell2 = "H3"
print(chess_board_cell_color(cell1,cell2))