'''
-> Ordered Collection: Lists maintain the order of elements as they are inserted.
-> Mutable: Elements of a list can be changed after the list is created.
-> Heterogeneous Data: Lists can hold elements of different data types.
-> Indexed Access: Elements in a list can be accessed using their index.
-> Dynamic Size: Lists can grow or shrink dynamically as elements are added or removed.
-> Nesting: Lists can contain other lists as elements, allowing for nested data structures.
'''

'''
-> Append()
-> extend()
-> Insert()
-> remove()
-> Pop()
-> Slice()
-> reverse()
-> len(), min() & max()
'''

'''
index()    
reverse()
copy()     
clear()    
sort()          
count()     
any()       
all()       
'''

'''
Concatenation (+)
Repetition (*)
Zip
'''
# Creating Lists:
lx = [1,2,3]
print(lx)

# itrative way to print
for key in lx:
 print(key)

# append()
print("append list",lx.append(4))

# extend()
print("extend list",lx.extend([5, 6]))

# insert()
print("insert list",lx.insert(1, 7))

# remove()
print("remove list",lx.remove(2))

# pop()
print("pop list",lx.pop(2))

# slice()
print("slice list",lx[1:4])

# reverse()

print("reverse list",lx.reverse())

# len(), min(), and max()
length = len(lx)
minimum = min(lx)
maximum = max(lx)

# Printing the results
print("Modified final List:", lx)
print("Length of List:", length)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)

#aditinal opration 

# Creating a list
l1 = [1, 2, 3, 4, 5]

# index()
print("Index of 3:", l1.index(3))

# reverse()
print("Reversed List:", l1.reverse())

# copy()
print("Copied List:",  l1.copy())

# clear()
print("Cleared List:", l1.clear())

# sort()
unsorted_list = [5, 2, 8, 1, 3]
print("Sorted List:", unsorted_list.sort())

# count()
print("Count of 3:", l1.count(3))

# any() and all()
bool_list = [True, False, True]
print("Any True in bool_list:", any(bool_list))
print("All True in bool_list:", all(bool_list))

# opration btw two list or more
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation (+)
print("Concatenated List:", list1 + list2)

# Repetition (*) 
print("Repeated List:", list1 * 3)

# Zip
print("Zipped List:", list(zip(list1, list2)))

# maths set opration 

listx = [1, 2, 3]
listy = [3, 4, 5]

# Union
union_set = set(listx).union(set(listy))
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set(listx).intersection(set(listy))
print("Intersection:", intersection_set)  # Output: {3}

# Difference
difference_set = set(listx).difference(set(listy))
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set(listx).symmetric_difference(set(listy))
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}
