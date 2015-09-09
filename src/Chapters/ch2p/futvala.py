def fut():
    x = int(input("Number of years"))
    #get number of years
    y = float(input("interest rate"))
    #get apr
    z = float(input("investment per year"))
    #get investment per year
    tmoney = 0;
    #tmoney is the money made in any year

    
    total = 0;
    #total is the overall value of the investment

    #add 1 to x for the # of iterations because in programming, everything starts at 0
    for i in range(x+1):
        #tmoney is the temporary variable where the total for each year is placed
        #Then it is transfored to total

        #the total interest over a period of years 'years' is apr^years
        # the total value of an investment is principal*(total interest)
        #thus, the total value is principal * apr^years, which is the formula below
        tmoney = z * (1+y)**i
        
        #offload the value into the total
        #because we are investing on a yearly basis, the calculation has to happen for each year
        total += tmoney
    print(total)
