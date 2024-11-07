# Bitwise Operator 

# Bitwise AND (Ampersand: &)
a = 11       # 1011 in binary
b = 10       # 1010 in binary

result = a & b  # 1011 & 1010 = 1010    # Performs an AND operation on each bit
print(result)   # Output: 10    

# Bitwise OR ( Pipe: |)
result = a | b  # 1011 | 1010 = 1011    # Performs an OR operation on each bit
print(result)   # Output: 11

# Bitwise NOT (~)
result = ~a  # ~1011 = -(1011 + 1) = -12    # Flips each bit of a
print(result)  # Output: -12

# Bitwise XOR (^)
result = a ^ b  # 1011 ^ 1010 = 0001
print(result)   # Output: 1