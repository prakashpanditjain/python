import random

print(
    "Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the "
    "game")

number_to_guess = random.randrange(50)

guess_counter = 0

chances = 8

while guess_counter < chances:
    # take a input from the user about the guess
    guess_counter += 1

    guess_number = int(input("Enter your number: "))

    if guess_number == number_to_guess:
        print(f"Congratulations!! You have got a right number : {guess_number}")
        if guess_number == 1:
            print(f"On your {guess_counter}st chance")
        if guess_number == 2:
            print(f"On your {guess_counter}nd chance")
        if guess_number == 4:
            print(f"On your {guess_counter}rd chance")
        else:
            print(f"On your {guess_counter}th chance")

        break
    elif guess_counter >= chances and guess_number != number_to_guess:
        print(f"You have exhausted all {chances} chances , Better luck next time!!")

    elif guess_number < number_to_guess:
        print("You are lower side")

    elif guess_number > number_to_guess:
        print("You are higher side")

