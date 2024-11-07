# most_called_functions.py

# Most commonly used Python built-in functions with simple examples.

# 1. len() - Returns the length of an object (e.g., string, list, etc.)
# Example: Get the length of a string
my_string = "Hello, World!"
print(f"Length of the string '{my_string}': {len(my_string)}")  # Output: 13

# 2. type() - Returns the type of an object
# Example: Check the type of an object
print(f"Type of my_string: {type(my_string)}")  # Output: <class 'str'>
print(f"Type of my_list: {type(my_list)}")      # Output: <class 'list'>

# 3. str() - Converts an object to a string
# Example: Convert an integer to a string
my_number = 100
print(f"Integer as string: {str(my_number)}")  # Output: '100'

# 4. int() - Converts a string or a float to an integer
# Example: Convert a string to an integer
num_str = "42"
print(f"String as integer: {int(num_str)}")  # Output: 42

# 5. float() - Converts a string or integer to a float
# Example: Convert a string to a float
float_str = "7.89"
print(f"String as float: {float(float_str)}")  # Output: 7.89

# 6. sum() - Returns the sum of all items in an iterable
# Example: Get the sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers}: {sum(numbers)}")  # Output: 15

# 7. max() - Returns the largest item in an iterable
# Example: Get the maximum value in a list
print(f"Maximum value in {numbers}: {max(numbers)}")  # Output: 5

# 8. min() - Returns the smallest item in an iterable
# Example: Get the minimum value in a list
print(f"Minimum value in {numbers}: {min(numbers)}")  # Output: 1

# 9. abs() - Returns the absolute value of a number
# Example: Get the absolute value of a negative number
negative_num = -10
print(f"Absolute value of {negative_num}: {abs(negative_num)}")  # Output: 10

# 10. round() - Rounds a floating point number to the nearest integer
# Example: Round a floating-point number
pi = 3.14159
print(f"Rounded value of {pi}: {round(pi)}")  # Output: 3

# 11. sorted() - Returns a sorted list of the specified iterable's elements
# Example: Sort a list of numbers
unsorted_numbers = [5, 3, 8, 1, 4]
print(f"Sorted numbers: {sorted(unsorted_numbers)}")  # Output: [1, 3, 4, 5, 8]

# 12. range() - Returns an iterable that generates a sequence of numbers
# Example: Create a range of numbers from 0 to 4
print(f"Range from 0 to 4: {list(range(5))}")  # Output: [0, 1, 2, 3, 4]

# 13. zip() - Combines two or more iterables element-wise into tuples
# Example: Combine two lists into tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped lists: {zipped}")  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# 14. any() - Returns True if any element of an iterable is True
# Example: Check if any element is True
values = [False, False, True]
print(f"Any True value in the list? {any(values)}")  # Output: True

# 15. all() - Returns True if all elements of an iterable are True
# Example: Check if all elements are True
values = [True, True, True]
print(f"All True values in the list? {all(values)}")  # Output: True

# 16. input() - Reads a line from input (as a string)
# Example: Take user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# 17. id() - Returns the unique identifier for an object
# Example: Get the ID of an object
my_variable = 10
print(f"ID of my_variable: {id(my_variable)}")

# 18. reversed() - Returns an iterator that accesses the given sequence in the reverse order
# Example: Reverse a string
string = "Python"
reversed_string = ''.join(reversed(string))
print(f"Reversed string: {reversed_string}")  # Output: nohtyP

# 19. slice() - Returns a slice object representing a set of indices
# Example: Create a slice from index 1 to 4, 4 not included
my_list = [10, 20, 30, 40, 50]
slice_obj = slice(1, 4)
print(f"Sliced list: {my_list[slice_obj]}")  # Output: [20, 30, 40]

# 20. map() - Applies a function to all the items in an iterable
# Example: Use map to double all elements in a list
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")  # Output: [2, 4, 6, 8]

# 21. filter() - Filters elements from an iterable based on a condition
# Example: Use filter to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]
