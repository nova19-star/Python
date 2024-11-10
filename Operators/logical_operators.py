# AND 
def AND(a, b):
    return a and b

# Examples
print(AND(True, True))   # Output: True
print(AND(True, False))  # Output: False

# OR
def OR(a, b):
    return a or b

# Examples
print(OR(True, False))   # Output: True
print(OR(False, False))  # Output: False

# NOT
def NOT(a):
    return not a

# Examples
print(NOT(True))   # Output: False
print(NOT(False))  # Output: True

# XOR
def XOR(a, b):
    return a != b

# Examples
print(XOR(True, False))  # Output: True
print(XOR(True, True))   # Output: False
