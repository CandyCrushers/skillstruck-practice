def inputs():
    knife = int(input("Rate 1-10 for knife: "))
    fire = int(input("Rate 1-10 for fire: "))
    starter = int(input("Rate 1-10 for fire starter: "))  # Assuming 'starter' is meant to be 'fire starter'
    pot = int(input("Rate 1-10 for pot: "))
    rope = int(input("Rate 1-10 for rope: "))
    tarp = int(input("Rate 1-10 for tarp: "))

    items = {
        "knife": knife,
        "fire": fire,
        "fire_starter": starter,  # Updated key to match expected representation
        "pot": pot,
        "rope": rope,
        "tarp": tarp
    }

    print(items)

inputs()
