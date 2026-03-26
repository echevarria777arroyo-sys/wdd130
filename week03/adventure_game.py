print("Welcome to the adventure game!")

choice1 = input("You are in a forest. You see a PATH and a CAVE. Which do you choose? ").lower()

if choice1 == "path":
    print("You walk along the path and hear a strange noise.")
    
    choice2 = input("Do you RUN, LOOK, or CLIMB a tree? ").lower()
    
    if choice2 == "run":
        print("You run away safely. The end.")
        
    elif choice2 == "look":
        print("You see a wolf!")
        
        choice3 = input("Do you FIGHT or RUN? ").lower()
        
        if choice3 == "fight":
            print("You fought bravely and won! The end.")
        elif choice3 == "run":
            print("You escaped just in time! The end.")
        else:
            print("Invalid choice.")
            
    elif choice2 == "climb":
        print("You climb a tree and stay safe. The end.")
        
    else:
        print("Invalid choice.")

elif choice1 == "cave":
    print("You enter the cave and it is very dark.")
    
    choice2 = input("Do you LIGHT a torch or GO BACK? ").lower()
    
    if choice2 == "light":
        print("You see treasure!")
        
        choice3 = input("Do you TAKE it or LEAVE it? ").lower()
        
        if choice3 == "take":
            print("You are rich! The end.")
        elif choice3 == "leave":
            print("You leave safely. The end.")
        else:
            print("Invalid choice.")
            
    elif choice2 == "go back":
        print("You leave the cave safely. The end.")
        
    else:
        print("Invalid choice.")

else:
    print("That is not a valid option.")