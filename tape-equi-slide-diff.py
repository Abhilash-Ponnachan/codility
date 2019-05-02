INPUT = [3, 1, 2, 4, 3]

def min_part_diff(a):
	sl, sr = 0, sum(a)
	md = 100000000
	i, l = 1, len(a)
	while i < l:
		sl += a[i-1]
		sr -= a[i-1]
		d = abs(sr - sl)
		print(a[i-1], sl, sr, d, md)
		if d < md:
			md = d
		i += 1 
	return md

r = min_part_diff(INPUT)
print(f'min partition diff = {r}')
print()
