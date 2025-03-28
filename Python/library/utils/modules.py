print("the file running is", __name__)

def calculator(operation):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            return "cannot divide by zero"
        return a / b
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    elif operation == "multiply":
        return multiply
    elif operation == "divide":
        return divide
    else:
        return "invalid operation"
    
# results = calculator("add")(5, 3)
# print("the result is:", results)

if __name__ == "__main__":
    results = calculator("add")(5, 3)
    print("the result is:", results)
    