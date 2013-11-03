finished = False;
pay = 0;

def year(pay,myBalance) :
    totalPaid = 0;
    for i in range(1,13):
        totalPaid += pay;
        myBalance = myBalance - pay;
        myBalance = myBalance + ((annualInterestRate/12.0) * myBalance);
        if myBalance<=0 :
            break;
    return myBalance;        
        
while finished == False :
    pay += 10;
    z = year(pay,balance);
    if z <= 0 :
        finished = True;
        print("Lowest Payment: " + str(pay));