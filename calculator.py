def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations: add, subtract, multiply, divide")

    operation = input("Choose an operation: ").lower()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            result = "Invalid operation selected."

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()