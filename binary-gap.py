INPUT = 1041

def binary_gap(num):
	g = 0
	bg = 0
	l = 32
	i = 0
	s = False
	while i < l:
		if not s:
			if (num & 1 == 1):
				s = True
		else:
			if (num & 1 == 1):
				if (g > bg):
					bg = g
				g = 0
			else: # bit == 0
				g += 1
		num = num >> 1
		i += 1
	return bg

r = binary_gap(INPUT)
print(f'Binary gap of {INPUT} is {r}')
print()
