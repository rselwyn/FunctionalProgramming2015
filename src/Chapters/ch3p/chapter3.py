def problem1():
    #define pi
    pi = 3.14159265358979323846264338279502
    print("This program calculates the volume and surface area of a sphere")
    # get input, float input so no error
    rad = float(input("what is the radius"))
    #surface area
    sa = 4 * pi * rad**2
    #volume
    vol = (4/3)*pi*rad**3
    print("The volume is", vol, "and the surface area is", sa)
def problem2():
    pi = 3.14159265358979323846264338279502
    #calculate cost per square inch of pizza
    rad = float(input("diameter"))/2
    cost = float(input("cost"))
    print("The cost per square inch is", (pi *rad**2)/cost)
def problem3():
    
    
    
