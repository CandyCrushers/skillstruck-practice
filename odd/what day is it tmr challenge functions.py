def tmr(): 
    month = int(input("Enter a month!")) 
    day = int(input("Enter a day!"))

    if day == 31 or day == 30:
        print(month + 1, 1) 
    elif day == 28 and month == 2: 
        print(month + 1, 1) 
    else:
        print(month, day + 1) 

tmr() 