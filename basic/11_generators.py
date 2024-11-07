# A generator is a special type of iterator that is defined using a function with the yield keyword. 
# Instead of returning a value all at once, a generator yields values one by one, pausing the
# function’s state until the next value is requested.

# generators.py

# A generator function that generates Fibonacci numbers up to a given limit
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a  # Yield the current value of a
        a, b = b, a + b  # Update the values of a and b

# Using the generator to get Fibonacci numbers less than 10
print("Fibonacci numbers less than 10:")
for number in fibonacci(10):
    print(number)  # Output: 0, 1, 1, 2, 3, 5, 8

# Generator for even numbers up to a given limit
def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

# Using the generator for even numbers up to 10
print("\nEven numbers less than 10:")
for even in even_numbers(10):
    print(even)  # Output: 0, 2, 4, 6, 8
