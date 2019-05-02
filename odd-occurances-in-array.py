INPUT = [9, 3, 9, 3, 9, 7, 9]

def odd_elem(arr):
	e = 0
	for x in arr:
		e = e ^ x
	return e

r = odd_elem(INPUT)
print(f'Odd element is {r}')
print()
