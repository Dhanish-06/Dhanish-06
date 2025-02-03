# simple calculator

value = input("enter the operator + - * / \n")
num1 = int(input("enter the first num \n"))
num2 = int(input("enter the second num \n"))

if value == "+":
    result = num1 + num2
elif value == "-":
    result = num1 - num2
elif value == "*":
    result = num1 * num2
elif value == "/":
    result = num1 / num2

print(result)