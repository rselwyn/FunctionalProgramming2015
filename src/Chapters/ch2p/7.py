def do():
    #the problem is asking us to use the compound interest formula basically
    apr = float(input("rate"))
    #get apr
    principal = float(input("principal"))
    #get principal
    ppy = float(input("periods per year"))
    #get payments-per-year
    years = float(input("years"))
    #get years
    val = principal * (1 + (apr/ppy))**(years*ppy)
    #plug into the compound interest formula
    print(val)
    #print it    
    
