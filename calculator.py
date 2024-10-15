# Simple calculator program using conditional statements

# Ask the user for the first number
num1 = float(input("Enter the first number: "))
# Ask the user for the second number
num2 = float(input("Enter the second number: "))
# Ask the user for the operation
operation = input("Enter the operation (+, -, *, /): ")
# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"
# Print the result
print("Result: " + str(result))