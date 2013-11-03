lower = balance/12.00;
upper = (balance*(1+(annualInterestRate/12.0))**12/12.0);
answer = (upper+lower)/2;

def year(pay,myBalance) :
    totalPaid = 0;
    for i in range(1,13):
        totalPaid += pay;
        myBalance = myBalance - pay;
        myBalance = myBalance + ((annualInterestRate/12.00) * myBalance);
        if myBalance<=0 :
            break;
    return myBalance;
    
while True :
    z = year(answer,balance);
    if abs(z-0.01)<0.1:
       print("Lowest Payment: " + str(answer));
       break;     
    elif z<0:
       upper = answer;
       answer = round((upper+lower)/2,2);
    else :
       lower = answer;
       answer = round((upper+lower)/2,2);