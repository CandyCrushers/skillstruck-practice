def leap(): 
    year = int(input("Enter a year!")) 
    math = year % 4 
    if math == 0: 
        print("Leap year!") 
    else: 
        print("Not a leap year.") 



leap() 