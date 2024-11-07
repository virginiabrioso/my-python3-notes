# lambda_function.py

# Lambda Functions in Python

# A lambda function is a small anonymous function defined using the `lambda` keyword.
# Unlike regular functions, lambda functions are not declared with `def`.
# Lambda functions are often used for short, one-liner functions.

# Basic Syntax:
# lambda arguments: expression

# 1. Lambda Function with No Arguments
# This lambda function takes no arguments and returns a constant string.
greet = lambda: "Hello, World!"
print(f"Lambda with no parameters: {greet()}")  # Output: 'Hello, World!'

# 2. Lambda Function with One Argument
# This lambda function takes one argument and returns its double.
double = lambda x: x * 2
print(f"Double of 5: {double(5)}")  # Output: 10

# 3. Lambda Function with Multiple Arguments
# This lambda function takes two arguments and returns their sum.
add = lambda x, y: x + y
print(f"Sum of 3 and 7: {add(3, 7)}")  # Output: 10

# 4. Lambda Functions with map()
# `map()` applies a function to every item in an iterable (like a list).
# Here we use a lambda function to double each element in the list.
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled_numbers}")  # Output: [2, 4, 6, 8]

# 5. Lambda Functions with filter()
# `filter()` is used to filter out elements from an iterable based on a condition.
# Here we use a lambda function to filter out even numbers from the list.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]

# 6. Lambda Functions with sorted()
# `sorted()` sorts an iterable based on the values of the elements.
# We can use a lambda function to specify a custom sorting key.
# Here we sort a list of tuples based on the second element of each tuple.
tuples = [(1, 2), (3, 1), (5, 0)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(f"Sorted tuples by second element: {sorted_tuples}")  # Output: [(5, 0), (3, 1), (1, 2)]

# 7. Lambda Functions with Reduce (from functools)
# The `reduce()` function from the functools module applies a binary function cumulatively to the items of an iterable.
# Here we use a lambda function to compute the product of all numbers in the list.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of the list: {product}")  # Output: 24

# Lambda functions are useful when you need a small, throwaway function for a short period.
# They are commonly used with functions like `map()`, `filter()`, and `sorted()`, where you want to define a function inline.
