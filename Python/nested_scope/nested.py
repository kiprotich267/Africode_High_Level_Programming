#this is a nested function example

def calculator(operation):
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def devide(a, b):
        return a/b
    
    if operation =='add':
        return add
    elif operation == 'subtract':
        return subtract
    elif operation == 'multiply':
        return multiply
    elif operation == 'devide':
        return devide
    else:
        return "invalid operation" 
    
results_add = calculator("add")(2,3)
print(f"Addition results:{results_add}")
    
