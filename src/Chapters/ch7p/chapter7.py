#1-3,6-8,11,12,16

def problem1():
    hours = int(input("How many hours did you work this week?"))
    wage = float(input("Enter your hourly wage"))

    if hours <= 40:
        print("You made {0:.2f} this week".format(hours*wage))
    else:
        print("You made {0:.2f} this week".format(40*wage + (1.5*(hours-40))*wage ))
