INPUT = [2,3,1,5]

def missing_int(a):
	l = len(a) + 1
	sl = l * (l + 1) / 2
	sa = sum(a)
	return sl - sa

r = missing_int(INPUT)
print(f'missing int is = {r}')
print()
