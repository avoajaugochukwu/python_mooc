# Problem Set 1
# Name: Avoaja Ugochukwu
# Collaborators: 
# Time Spent: 3:30
balance  = float(raw_input("Enter the outstanding balance on your credit card:", ))
annual_interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal:", ))

check_balance = balance

#monthly compounding
monthly_interest_rate = annual_interest_rate / 12.0   #0.015 @ 18%
minimum_monthly_payment = 10

#initialise count
month = 0

while (balance > 0):
	if (month < 12):
		balance = balance * (1 + monthly_interest_rate) - minimum_monthly_payment
		month += 1
	else:
		minimum_monthly_payment += 10
		month = 0
		balance = check_balance

print 'month', month
print 'balance', balance
print 'minimum_monthly_payment', minimum_monthly_payment