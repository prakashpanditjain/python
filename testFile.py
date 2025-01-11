import time
from datetime import datetime
from functools import wraps


def decorator_fun(fun):
    """
    This is decorator function
    :param fun: It takes function as argument
    :return: it will return the wrapper function
    """
    @wraps(fun)
    def wrapper(*args,**kwargs):
        """
        This is wrapper function
        :param args: args
        :param kwargs: kwargs
        :return: it will return the result
        """

        start_time = time.time()
        print(start_time)
        result = fun(*args,**kwargs)

        end_time = time.time()
        total_time = end_time - start_time
        print(f"Function {fun.__name__} has taken {total_time} seconds to run")
        return result

    return wrapper



@decorator_fun
def trial_fun():
    """
    this is trial_ function
    :return: sleep for some seconds
    """
    sec = 2
    time.sleep(sec)
    print(f"This fun has delayed by {sec} sec")

# p = trial_fun()


if __name__ == '__main__':
    f = trial_fun()
    print(trial_fun.__name__)
    print(trial_fun.__annotations__)
    print(trial_fun.__doc__)
