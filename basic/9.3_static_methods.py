# A static method does not take self or cls as a parameter and is used when you need to perform a 
# task that is related to the class but doesn’t need access to instance or class variables.

# static_methods.py

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Calling static methods
print(Calculator.add(5, 3))  # Output: 8
print(Calculator.subtract(10, 4))  # Output: 6
