
def fibonacci_number():
    first_number = 0
    second_number = 1
    fib_list = [first_number,second_number ]
    # number_of_fib = int(input("Upto which number you wanna print the fibonacci number\n"))
    while True:

        next_number = first_number + second_number
        first_number= second_number
        second_number  = next_number

        if next_number < 30:
            fib_list.append(next_number)
        else:
            break
    return fib_list