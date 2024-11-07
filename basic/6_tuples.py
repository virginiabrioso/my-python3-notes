# A tuple is an ordered, immutable collection of elements. Once created, you cannot modify the elements of a tuple.
# Tuples are useful when you need to store data that should not be changed.

# Characteristics:
#   Ordered: Elements have a defined order.
#   Immutable: Cannot be modified after creation.
#   Can contain mixed data types: Tuples can store a mix of data types.
#   Supports indexing, slicing, and iteration.

# tuples.py

# Defining a tuple
coordinates = (10.0, 20.0)

# Accessing elements using indexing
print("First coordinate:", coordinates[0])  # 10.0
print("Second coordinate:", coordinates[1])  # 20.0

# Attempting to modify a tuple (will result in an error)
# coordinates[0] = 15.0  # Uncommenting this will raise a TypeError

# Slicing a tuple
sub_coordinates = coordinates[0:1]
print("\nSliced tuple:", sub_coordinates)  # (10.0,)

# Tuple with mixed data types
person_info = ("Alice", 25, 5.7)
print("\nTuple with mixed data types:", person_info)

# Nested tuples
nested_tuple = (1, 2, (3, 4, 5), 6)
print("\nNested tuple:", nested_tuple)
print("Accessing nested tuple:", nested_tuple[2][1])  # 4

# Iterating through a tuple
print("\nIterating over the tuple:")
for coord in coordinates:
    print(coord)
