#INPUT = [1, 2, 3, 4]
#INPUT = [2, 2, 2, 4]
#INPUT = [1, 2, 2, 5]
#INPUT = [1, 1, 2, 6]
#INPUT = [1, 1, 1, 7]
#INPUT = [1, 3, 3, 3]
#INPUT = [2, 2, 3, 3]
#INPUT = [4, 1, 3, 2]
#INPUT = [2, 3, 3, 1, 6]
#INPUT = [2, 3, 3, 1, 5]

def is_perm(a):
	n = len(a)
	sn = int(n * (n+1) / 2)
	sa = 0
	occ = [0] * n

	for x in a:
		if x > n:
			return 0
		sa += x
		occ[x-1] += 1
		if occ[x-1] > 1:
			return 0
	if sa != sn:
		return 0
	return 1 if sum(occ) == n else 0

r = is_perm(INPUT)
print(f'arry is a perm is {r}')
print()
