# A class method operates on the class itself, rather than on an instance. 
# It takes cls as the first argument instead of self. 
# Class methods are used to define behaviors that are related to the class but not necessarily 
# to any particular instance.

# class_methods.py

class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

    # Class method to get the company name
    @classmethod
    def get_company_name(cls):
        return cls.company_name
    
    # Class method to change the company name
    @classmethod
    def set_company_name(cls, new_name):
        cls.company_name = new_name

# Creating instances of Employee
emp1 = Employee("Alice", "Engineer")
emp2 = Employee("Bob", "Manager")

# Accessing class methods
print(Employee.get_company_name())  # Output: TechCorp

# Modifying the class variable using a class method
Employee.set_company_name("NewTech")
print(Employee.get_company_name())  # Output: NewTech

