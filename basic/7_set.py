# A set is an unordered collection of unique elements. 
# It does not allow duplicates and is useful for mathematical set operations like union, intersection, and difference.

# Characteristics:
#   Unordered: No guaranteed order of elements.
#   Unique elements: Automatically removes duplicates.
#   Mutable: Elements can be added or removed.
#   Supports set operations: Union, intersection, and difference.

# sets.py

# Defining a set
fruits_set = {"apple", "banana", "cherry", "date"}

# Adding elements to a set
fruits_set.add("elderberry")
print("Set after adding 'elderberry':", fruits_set)

# Removing elements from a set
fruits_set.remove("banana")  # Removes 'banana'
print("\nSet after removing 'banana':", fruits_set)

# Discarding an element (does not raise an error if the element is not found)
fruits_set.discard("fig")  # 'fig' is not in the set, but no error occurs
print("\nSet after discarding 'fig':", fruits_set)

# Set operations: Union, Intersection, and Difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union of two sets (combines all elements)
union_set = set_a | set_b
print("\nUnion of set_a and set_b:", union_set)

# Intersection of two sets (common elements)
intersection_set = set_a & set_b
print("Intersection of set_a and set_b:", intersection_set)

# Difference of two sets (elements in set_a but not in set_b)
difference_set = set_a - set_b
print("Difference between set_a and set_b:", difference_set)

# Iterating over a set
print("\nIterating over the set:")
for fruit in fruits_set:
    print(fruit)
