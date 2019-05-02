INPUT = [3, 8, 9, 7, 6]

def cyclic_rotate(arr, k):
	l = len(arr)
	r = [0] * l
	i = 0
	while i < l:
		j = (i + k) % l
		r[j] = arr[i]
		i += 1
	return r

r = cyclic_rotate(INPUT, 3)
print(f'rotated array is = {r}')
print()
