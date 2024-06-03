import random

# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
while True:
    # Give user the information of choices
    print("please Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissor ")

    # Enter user name
    user_name = input("Enter your name as a user:")

    # take input from the user
    choice = int(input("Enter your choice:- "))

    while choice > 3 or choice < 1:
        print("Enter the valid choice: please :( ")

    # check the condition for choice name which user has entered
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("User choice is \n", choice_name)
    print("Now its computer's turn \n")

    # Computer chooses randomly any number among 1,2,3 using randint method of random module
    comp_choice = random.randint(1, 3)

    # looping until the comp_choice value equals to choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # defining the comp_choice_name for input of comp_choice which is random number

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print(f"Computer choice is --------> {comp_choice_name}")
    print(
        f"User choice VS computer Choice \n ----------------------------{choice_name} VS "
        f"{comp_choice_name}----------------------------")

    # for draw the condition if as follows
    if choice == comp_choice:
        print("Your choice and computers choice is same, Its a draw")
        print("<== ITS A TIE ==>")

    if (choice == 1 and comp_choice == 2):
        print("Paper wins ====> \n", end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print("Paper wins ==> \n", end="")
        result = 'Paper'

    if (choice == 2 and comp_choice == 3):
        print("Scissor wins ==>\n", end="")
        result = "Scissor"
    elif (choice == 3 and comp_choice == 2):
        print("Scissor wins ==>\n", end="")
        result = 'Scissor'

    if (choice == 1 and comp_choice == 3):
        print("Rock wins ==> \n", end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins ==> \n', end='')
        result = 'Rock'
    # check whos choice matching with result
    # If choice matches then he wons

    if result.lower() == 'draw':
        print('<== ITS A TIE ==>')

    if result.lower() == choice_name.lower():
        print(f'\n<== {user_name} WINS ==>')
    else:
        print('\n<== COMPUTER WINS ==>')

    print("Do you want to play again ? Yes/ NO")
    ans = input().lower()

    if ans == 'n':
        break

print("Thanks for playing")
