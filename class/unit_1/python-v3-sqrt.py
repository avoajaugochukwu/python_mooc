#find the cube root of a perfect cube
# x = int(raw_input('Enter an integer: '))
# for ans in range(0, abs(x) + 1):
# 	print ans
# 	if ans**3 == abs(x):
# 		break
# if ans**3 != abs(x):
# 	print x, "is not a perfect cube"
# else:
# 	if x < 0:
# 		ans = -ans
# 	print "Cube root of " + str(x) + " is " + str(ans)

x = 25
epsilon= 0.01
numGuessess = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
	ans += 0.00001
	numGuessess += 1
print 'numGuessess =', numGuessess
if abs(ans**2 - x) >= epsilon:
	print 'Failed to find sqrt of ', x
else:
	print ans, 'is close to sqrt', x