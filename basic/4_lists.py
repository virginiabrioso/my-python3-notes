# A list is an ordered, mutable collection of elements. 
# Lists are great when you need an ordered collection where elements can be modified, added, or removed.

# Characteristics:
#   Ordered: Elements maintain their order.
#   Mutable: Can be changed after creation.
#   Allow duplicates: Can contain the same element multiple times.
#   Indexed: Elements can be accessed by index.

# lists.py

# Defining a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements using indexing
print("First element:", fruits[0])  # 'apple'
print("Last element:", fruits[-1])  # 'date'

# Modifying an element
fruits[1] = "blueberry"  # Change "banana" to "blueberry"
print("\nList after modification:", fruits)

# Adding elements to the list
fruits.append("elderberry")  # Add to the end of the list
print("\nList after appending 'elderberry':", fruits)

# Inserting an element at a specific position
fruits.insert(1, "fig")  # Insert 'fig' at index 1
print("\nList after inserting 'fig' at index 1:", fruits)

# Removing an element from the list
fruits.remove("cherry")  # Remove the first occurrence of "cherry"
print("\nList after removing 'cherry':", fruits)

# Popping an element (removes and returns the last element)
last_fruit = fruits.pop()
print("\nPopped fruit:", last_fruit)
print("List after popping:", fruits)

# List slicing
subset = fruits[1:4]  # Get a slice of the list (from index 1 to 3)
print("\nList slice:", subset)

# Iterating over a list
print("\nIterating over the list:")
for fruit in fruits:
    print(fruit)
