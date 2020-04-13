print("math")
number_1 = eval(input("number1: "))
operation = input("operation - +,-,*,/: ")
number_2 = eval(input("number2: "))

if operation == "+":
    result = number_1 + number_2

elif operation == "-":
    result = number_1 - number_2

elif operation == "*":

    result = number_1 * number_2

elif operation == "/":
    result = number_1 / number_2

print(number_1, operation, number_2,"=",result)

x = 1+10
y = x+1 
print(y)

