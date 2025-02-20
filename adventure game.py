print( "welcome")
print("This house belongs to prajwal")
print(f"Where do you want to go lliving room or dining room ")


roomChoice = input("-> ")

if(roomChoice == "living room"):
    print("You enter the living room.")
    print("As you walk in, you see a sleeping pitbull guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the pitbull?")

    pitBullChoice = input("-> ")

    if(pitBullChoice == "yes"):
        print("You attempt to steal the jewelry, but it wakes up and rips you to shreds.")
        print("You are now dead.")
    elif(pitBullChoice == "no"):
        print("You decide to not steal the dog's jewelry.")
        print("You turn around and leave the house safely.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif(roomChoice == "dining room"):
    print("You enter the dining room.")
    print("There is a food on the table")
    print("do u want to eat it")
    food_choice = input("-> ")
    if food_choice == "yes":
        print("food was good")
    elif food_choice == "no":
        print("iam full ")

else:
    print("Invalid choice. Please enter living room or dining room.")
