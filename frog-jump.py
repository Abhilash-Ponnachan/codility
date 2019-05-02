INPUT = (10, 85, 30)

def min_jumps(x, y, d):
	l = y - x
	s = l // d
	f = l % d
	return s + 1 if f > 0 else s

x, y, d = INPUT
r = min_jumps(x, y, d)
print(f'min jumps needed is = {r}')
print()
