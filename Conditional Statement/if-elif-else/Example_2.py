""" How can you create a program that takes a student's marks as input and uses if-elif statement to 
determine their corresponding grade? """

marks = int(input("Enter a marks:"))
if marks > 90 and marks <= 100:
    print("Your grade is A")
elif marks > 80 and marks <= 90:
     print("Your grade is B")
elif marks > 70 and marks <= 80:
     print("Your grade is C")
elif marks > 60 and marks <= 70:
     print("Your grade is D")
elif marks >= 50 and marks <= 60:
     print("Your grade is E")
else:
     print("Your grade is F")