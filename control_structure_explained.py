# Control structure     # it is a block of code that determines the flow of execution based on certain conditions or repetitions.
# 1. Conditional statement     # allow you to execute certain blocks of code based on whether a condition is True or False. 
    # if condition:
        # code block to execute if condition is True

    # elif statement: 
        # Stands for "else if," and it checks another condition if the previous one was False.

    # else statement:
        # Executes a block of code if none of the previous conditions were True.
# simple if condition:
a = 10      # Assigns the value 10 to the variable 'a'  
if a < 15:      # Checks if the value of 'a' is less than 15
    print(a, "is less then 15")     # If the condition is True, it prints '10 is less than 15'

# else statement:
a = 8       # Assigns the value 8 to the variable 'a'
if a < 5:       # Checks if the value of 'a' is less than 5      
    print(a, "is less then 5")      # If the condition is True, it prints '8 is less than 5'
else:            # If the condition in the 'if' statement is False, the code in the 'else' block runs
    print(a, "is greater then 5")       # Since 'a' is 8, it prints '8 is greater than 5'

# elif condition:
x = 100     # Assigns the value 100 to the variable 'x'
z = 200     # Assigns the value 200 to the variable 'z'

if x > 100:     # Checks if the value of 'x' is greater than 100
    print(x, "is bigger than 200")      # If the condition is True, it would print 'x is bigger than 200'
elif x < 200:       # If the first condition is False, it checks if 'x' is smaller than 200
    print(x, "is smaller than 200")     # Since 'x' (100) is smaller than 200, this will print '100 is smaller than 200'
else:       # If neither the 'if' nor the 'elif' condition is True, this block will execute
    print(x, "is not equal to 200")     # This block would run if 'x' were neither greater than 100 nor smaller than 200


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
area = 3.14*r**2
print("Area of a circle:",area)

# Write a python program to calculate area of a triangle as well as rectangle given b = 4, h = 12
b = 4
h = 12
triangle_area = 0.5*b*h
ractangle_area = b*h
print("Area of a triangle:",triangle_area)
print("Area of a ractangle:",ractangle_area)
