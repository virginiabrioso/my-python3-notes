# A class in Python is essentially a blueprint for creating objects. 
# Objects created from the same class share the same structure and behavior (attributes and methods).

# A class can contain:
#   Attributes (Instance Variables): Data that is associated with a specific object of the class.
#   Methods: Functions that define the behavior of the objects of the class.
# classes_and_ttributes_and_methods.py

class Car:
    # The constructor __init__ method initializes instance variables
    def __init__(self, make, model, year):
        self.make = make       # Instance variable
        self.model = model     # Instance variable
        self.year = year       # Instance variable
    
    # A method that prints car details
    def display_details(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Corolla", 2021)
car2 = Car("Honda", "Civic", 2020)

# Accessing methods and instance variables
car1.display_details()  # Output: 2021 Toyota Corolla
car2.display_details()  # Output: 2020 Honda Civic
