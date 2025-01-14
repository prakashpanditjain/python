import random
import turtle
from turtle import Screen, Turtle
import colorgram

# Extract colors from an image using colorgram
col = colorgram.extract("images.jpeg", 20)  # Extract up to 20 colors from the image

# Initialize a list to store RGB color tuples
list_of_color = []
for _ in range(len(col)):  # Loop through the extracted colors
    rgb = col[_]  # Get the RGB object
    r = rgb.rgb[0]  # Extract the red component
    g = rgb.rgb[1]  # Extract the green component
    b = rgb.rgb[2]  # Extract the blue component
    list_of_color.append(tuple((r, g, b)))  # Add the RGB tuple to the list

# Print the extracted colors
print(list_of_color)

# Create a Turtle object and configure its properties
tim = Turtle()
turtle.colormode(255)  # Enable RGB color mode
tim.hideturtle()  # Hide the turtle cursor for better visuals
tim.speed("fastest")  # Set the drawing speed to the fastest

# Function to create a row of dots
def x_axis_movement():
    for _ in range(10):  # Draw 10 dots in a row
        tim.dot(20, random.choice(list_of_color))  # Create a dot with a random color
        tim.penup()  # Lift the pen to move without drawing
        tim.fd(50)  # Move forward to the next position
        tim.pendown()  # Put the pen down to draw

    # Move to the next row
    tim.setheading(90)  # Point the turtle upward
    tim.penup()  # Lift the pen
    tim.fd(50)  # Move up to the next row
    tim.setheading(180)  # Point the turtle left
    tim.fd(500)  # Move back to the starting position of the new row
    tim.setheading(0)  # Point the turtle right again
    tim.pendown()  # Put the pen down

# Draw 5 rows of dots
for _ in range(5):
    x_move = x_axis_movement()  # Call the row-drawing function

# Call the function one more time (seems redundant in this code)
s_mov = x_axis_movement()

# Keep the screen open until the user clicks
screen = Screen()
screen.exitonclick()