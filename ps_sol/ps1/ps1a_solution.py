# 6.00 PS1-A Solution
# Determines remaining credit card balance after a year of making the minimum payment each month

balance = 1200
annualInterestRate = .12
minMonthlyPaymentRate = 10

# Monthly Interest Rate
monthlyInterestRate = annualInterestRate/12

# Initialize state variables
numMonths = 1
totalAmtPaid = 0

while numMonths <= 12:
    # Minimum monthly payment of balance at start of the month
    minPayment = round(minMonthlyPaymentRate * balance,2)
    totalAmtPaid += minPayment
    
    # Amt of monthly payment that goes to interest
    interestPaid = round(monthlyInterestRate * balance,2)
    
    # Amt of principal paid off
    principalPaid = minPayment - interestPaid
    
    # Subtract monthly payment from outstanding balance
    balance -= principalPaid
    
    print "Month:", numMonths
    print "Minimum monthly payment:", minPayment
    print "Remaining balance:", balance
    
    # Count this as a new month     
    numMonths += 1

print "RESULT"
print "Total amount paid:",totalAmtPaid
print "Remaining balance:",balance
        
        
    
    

