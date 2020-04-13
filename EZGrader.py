Correct = eval(input("Total Correct: "))
#Total   = eval(input("Total Problems: "))
Total = 65
Result  = round((Correct/Total)*100,2)
print(Result, "%")

if Result >= 73 :
    print("You passed, Congrats!")
else :
    print("You failed")


