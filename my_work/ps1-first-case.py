#get input from users

balance 				 = float(raw_input("Enter the outstanding balance on your credit card:", ))
annual_interest_rate 	 = float(raw_input("Enter the annual credit card interest rate in percent:", ))
min_monthly_payment_rate = float(raw_input("Enter the minimum monthly payment rate in percent:", ))

#clean input and convert percent to decimal
annual_interest_rate 	 = annual_interest_rate / 100
min_monthly_payment_rate = min_monthly_payment_rate / 100
monthly_interest_rate 	 = annual_interest_rate / 12

#initialize values
month = 1; total_principal_paid = 0
while month <= 12:
	month += 1

	min_monthly_cash_payment = min_monthly_payment_rate * balance

	interest_cash_paid		 = monthly_interest_rate * balance

	principal_cash_paid		 = min_monthly_cash_payment - interest_cash_paid

	balance 		 		 = balance - principal_cash_paid

	total_principal_paid	+= principal_cash_paid + interest_cash_paid









	print "Month", month
	print "Minimun monthly payment:", round(min_monthly_cash_payment, 2)
	print "Principle paid:", round(principal_cash_paid, 2)
	print "Remaining balance:", round(interest_cash_paid, 2)
	print "End of month outstanding balance", round(balance, 2)
print "You paid a total of:", round(total_principal_paid, 2), "during the year"