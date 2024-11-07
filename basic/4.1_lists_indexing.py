# Indexing:
#   Indexing allows you to access a single element in a string or list.
#   Positive indices count from the start (0, 1, 2, ...).
#   Negative indices count from the end (-1, -2, -3, ...).

# indexing.py

# Indexing with Strings
text = "Hello, World!"
print("Original Text:", text)

# Accessing characters using positive indexes
print("Character at index 0:", text[0])  # 'H'
print("Character at index 7:", text[7])  # 'W'

# Accessing characters using negative indexes
print("Character at index -1:", text[-1])  # '!'
print("Character at index -6:", text[-6])  # 'W'

# Indexing with Lists
numbers = [10, 20, 30, 40, 50]
print("\nOriginal List:", numbers)

# Accessing elements using positive indexes
print("Element at index 2:", numbers[2])  # 30
print("Element at index 4:", numbers[4])  # 50

# Accessing elements using negative indexes
print("Element at index -1:", numbers[-1])  # 50
print("Element at index -3:", numbers[-3])  # 30
