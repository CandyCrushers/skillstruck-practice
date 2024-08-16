# Initialize an empty dictionary
dinosaur_box = {}

while True:
    # Get the name and height of the dinosaur from the user
    name = input("What's the dinosaur's name? ")
    height = int(input("How tall is it? "))
    
    # Add the dinosaur's name and height to the dictionary
    dinosaur_box[name] = height
    
    # Check if the dinosaur's name is 'triceratops'
    if name == "triceratops":
        break  # Exit the loop if the name is 'triceratops'

# Print the final dictionary
print(dinosaur_box)

