shapes = {

"Triangle": 8,

"Circle": 15,

"Square": 10,

"Rectangle" : 12

}

newshape = input("Enter a new shape!") 
newheight = int(input("Enter a new hight!")) 

shapes[newshape] = newheight
print(shapes) 