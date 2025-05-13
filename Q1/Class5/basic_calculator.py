# This program is a Simple & Basic Calculator

# A single Function which will work as Calc
def calculate(num1 = 20, num2 = 10, operation = "+"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by Zero!"
    else:
        result = "Input Invalid!"
    return result

# Input Fields
num1 = int(input("Enter First Number: "))
operation = input("Enter Operation: ")
num2 = int(input("Enter Second Number: "))

# Result using Keyword Arguments 
result = calculate(num1, num2, operation)
print(result)

# Result using Positional Arguments
result = calculate(10, 4, "*")
print(result)

# Result using Default Parameters
result = calculate()
print(result)
