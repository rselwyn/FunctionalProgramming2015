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
