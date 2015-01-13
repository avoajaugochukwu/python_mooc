balance = float(raw_input("Enter the outstanding balance on your credit car: "))
annualInterestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
monthlyPayment = 10
monthlyInterestRate = annualInterestRate/12
newbalance = balance - 10
while (newbalance > 0):
    monthlyPayment += 10
    newbalance = balance
    month = 0
    while (month < 12 and newbalance > 0):
        month += 1
        interest = monthlyInterestRate * newbalance
        ##newbalance = (newbalance * (1 + monthlyInterestRate)) - monthlyPayment
        newbalance = newbalance - (monthlyPayment - interest)
       
newbalance = round(newbalance,5)
print " RESULT"
print " Lowest Payment: ", monthlyPayment
print " Number of months needed: ", month
print " Balance: ", newbalance
