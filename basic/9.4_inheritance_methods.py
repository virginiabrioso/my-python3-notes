# In Python, classes can inherit from other classes. 
# When a class inherits from another, it inherits both the attributes and methods of the parent class.
# This allows you to create a hierarchy of classes and reuse code.

# inheritance_methods.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's constructor
        self.breed = breed

    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        print(f"{self.name} meows.")

# Creating instances
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

# Calling overridden methods
dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
