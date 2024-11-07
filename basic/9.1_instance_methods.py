# Instance Methods: These operate on the instance of the class and modify or use instance variables.

# instance_methods.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method that prints a greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    # Instance method that increments age
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling instance methods
person1.greet()            # Output: Hello, my name is Alice and I am 30 years old.
person1.have_birthday()    # Output: Happy Birthday, Alice! You are now 31 years old.
