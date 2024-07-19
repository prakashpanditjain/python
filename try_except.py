
#USE OF TRY EXCEPET ELSE AND FINALLY BLOCKS

def divide_numbers(a, b):
    try:
        # Try to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle the division by zero error
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle the error if a non-numeric type is provided
        print("Error: Both arguments must be numbers.")
    else:
        # This block executes if no exceptions were raised
        print(f"The result is {result}.")
    finally:
        # This block always executes, regardless of whether an exception was raised or not
        print("Execution completed.", end='\n')

# Example usage
# divide_numbers(10, 2)  # Successful division
# divide_numbers(10, 0)  # Division by zero
# divide_numbers(10, 'a')  # Invalid type