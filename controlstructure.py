# Control structure     # it is a block of code that determines the flow of execution based on certain conditions or repetitions.
# 1. Conditional statement     # allow you to execute certain blocks of code based on whether a condition is True or False. 
    # if condition:
        # code block to execute if condition is True

    # elif statement: 
        # Stands for "else if," and it checks another condition if the previous one was False.

    # else statement:
        # Executes a block of code if none of the previous conditions were True.
# simple if condition:
a = 10 
if a < 15:
    print(a, "is less then 15")

# else statement:
a = 8 
if a < 5:
    print(a, "is less then 5")
else:
    print(a, "is greater then 5")

# elif condition:
x = 100
z = 200
if  x > 100:
    print(x, "is bigger then 200")
elif x < 200:
    print(x, "is smaller then 200")
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

                                                                                                                                                                                                                                                                                                                                                                                  