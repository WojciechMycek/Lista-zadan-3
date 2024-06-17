# app.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Add: ", add(1, 2))
    print("Subtract: ", subtract(4, 2))
    print("Multiply: ", multiply(3, 3))
    print("Divide: ", divide(10, 2))
