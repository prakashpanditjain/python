import random

print(
    "Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the "
    "game")

number_to_guess = random.randrange(50)

guess_counter = 0

chances = 8

while guess_counter < chances:
    # take an input from the user about the guess
    guess_counter += 1

    guess_number = int(input("Enter your number: "))

    number_dict = {
        1: 'st',
        2: 'nd',
        3: 'rd',
        4: 'th',
        5: 'th',
        6: 'th',
        7: 'th',
        8: 'th',
    }

    if guess_number == number_to_guess:
        print(f"Congratulations!! You have got a right number : {guess_number}")

        for key, value in number_dict.items():
            if guess_counter == key:
                print(f"on your {key}{value} chance")
                if guess_counter >= 7:
                    print("Bach gaya sale :>")
        break

    elif guess_counter >= chances and guess_number != number_to_guess:
        print(f"You have exhausted all {chances} chances , Better luck next time!!")

    elif guess_number < number_to_guess:
        print("You are lower side")

    elif guess_number > number_to_guess:
        print("You are higher side")
