work = { 
    "Monday" : 5,
    "Tuesday" : 9,
    "Wednesday" : 5,
    "Thursday" : 12,
    "Friday" : 3,
    "Sunday" : 0 
}



work["Saturday"] = 0 
work.pop("Wednesday") 

print(len(work)) 

if "Friday" in work: 
    print("Inside") 

print(work) 