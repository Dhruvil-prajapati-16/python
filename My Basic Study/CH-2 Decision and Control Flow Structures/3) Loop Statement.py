# Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Printing numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1 2 3 4 5

# Regular while loop
number = int(input("Enter a number (0 to exit): "))
while number != 0:
    number = int(input("Enter another number (0 to exit): "))
print("Goodbye!")

# Mimicking do-while loop
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        print("Thank you!")
        break
    else:
        print("That's not a positive number. Try again.")

# Using break to exit the loop
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# Output: 1 2 3 4

# Using continue to skip an iteration
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5

# The else block will execute because the loop completes normally
for num in range(1, 4):
    print(num)
else:
    print("Loop completed")
# Output: 1 2 3
#         Loop completed

# The else block will not execute because the loop is terminated by break
for num in range(1, 4):
    if num == 2:
        break
    print(num)
else:
    print("Loop completed")
# Output: 1

# Printing a 2D grid )Nested loop()
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
# Output:
# (0, 0) (0, 1) (0, 2) 
# (1, 0) (1, 1) (1, 2) 
# (2, 0) (2, 1) (2, 2)

# Looping through keys and values of a dictionary
dict_example = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict_example.items():
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3
