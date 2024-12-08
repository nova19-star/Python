# Write a c python program to calculate grade basing on percentage obtain given.

s1 = int(input("Enter your marks: "))
s2 = int(input("Enter your marks: "))
s3 = int(input("Enter your marks: "))
s4 = int(input("Enter your marks: "))

percentage = (s1+s2+s3+s4)/400*100
if (percentage >= 90):
    print("grade = O")
elif (percentage >= 80 & percentage < 90):
    print("Grade = E")
elif (percentage >= 70 & percentage < 80):
    print("Grade = A")
elif (percentage >= 60 & percentage < 70):
    print("Grade = B")
else: 
    print("Fail")