x = int(raw_input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    print ans
    
if ans*ans*ans != abs(x):
    print x, ' is not a perfect cube'
else:
    if x < 0:
        ans = - ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
##x = 0
##for x in range(0, 10):
##    x = x + 1
##    print x
##
##y = 0
##while y < 10:
##    y = y + 1
##    print y
