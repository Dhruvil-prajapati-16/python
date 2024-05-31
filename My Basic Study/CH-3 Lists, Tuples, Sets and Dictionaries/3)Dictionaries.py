"""
Unordered Collection:

Dictionaries are unordered collections of items. Each item is a key-value pair. In Python 3.7 and later versions, dictionaries maintain the insertion order, but this is considered an implementation detail.
Mutable:

Dictionaries are mutable, meaning you can add, remove, and modify key-value pairs after the dictionary has been created.
Indexed by Keys:

Unlike lists and tuples, which are indexed by a range of numbers, dictionaries are indexed by keys. Keys can be of any immutable data type (strings, numbers, tuples).
Dynamic Size:

Dictionaries can grow and shrink in size as needed. You can add or remove key-value pairs at any time.
Heterogeneous Data:

Both keys and values in a dictionary can be of any data type. This allows for the storage of complex data structures.
Fast Lookup:

Dictionaries provide average-case O(1) time complexity for lookups, insertions, and deletions, making them very efficient for retrieving and managing data.
Keys are Unique:

Keys in a dictionary must be unique. If you attempt to store a value with a key that already exists, the old value associated with that key will be overwritten.
Dictionary Comprehensions:

Like list comprehensions, Python supports dictionary comprehensions, which provide a concise way to create dictionaries.
Methods for Efficient Data Management:

Dictionaries come with a variety of methods that facilitate efficient data management, including keys(), values(), items(), get(), update(), pop(), and more.

"""

# Creating a dictionary
dictx = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Original Dictionary:", dictx)

# Accessing values
print("Name:", dictx["name"])

# Adding a new key-value pair
dictx["email"] = "alice@example.com"
print("After Adding Email:", dictx)

# Modifying an existing value
dictx["age"] = 26
print("After Modifying Age:", dictx)

# Removing a key-value pair
del dictx["city"]
print("After Deleting City:", dictx)

# Using the pop() method
email = dictx.pop("email")
print("Popped Email:", email)
print("After Popping Email:", dictx)

# Using the get() method
age = dictx.get("age", "Not found")
print("Age:", age)

# Checking if a key exists
if "name" in dictx:
    print("Name is a key in dictx")

# Iterating over keys
for key in dictx:
    print("Key:", key)

# Iterating over values
for value in dictx.values():
    print("Value:", value)

# Iterating over key-value pairs
for key, value in dictx.items():
    print(f"Key: {key}, Value: {value}")

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(5)}
print("Squared Numbers:", squared_numbers)
