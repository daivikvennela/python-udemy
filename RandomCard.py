import random
suits = [ "clubs", "diamonds", "hearts", "spades"]
faces = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
my_face = random.choices(faces)
my_suit = random.choices(suits)
print("Your card is the ", my_face, "of", my_suit )


