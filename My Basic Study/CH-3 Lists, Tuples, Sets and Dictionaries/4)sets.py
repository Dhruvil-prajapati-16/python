'''
-> Unique Elements: Sets contain only unique elements. If you try to add a duplicate element to a set, it will be ignored.
-> Unordered: Sets do not maintain the order of elements as they are inserted. This means you cannot rely on the order of elements in a set.
-> Mutable: You can add and remove elements from a set after it's created.
-> No Duplicates: Sets automatically handle duplicates. If you try to add the same element multiple times, it will only appear once in the set.
-> Fast Membership Testing: Checking for membership (whether an element is present in the set) is very efficient in sets, even for large collections of elements.
-> Mathematical Operations: Sets support various mathematical operations such as union, intersection, difference, and symmetric difference, which can be handy in solving various problems.
-> Hashable: Sets are hashable, meaning they can be used as elements of other sets or as keys in dictionaries.
-> Creating Sets: Sets can be created using curly braces {} or the set() constructor.

'''
# Creating a set
setx = {'xyz','!',1, 2, 2, 3,'hello', 5, '$'}
print("Original Set:", setx)

# Adding elements to a set
setx.add(8)
print("After Adding 6:", setx)

# Removing elements from a set
setx.remove(3)
print("After Removing 3:", setx)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print("Union Set:", set1.union(set2))

# Intersection
print("Intersection Set:", set1.intersection(set2))

# Difference
print("Difference Set (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference Set:", set1.symmetric_difference(set2))

# Additional operations
# Checking for membership
print("Is 2 present in the set?", 2 in setx)

# Checking length
print("Length of the set:", len(setx))

print("Popped Element:", setx.pop())
print("Set after pop:", setx)

# Using discard() to remove a specific element
setx.discard(8)
print("Set after discarding 2:", setx)

print (list(setx))
