'''

1. **Ordered Collection:** Like lists, tuples are ordered collections of elements. This means the elements in a tuple maintain their order of insertion, and you can access them by their indices.
2. **Immutable:** Tuples are immutable, meaning once created, you cannot change the elements of a tuple. You cannot add, remove, or modify elements in a tuple after its creation. However, if an element is mutable (like a list), you can modify the elements within it.
3. **Heterogeneous Data:** Tuples can contain elements of different data types. You can have integers, floats, strings, lists, other tuples, etc., all within the same tuple.
4. **Indexed Access:** Similar to lists, you can access individual elements of a tuple using their indices. Indexing starts from 0 for the first element and proceeds sequentially.
5. **Size and Performance:** Tuples are generally more memory-efficient than lists because they are immutable. They have a fixed size, so Python can allocate memory accordingly, leading to better performance in certain scenarios.
6. **Iteration:** You can iterate over the elements of a tuple using loops (e.g., `for` loops), just like you can with lists.
7. **Nesting:** Tuples can be nested within each other. This means you can have tuples containing other tuples as elements, allowing for the creation of nested data structures.
8. **Hashable:** Tuples are hashable, which means they can be used as keys in dictionaries and as elements of sets. This is because tuples are immutable and thus their contents cannot change, making them suitable for use in scenarios where immutability is required.

'''

# Creating a tuple
tuplex = (1, 2, 3, 4, 5)
print("Original Tuple:", tuplex)

# Accessing elements
print("Accessing Element at Index 0:", tuplex[0])

# Slicing
print("Sliced Tuple:", tuplex[1:4])

# Length
print("Length of Tuple:", len(tuplex))

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition 
print("Repeated Tuple:", tuplex * 2)

# Membership
print("Is 2 present in Tuple?", 2 in tuplex)

# Count
print("Count of 3 in Tuple:", tuplex.count(3))

# Index
print("Index of 4 in Tuple:", tuplex.index(4))

# Convert tuple to list
listx = list(tuplex)
print("List from Tuple:", listx)

# Append an element to the list
listx.append(8)

# Convert the modified list back to a tuple
print("Tuple from Modified List:",  tuple(listx))

# Pop an element from the list
listx.pop()

# Convert the modified list back to a tuple

print("Final Tuple:", tuple(listx))

for key in tuplex:
    print(key)