# intial floor where the lift is currently at
current_floor = 1   
# show available floors
print("Welcome to the Lift Simulation Program!")
print("This building has 14 floors (1 to 14).")
print(f"Lift is currently on floor {current_floor}.")
# take input from the user
try:
    desired_floor = int(input("Enter the floor you want to go to (1-14): "))
    
    # conditions
    if desired_floor < 1 or desired_floor > 14:
        print("Invalid floor! Please enter a number between 1 and 14.")
    elif desired_floor == current_floor:
        print("Lift is already on the same floor.")
    elif desired_floor > current_floor:
        print(f"Lift is going UP from floor {current_floor} to floor {desired_floor}.")
    elif desired_floor < current_floor:
        print(f"Lift is going DOWN from floor {current_floor} to floor {desired_floor}.")
    else:
        print("Unexpected error.")
except ValueError:      
    print("Please enter a valid number (integer).") 