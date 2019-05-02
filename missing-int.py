INPUT = [-1, -3]

def missing_int(arr):
	MAX = 1000000
	mn = [False] * MAX
	for x in arr:
		if x > 0:
			mn[x - 1] = True
	i = 0
	while i < MAX:
		if not mn[i]:
			break
		i += 1
	return i + 1

r = missing_int(INPUT)
print(f'Missing int in array is = {r}')
print()
