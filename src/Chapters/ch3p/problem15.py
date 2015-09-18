
def problem16():
    hm = int(input("which fibonnaci number do you want to print?"))
    tnum1 = 0
    tnum2 = 1
    store = 0
    #get the number of fibonnaci numbers, cast it to an int because we cant have
    #a loop iterate 1.23 times    
    for i in range(hm):
        store = tnum2
        tnum2 += tnum1
        tnum1 = store        
    print(tnum1)

