#INPUT = [1, 3, 1, 4, 2, 3, 5, 4]
INPUT = [1, 3, 1, 3, 2, 1, 3]
X = 3

def earliest_time(x, a):
	et = -1
	if x <= 0:
		return et
	l = len(a)
	c = [-1] * x
	i = 0
	while i < l:
		j = a[i] - 1
		if (j < x) and (c[j] == -1):
			c[j] = i
		i += 1
	for k in c:
		if k == -1:
			return -1
		if k > et:
			et = k
	return et
	

r = earliest_time(X, INPUT)
print(f'earliest crossing time {r}')
print()
