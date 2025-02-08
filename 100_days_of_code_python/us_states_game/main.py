import turtle
from turtle import Turtle,Screen

import pandas

#create screen
screen = Screen()
screen.title('Us states game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#read the dataframe of states coordinates
df = pandas.read_csv('50_states.csv')
correct_guess = []
score = 0

for i in range(50):
    answer_text = screen.textinput(title=f"{score}/50 States Correct",prompt='Whats the new state name?').upper()
    print(answer_text)

    #exit on type exit
    if answer_text == 'EXIT':
        break

    state_availability = df.state.str.upper() == answer_text

    #check for state available in dataframe and extract data corresponding to state
    check_state = df[state_availability]

    #check is state is available in data
    bool_exp = (df.state.str.upper().isin([answer_text]).any())

    if bool_exp:
        #append the correct state name to list to write into another csv
        correct_guess.append(answer_text)
        score += 1

        #create turtle
        new_text = Turtle()
        new_text.penup()
        new_text.hideturtle()
        x_cor = check_state.x.values[0]
        y_cor = check_state.y.values[0]

        #Goto the coordinates
        new_text.goto(x_cor,y_cor)
        new_text.write(answer_text, align='center',font=('Courier',10,'normal'))
    else:
        pass
