import random  # Importing the random module for generating random distances
from turtle import Screen, Turtle  # Importing Turtle graphics components

# Flag to control when the race starts
is_race_on = False

# Setting up the screen for the race
screen = Screen()
screen.setup(width=500, height=500)  # Setting screen size

# Asking the user to place their bet on a turtle color
user_bets = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

# List of turtle colors
colors = ['red', 'green', 'black', 'blue', 'pink', 'orange']
y_axis = -150  # Initial y-coordinate for the first turtle
all_turtle = []  # List to store all turtle objects

# Creating and positioning turtles
for i in range(6):  # Looping to create 6 turtles
    new_turtle = Turtle(shape='turtle')  # Creating a turtle object with a turtle shape
    new_turtle.color(colors[i])  # Assigning a color from the colors list
    new_turtle.penup()  # Lifting the pen to avoid drawing while moving
    new_turtle.goto(x=-240, y=y_axis)  # Placing the turtle at the starting line
    y_axis += 50  # Incrementing y-axis for the next turtle's position
    all_turtle.append(new_turtle)  # Adding the turtle to the list

# If the user has placed a bet, start the race
if user_bets:
    is_race_on = True  # Race begins

print(all_turtle)  # Debugging: Prints the list of all turtle objects

# Main game loop
while is_race_on:
    for turtle in all_turtle:  # Iterate through each turtle
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:  # Finish line x-coordinate
            is_race_on = False  # Stop the race
            winning_turtle = turtle.pencolor()  # Get the color of the winning turtle
            if winning_turtle == user_bets:  # Check if the user's bet matches the winner
                print("You have won!! Cheers!!!")  # User wins
            else:
                print("You have lost... Better luck next time.")  # User loses
        # Move the turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Wait for the user to close the screen
screen.exitonclick()