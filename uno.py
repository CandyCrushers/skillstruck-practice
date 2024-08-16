snickers = input("How many snickers did you get?") 
nerds = input("How many nerds did you get?")
butterfingers = input("How many butterfingers did you get?") 

## adds the total candy
total_Candy = snickers + nerds + butterfingers
## completes the input prompts together for the user 
sentence = ("This year, you got " + snickers + " snickers, " + nerds + " nerds, and " + butterfingers + " butterfingers. The total number of these candies is " + total_Candy + " candies.")

print(sentence)
## Prints the big sentence 