# # Dictionary        # it is a data structure that stores data in key - value pair.      

# dict1 = {1: "one"}  # Initialize dict1 with a key-value pair (1: "one")
# dict2 = {2: "two"}  # Initialize dict2 with a key-value pair (2: "two")
# dict1.update(dict2)  # Update dict1 by adding all key-value pairs from dict2
# print(dict1)  # Print the updated dict1 which now contains both (1: "one") and (2: "two")

# print(dict1[1])  # Attempts to access the value associated with the key '1' in dict1. If key '1' doesn't exist, it will raise a KeyError.

# print(dict1.keys())  # Prints the keys in the dictionary dict1. This returns a view object of the keys.

# print(dict1.values())  # Prints the values in the dictionary dict1. This returns a view object of the values.

# print(dict1.get(1, "Key not found"))  # This will print "Key not found" if the key '1' does not exist in dict1.

# # To delete a key-value pair in a dictionary.
# del(dict1[1])  # Deletes the key-value pair with the key '1' from dict1. If key '1' doesn't exist, a KeyError will be raised.
# print(dict1)  # Prints the updated dictionary after the key-value pair has been deleted.

# # To clear dictionary or remove all iteams
# print(dict2.clear())    # Clears all items in dict2 and prints None.

# print(dict2)  # Will print {} since the dictionary is now empty.

# # CONTROL STRUCTURE

# Write a python program to find maximum among 2 values,

a = 5  # First value
b = 2  # Second value

if a > b:  # Check if 'a' is greater than 'b'
    print(a, "is bigger")  # If true, print 'a' is bigger
else:  # If 'b' is greater or equal to 'a'
    print(b, "is bigger")  # Print 'b' is bigger
