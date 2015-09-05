
#x = int(input("Enter the payment per period"))
#y = int(input("# of periodds"))
#z = int(input("rate per period"))

#money = x + x*((1-(1+z)**(-(y-1)/z)))
#print(money)
def fut():
    x = int(input("Number of years"))
    y = float(input("interest rate"))
    z = float(input("money per year"))
    tmoney = 0;
    total = 0;
    for i in range(x+1):
        tmoney = z * (1+y)**i
        total += tmoney
    print(total)
