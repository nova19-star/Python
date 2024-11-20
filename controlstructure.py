# Control structure     # it is a block of code that determines the flow of execution based on certain conditions or repetitions.
# 1. Conditional statement     # allow you to execute certain blocks of code based on whether a condition is True or False. 

# simple if condition:
a = 10
if a < 15:
    print(a, "is less than 15")

# else statement:
a = 8
if a < 5:
    print(a, "is less than 5")
else:
    print(a, "is greater than 5")

# elif condition:
x = 100
z = 200
if x > 100:
    print(x, "is bigger than 200")
elif x < 200:
    print(x, "is smaller than 200")
else:
    print(x, "is not equal to 200")

# Nested if statement
x = 5
if x > 0:
    if x < 10:
        print("x is between 0 and 10")
    else:
        print("x is 10 or greater")
else:
    print("x is negative or zero")

# Write a python program to find maximum between three numbers
a = 13
b = 7
c = 3

if a >= b and a >= c:
    print(a, "is maximum")
elif b >= a and b >= c:
    print(b, "is maximum")
else:
    print(c, "is maximum")

# Write a python program to calculate area of a circle. Given r = 4
r = 4
area = 3.14 * r**2
print("Area of a circle:", area)

# Write a python program to calculate area of a triangle as well as rectangle given b = 4, h = 12
b = 4
h = 12
triangle_area = 0.5 * b * h
rectangle_area = b * h
print("Area of a triangle:", triangle_area)
print("Area of a rectangle:", rectangle_area)
