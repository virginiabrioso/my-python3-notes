# A dictionary is an unordered collection of key-value pairs. 
# It’s used to store data in pairs, where each key is unique and maps to a specific value.

# Characteristics:
#   Unordered: Elements are not stored in a specific order (before Python 3.7).
#   Mutable: You can change, add, or remove elements.
#   Unique keys: Each key must be unique, but values can be duplicated.
#   Fast lookup: You can quickly look up values by their key.

# dictionaries.py

# Defining a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland"
}

# Accessing values using keys
print("Name:", person["name"])  # 'Alice'
print("Age:", person["age"])    # 25

# Modifying a value
person["age"] = 26  # Change age from 25 to 26
print("\nDictionary after modifying age:", person)

# Adding a new key-value pair
person["job"] = "Engineer"
print("\nDictionary after adding 'job':", person)

# Removing a key-value pair
del person["city"]
print("\nDictionary after deleting 'city':", person)

# Using the get() method to access values (avoids KeyError)
job = person.get("job", "Not found")
print("\nJob using get():", job)

# Iterating over keys and values
print("\nIterating over the dictionary:")
for key, value in person.items():
    print(key, ":", value)

# Checking if a key exists
if "name" in person:
    print("\n'Name' key exists in the dictionary.")
