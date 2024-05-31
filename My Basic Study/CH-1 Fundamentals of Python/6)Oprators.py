# Arithmetic operators
x = 10
y = 3
print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.3333333333333335
print(x % y)  # Output: 1
print(x ** y) # Output: 1000
print(x // y) # Output: 3

# Comparison operators(Relation operators)
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

# Logical operators
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)    # Output: False
print(list1 is not list2)# Output: True

# Membership operators
print(1 in list1)    # Output: True
print(4 not in list1)# Output: True

# Bitwise operators
num1 = 10   # Binary representation: 1010
num2 = 4    # Binary representation: 0100
print(num1 & num2)  # Output: 0 (Bitwise AND)
print(num1 | num2)  # Output: 14 (Bitwise OR)
print(num1 ^ num2)  # Output: 14 (Bitwise XOR)
print(~num1)        # Output: -11 (Bitwise NOT)
print(num1 << 1)    # Output: 20 (Left shift)
print(num1 >> 1)    # Output: 5 (Right shift)

# ternary operator
a = 10
b = 20
result = "a is minimum" if a < b else "b is minimum"
print(result)