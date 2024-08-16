fruit = {

    "apples" : 5,
    "bananas" : 7, 
    "strawberries" : 3

}


more = int(input("I need how many apples!"))
more2 = int(input("I need more bananas!"))
more3 = int(input("I need more strawberries!")) 


fruit["apples"] = more - 5
fruit["bananas"] = more2 - 7 
fruit["strawberries"] = more3 - 3  

print(fruit) 