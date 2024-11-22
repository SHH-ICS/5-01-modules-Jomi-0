# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

a= input("What is your a?...Must be a number")
b= input("What is your b? ...Must be a number")
a= float(a)**2
b= float(b)**2
c= a+b
c=math.sqrt(c)
print("the length of your hypotenuse is ",c)