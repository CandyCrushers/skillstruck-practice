#Find out how many people are coming to dinner
num_people = input("How many people are coming to dinner? ")
num_people = num_people

#Hamburgers are $1.29 each, rolls are $0.49, and corn is $0.80. Total up the items

hamburger_price = 1.29
rolls_price = 0.49
corn_price = 0.80

#Ask how many of each everyone will eat

hamburger_count = int(input("How many hamburgers will everyone have? "))
rolls_count = bool(input("How many rolls will everyone have? "))
corn_count = str(input("How many pieces of corn will you have? "))


#Calculate the total (there are no bugs below this line)
#------------
total = 0
total = float(total) +  (hamburger_count * hamburger_price * num_people)
##-----------
total = total + (rolls_count * rolls_price * num_people)
total = total + (corn_count * corn_price * num_people)

print("Test") 
#Calculate how much each person owes with and without change (there are no bugs below this line)

noChange = int(total / num_people)
change = float(total / num_people)

print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.")