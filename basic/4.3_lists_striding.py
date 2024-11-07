# Striding:
#   Striding is a special case of slicing where you specify the step size.
#   It can be used to select every nth element or reverse a sequence.
#   A negative stride reverses the sequence.

# striding.py

# Striding with Strings
text = "Hello, World!"
print("Original Text:", text)

# Stride of 2 - every second character starting from index 0
print("Every second character:", text[::2])  # 'Hoo ol!'

# Stride of 3 - every third character starting from index 0
print("Every third character:", text[::3])  # 'Hl ol'

# Negative stride (reverse string)
print("Reversed string:", text[::-1])  # '!dlroW ,olleH'

# Striding with Lists
numbers = [10, 20, 30, 40, 50, 60, 70]
print("\nOriginal List:", numbers)

# Stride of 2 - every second element starting from index 0
print("Every second element:", numbers[::2])  # [10, 30, 50, 70]

# Stride of 3 - every third element starting from index 0
print("Every third element:", numbers[::3])  # [10, 40, 70]

# Negative stride (reversed list)
print("Reversed List:", numbers[::-1])  # [70, 60, 50, 40, 30, 20, 10]
