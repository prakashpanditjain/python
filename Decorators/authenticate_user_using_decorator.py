logging_info = False


def authenticate_users():
    def decorator(fun):
        def wrapper(*args):
            global logging_info
            if logging_info == True:
                fun(*args)
            else:
                print("User not authenticated. Please log in.")

        return wrapper

    return decorator


@authenticate_users()
def withdraw(amount):
    print(f"Withdrawing {amount}")


@authenticate_users()
def check_balance(args: int):
    print(f"your current balance is {1000 - args}")


def login():
    global logging_info
    logging_info = True
    print("You are logged in")


if __name__ == '__main__':
    # login()
    # withdraw_amount = 200
    # withdraw(withdraw_amount)
    # check_balance(withdraw_amount)

    withdraw_amount = 100
    withdraw(withdraw_amount)
    check_balance(withdraw_amount)
