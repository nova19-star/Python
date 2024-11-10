# Bitwise left shift operator (<<)      # For +ve number

                    # This operation effectively multiplies the number by 2^n, where n is the number of positions shifted.
# result = a << n     # a is the number to shift.
                    # n is the number of positions to shift to the left.

a = 5       # In binary: 0101
n = 1       # Shift left by 1 position
            # converts to 8 bit => 000000101  
            # Shifting 000000101 one position to the left gives 00001010, which is 10 in decimal
print(5<<1)  # Output: 10

a = 3       # In binary: 0011
n = 2       # Shift left by 2 positions
result = a << n
print(3<<2)  # Output: 12     

# Bitwise left shift operator (>>)      # For -ve number 

a = -5       # In binary: 0101 (5)
n = 1       # IShift Left by 1 position
            # converts to 8 bit => 00000101
            # Find One's complimentary => inverte 00000101 --> 11111010 
            # Find Two's complimentary => add 00000001 to One's compliment 
            # 11111010 + 00000001 = 11111011 (-5)
            # Shifting 11111011 one position to left gives 11110110, 
            # This is still in two's compliment
            # Again inverte 11110110 --> 00001001  
            # Add 00000001 to 00001001 --> 10001010 (-10) 
print(a<<1)

# Bitwise Right shift operator (>>)      # For +vs number

a = 5       # In binary: 0101
n = 1       # Shift Right by 1 position
            # converts to 8 bit => 000000101  
            # Shifting 000000101 one position to the Right gives 00000010, which 2 in decimal
print(5>>1)  # Output: 2

# Bitwise left shift operator (>>)      # For -ve number 

a = -5       # In binary: 0101 (5)
n = 1       # Shift Left by 1 position
            # converts to 8 bit => 00000101
            # Find One's complimentary => inverte 00000101 --> 11111010 
            # Find Two's complimentary => add 00000001 to One's compliment 
            # 11111010 + 00000001 = 11111011 (-5)
            # Shifting 11111011 one position to Right gives 01111101, 
            # This is still in two's compliment
            # Again inverte 11110110 --> 00001001  
            # Add 00000001 to 00001001 --> 10001010 (-10) 
print(a>>1)
