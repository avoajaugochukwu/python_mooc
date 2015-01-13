original_balance = 320; an_interest_rt = .2
interest_rate = .2
numTries = 0; month = 0 # check_balance = balance

low = original_balance / 12.0
high = (original_balance*(1+(interest_rate/12))**12)/12

acc_balance = (original_balance * 
ans = (high + low) /2
epsilon = 0.005
print "high", high
print "low", low
print "ans", ans
print "acc_balance", acc_balance
# while abs(ans*12 - acc_balance) >= epsilon:
for i in range(0, 10):
	interest = 
	if abs(ans*12 - acc_balance) < epsilon:
		print "if"

	else:
		low = ans
		print "else"
	# print "ans", ans
	ans = (high + low) / 2
# print "low", low
# print "high", high
#high 39020.514717

# print "original_balance", original_balance
# print "min_payment", min_payment
# print "month", month
# print "ans", ans * 12
# print "acc_balance", acc_balance
# print numTries
#3860 numTries















# balance = 320000; an_interest_rt = .2
# mo_interest_rt = an_interest_rt / 12 #0.0166666666666666667
# numTries = 0; month = 0 # check_balance = balance
# low = balance / 12.0
# high = (balance * (1 + mo_interest_rt)**12) / 12.0
# acc_balance = high
# ans = (high + low)/2.0
# while month < 12: #and (ans * 12) < acc_balance:
# 	print "low:",low, "high", high, "ans", ans, "ans_sqaured", ans*12
# 	if ans * 12 < high:
# 		low = ans
# 		print "if"
# 	else:
# 		high = ans
# 		print "else"
# 	ans = (high + low)/2.0
# 	month += 1

# print "low", low
# print "high", high
# #high 39020.514717

# # print "balance", balance
# # print "min_payment", min_payment
# print "month", month
# # print numTries
# #3860 numTries