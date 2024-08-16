def fivesmall(): 
    hi1 = input("Hi") 
    hi2 = input("Hi") 
    hi3 = input("Hi") 
    hi4 = input("Hi") 
    hi5 = input("Hi") 
    print(hi1)
    print(hi2) 
    print(hi3) 
    print(hi4) 
    print(hi5)
    numbers = [int (n) for n in input().split()] 
    find = min(numbers) 
    print(find) 
    

fivesmall() 