import string
import random




print("Rock Paper Scissors")

#validList=['R','P','S']
#^^^^^^^^^INTVALUES[0,1,2]^^^^^^^

response = input("Type R for rock, P for paper and S for scissors: ")

while response != "" : 
    
    randnumber=random.randint(0,2)
    if response == ("R") :
        if randnumber == 0 :
            print("Rock-TIE")
        elif randnumber == 1 :
            print("Paper-YOU LOSE")
        else :
            print("Scissors-YOU WIN")
    elif response == ("P") :
        if randnumber == 0 :
            print("Rock-YOU WIN")
        elif randnumber == 1 :
            print("Paper-TIE")
        else :
            print("Scissors-YOU LOSE")
    elif response == ("S") :
        if randnumber == 0 :
            print("Rock-YOU LOSE")
        elif randnumber == 1 :
            print("Paper-YOU WIN")
        else :
            print("Scissors-TIE")
    else :
        print("That is not a valid input")
    response = input("Type R for rock, P for paper and S for scissors or [Enter] to exit: ")
