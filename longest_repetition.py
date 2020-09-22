'''
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:
('', 0)
'''

def longest_repetition(chars):
	stack = []
	counts = [1]
	count = 1

	if chars:
		stack.append(chars[0])
		for i in range(1,len(chars)):

			if chars[i] == stack[-1]:
				stack.append(chars[i])

			else:
				stack = [chars[i]]
			
			counts.append(len(stack))

		char_index = counts.index(max(counts))
		return chars[char_index], max(counts)

	else:
		return ('', 0)




print(len(mystr))
print(longest_repetition(mystr))