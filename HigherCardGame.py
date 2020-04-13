import random
computer_score = 0
player_score = 0
cards = 0
ties = 0
game_end = False
name = input("Enter your player name:  ")

suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "jack",
         "queen", "king", "ace"]
playing = True
while playing  and (cards < 26) :
    computer_face = random.choice(faces) 
    computer_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("Computer has the", computer_face, "of", computer_suit)
    print("You have the", your_face, "of", your_suit)
    if faces.index(computer_face) > faces.index(your_face):
        print("Compter Wins") 
        computer_score += 1 + ties
        ties = 0
    elif faces.index(computer_face) < faces.index(your_face):
        print(name,"Won!")
        player_score += 1 + ties
        ties = 0
    else:
        print("It's a tie!")
        ties += 1
    print("Computer-", computer_score,name, "has", player_score )
    if computer_score + player_score > 52  :
        print("Game Over")
        game_end = True
    if (game_end !=True) :
        print("________________________________________")
    elif computer_score > player_score :
        print("Computer Wins the Game! Better luck nex time")
    elif computer_score < player_score :
        print( name, "Wins the Game!")
    


    answer = input("Click [Enter] to keep going, q to quit: ")
    print("------------NEXT-ROUND-------------")
    
    playing = (answer == "")
    