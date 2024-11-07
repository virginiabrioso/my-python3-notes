# Slicing:
#   Slicing allows you to extract a portion of a string or list.
#   The syntax is: start:stop:step.
#     start: The index where the slice starts (inclusive).
#     stop: The index where the slice ends (exclusive).
#     step: The step size (defaults to 1).
#   Slicing with negative indices counts from the end.

# slicing.py

# Slicing with Strings
text = "Hello, World!"
print("Original Text:", text)

# Slicing from index 0 to 4 (not including index 5)
print("Text from index 0 to 5:", text[0:5])  # 'Hello'

# Slicing from index 7 to end
print("Text from index 7 to end:", text[7:])  # 'World!'

# Slicing from start to index 5 (not including index 5)
print("Text from start to index 5:", text[:5])  # 'Hello'

# Slicing with step
print("Every 2nd character:", text[::2])  # 'Hoo ol!'

# Slicing with negative indices
print("Slicing with negative indices:", text[-6:-1])  # 'World'

# Slicing with Lists
numbers = [10, 20, 30, 40, 50, 60, 70]
print("\nOriginal List:", numbers)

# Slicing from index 2 to 5 (not including index 5)
print("List from index 2 to 5:", numbers[2:5])  # [30, 40, 50]

# Slicing from index 1 to end
print("List from index 1 to end:", numbers[1:])  # [20, 30, 40, 50, 60, 70]

# Slicing from start to index 4 (not including index 4)
print("List from start to index 4:", numbers[:4])  # [10, 20, 30, 40]

# Slicing with step
print("List with step 2:", numbers[::2])  # [10, 30, 50, 70]
