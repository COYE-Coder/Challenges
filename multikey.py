import string
def presses(phrase):
	phrase = phrase.lower()
	a = list(range(1,4))
	b = list(range(1,5))
	vals = a * 5
	vals.extend(b)
	vals.extend(a)
	vals.extend(b)
	vals.extend([2,1,4,4,4,4,4,5,4,5,1,1])
	
	extras = [str(n) for n in range(10)]
	extras.extend(['*','#'])
	keys = list(string.ascii_lowercase)
	keys.extend(extras)

	press_dict = {k:v for (k,v) in zip(keys,vals)}
	print(press_dict)

	presses = 0
	for c in phrase:
		if press_dict.get(c):
			presses += press_dict.get(c)
		else:
			presses += 1

	return presses


print(presses("HOW R U2"))


