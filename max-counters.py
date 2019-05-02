INPUT = [3, 4, 4, 6, 1, 4, 4]
N = 5

def max_counters(n, a):
	c = [0] * n
	m, l = 0, len(a)
	nx = n + 1
	for x in a:
		if x == nx:
			c[:] = [m] * n
		else:
			i = x - 1
			c[i] += 1
			if c[i] > m:
				m = c[i]
	return c
	

r = max_counters(N, INPUT)
print(f'counter values are = {r}')
print()
