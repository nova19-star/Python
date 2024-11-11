# List      # It is a Mutable data structure that can store a collection of items of different type 

lst = [1,2,3,"fact",10]     # Here while going onwards 1 is in 0th Position, 2 is in 1st position, 3 is in 3rd position...   # While going backward 10 is in -1 pos, "fact" is in -2 pos, 3 is in -3 pos 

print(type(lst))        # To check data type 

# 1.    appent ( )        # To add items to a list 
lst.append ( 12 )
print(lst)

# 2.    extend ( )      # To add another list to a existing list 
lst.extend ( [5,7] )
print(lst)

# 3.    remove ( )      # To remove an item from list 
lst.remove ( "fact" )
print(lst)

# 4.    pop( )      # To remove a perticular item from list 
lst.pop( 5 )
print(lst)

# 5. reverse ( )       # To reverse the list items 
lst.reverse( )
print(lst)

# 6. sort ( )     # To sort/rearrage the list items 
lst.sort ( )
print(lst)

# 7. max ( )        # To find maximum value from a list 
print(max(lst))

# 7. min ( )        # To find minimum value from a list 
print(min(lst))

# SLICING       # A portion of list to be displayed 
lst1 = [ 1,2,3,"hello",7,10 ]   # Index starts from 0
''' Indexing from left to right ---> 0,1,2,3,4,...
Indexing from right to left -1,-2,-3,-4,... <---       
                                     lst1 = [ 1,2,3,"hello",7,10 ] 
                                              | | |    |    |  |       
                                        --->  0 1 2    3    4  5 
                                        <--- -6-5 -4  -3   -2 -1 '''

# To display third element from list                                    
print(lst1[2])                                         
                                               
# To display values from 4th to end            
print(lst1[3: ])    

# to display all values 
print(lst1[:])

# To display 3rd value from right 
print(lst1[-3])

print(lst1[2:5])        #[2:5] Here 2 is start value, so we have to start from index value 2 & 5 is the ending value and we have to stop at 'End value - 1 --> 5 - 1 = 4 (index value)

# To display number of elements from list 
lst4 = [2,3,5]

l = len(lst4)

print(l)

# Concatenate       # To add the list together 
lst2 = [2,3,5]
lst3 = [2,3,4,5,"a","b"]

print(lst2+lst3)

# Multiply      # It will print the elements, the number of times written to multiply
lst5 = [10,20,30]
print(lst5*2)

# Copy      # It copies the list
lst6 = [50,80,100]

print(lst6.copy())

# Clear     # To clear entire list
lst7 = [5,6,7]

print(lst2.clear())

