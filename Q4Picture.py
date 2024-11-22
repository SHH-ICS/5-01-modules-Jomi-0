#link to replit    https://replit.com/@jomiobasanya/MeekRoastedPipeline#main.py

import pygame
from pygame import Color, Rect, draw, display

SCREEN_SIZE = (500, 500)

# Initialize pygame
pygame.init()

# Set up the display
gameDisplay = display.set_mode(SCREEN_SIZE)

# Fill the background with sky blue
gameDisplay.fill(Color('lightblue'))

# Draw the car body
draw.rect(gameDisplay, Color('red'), Rect(150, 300, 200, 50))  # Main car body
draw.rect(gameDisplay, Color('black'), Rect(175, 275, 175, 50))  # Car roof
draw.rect(gameDisplay, Color('red'), Rect(150, 300, 200, 50))  # Main 
#car exhaust

# Draw car windows
draw.rect(gameDisplay, Color('orange'), Rect(182, 283, 65, 35))# Front window
draw.rect(gameDisplay, Color('white'), Rect(185, 285, 60, 30)) 

draw.rect(gameDisplay, Color('orange'), Rect(253, 283, 65, 35))
draw.rect(gameDisplay, Color('white'), Rect(255, 285, 60, 30))  # Back window


# Draw the wheels
draw.circle(gameDisplay, Color('black'), (175, 360), 20)  # Front wheel
draw.circle(gameDisplay, Color('grey'), (175, 360), 15)  # Front wheel
draw.circle(gameDisplay, Color('black'), (325, 360), 20)  # Rear wheel
draw.circle(gameDisplay, Color('grey'), (325, 360), 15)  # Front wheel

# Draw the sun
draw.circle(gameDisplay, Color('yellow'), (50, 50), 50)

# Display everything
display.flip()

# Wait for user input before closing the window
input("Press Enter to exit...")

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")