""" How can you use nested if-else statement to determine if a temperature input is within a certain range , 
and displays whether its low or high? """

temp = float(input("Enter a temperature:"))
if temp >= 0:
    if temp <=30:
        print("The temperature is low.")
    else:
        print("The temperature is high.")
else:
    print("Invalid temperature entered.")