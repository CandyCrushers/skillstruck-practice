permission = [str(n) for n in input("Input a list of names separated by spaces").split()]


people_dictionary = dict.fromkeys(permission, "yes")

print(people_dictionary) 