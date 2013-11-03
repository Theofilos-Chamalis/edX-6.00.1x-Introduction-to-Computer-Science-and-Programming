# Paste your code into this box
totalPaid = 0;

for i in range(1,13):
    print("Month: "+str(i));
    print("Minimum monthly payment: " + str(round(monthlyPaymentRate*balance,2)));
    totalPaid += monthlyPaymentRate*balance;
    balance = balance + (annualInterestRate/12.0)*balance;
    balance = balance - (monthlyPaymentRate*balance);
    print("Remaining balance: " + str(round(balance,2)));
    
print("Total paid: " + str(round(totalPaid,2)));    
print("Remaining balance: " + str(round(balance,2)));