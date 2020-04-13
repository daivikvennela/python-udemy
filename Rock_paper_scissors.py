print("Rock Paper Scissors")

response = input("Type R for rock, P for paper and S for scissors: ")

while response != "" : 
    
    if response == ("R") :
            print("Paper-YOU LOSE")
    elif response == ("P") :
        print("Scissors-YOU LOSE")
    elif response == ("S") :
        print("Rock-YOU LOSE")
    else :
        print("That is not a valid input")
    response = input("Type R for rock, P for paper and S for scissors or [Enter] to exit: ")
