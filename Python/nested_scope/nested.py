#this is a nested function example

def calculator(operation):
    def add(a, b):
        return a + b
    """
    this function returns the sum of two numbers
    """
    def subtract(a, b):
        return a - b
    """
    this function subtracts two numbers
    """
    
    def multiply(a, b):
        return a * b
    """
    this function multiplies two numbers
    """
    
    def divide(a, b):
        return a/b
    """
    this function divides two numbers
    """
    if operation =='add':
        return add
    elif operation == 'subtract':
        return subtract
    elif operation == 'multiply':
        return multiply
    elif operation == 'divide':
        return divide
    else:
        return "invalid operation" 
"""
this returns an error message if the operation is not valid
"""
    
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


calculation = calculator(operation)

if calculation != "invalid operation":
    result = calculation(a, b)
   
    print(f"Result of {operation} is: {result}")
else:
    print(calculation)
    """
    this prints the result of the operation
    """
   
    
