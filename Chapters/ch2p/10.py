def do():
    apr = float(input("rate"))
    principal = float(input("principal"))
    ppy = float(input("periods per year"))
    years = float(input("years"))
    val = principal * (1 + (apr/ppy))**(years*ppy)
    print(val)
    
    
