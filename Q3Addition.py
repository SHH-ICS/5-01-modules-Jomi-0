# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
print("This is a random addition!")
x= int(random.randint(1,100))
y= int(random.randint(1,100))

print(x," + ",y ,"= ")
try: 
    ans=input()
    ans=int(ans)

    if int(ans) == x+y:
        print("Your answer is correct!")


    elif int(ans) != x+y:
        print("Wrong!")
        
except ValueError:
    print("Your answer must be an integer!")