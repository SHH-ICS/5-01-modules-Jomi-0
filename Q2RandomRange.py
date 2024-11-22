# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random
print("This is a random number generator. Your numbers are the range")
x= int(input("Enter first number:"))
y=int(input("Enter second number:"))
if x<y:
    print(random.randint(x,y))
else:
    print("Your first number must be less than your second number")