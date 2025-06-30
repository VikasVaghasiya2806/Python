# Very Simple Calculator in Python

# Get the first number
num1 = float(input("Enter the first number: "))

# Get the operator
op = input("Enter the operation (+, -, *, /): ")

# Get the second number
num2 = float(input("Enter the second number: "))

# Use eval to compute the result
result = eval(str(num1) + op + str(num2))

# Print the result
print("Result:", result)
