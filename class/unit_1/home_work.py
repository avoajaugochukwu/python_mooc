def fact(m, n):
	if n == 0:
		return 1
	return m * fact(m, n-1)

print fact(2, 4)