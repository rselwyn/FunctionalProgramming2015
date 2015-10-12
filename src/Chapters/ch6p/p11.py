print("PROBLEM 11")
def squareEach(nums):
    for i in range(len(nums)):
        #print(type(nums[i]))
        nums[i] = float(nums[i])   
        nums[i] = nums[i]**2
        print("HERE")
    print(nums)

squareEach(input("ENTER A LIST OF NUMBERS").split(","))

