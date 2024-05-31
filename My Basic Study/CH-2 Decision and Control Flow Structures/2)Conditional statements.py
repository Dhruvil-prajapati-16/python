# nested if else (if..else) 
print('nested') 
x = 10
y = 5

if x > y:
    print("x is greater ")
    if x == 10:
        print("x is equal to 10")
else:
    print("y is greater ")

#ladder if else ( if..elif..else )
print("ladder")

x = 10
y = 5

if x > y:
    print("x is greater than y")
elif x == 10:
    print("x is equal to 10")
else:
    print("y is  greater")

#match-case
day = 4 
match day:
    case 0:
        day_name = "Monday"
    case 1:
        day_name = "Tuesday"
    case 2:
        day_name = "Wednesday"
    case 3:
        day_name = "Thursday"
    case 4:
        day_name = "Friday"
    case 5:
        day_name = "Saturday"
    case 6:
        day_name = "Sunday"
    case _:
        day_name = "Invalid day of the week"

print(day_name)  # Output: Friday
