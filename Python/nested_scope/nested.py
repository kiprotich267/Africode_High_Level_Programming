#this is a nested function example

def calculator(operation):
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        return a/b
    
    if operation =='add':
        return add
    elif operation == 'subtract':
        return subtract
    elif operation == 'multiply':
        return multiply
    elif operation == 'dide':
        return divide
    else:
        return "invalid operation" 
    
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


calculation = calculator(operation)

if calculation != "invalid operation":
    result = calculation(a, b)
    print(f"Result of {operation} is: {result}")
else:
    print(calculation)
    
