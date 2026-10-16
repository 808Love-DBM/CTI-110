# Kristina Walker
# October 12, 2026
# P4LAB1
# Drawing shapes using loops

import turtle

# Set up the turtle drawing object

window = turtle.Screen()

honu = turtle.Turtle()

# Change color, size, and shape
honu.pensize(5)
honu.pencolor("purple")
honu.shape("turtle")

# Use a for loop to draw a square
for side in range(4):
    honu.forward(200)
    honu.right(90)

# Use a while loop to draw a triangle 
honu.fillcolor("yellow")
honu.begin_fill()

# Use a while loop to draw the triangle
num = 1
while num <= 3:
    honu.forward(200)
    honu.left(120)
    num = num + 1
honu.end_fill()





# Keep this at the bottom
window.mainloop()