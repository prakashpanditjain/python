import time


def log_execution_time(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"starting execution of '{fun.__name__}' ")
        result = fun(*args, **kwargs)

        end_time = time.time()
        print(f"Execution end time of '{fun.__name__}' is {end_time}")
        print(f"Execution of '{fun.__name__}' has completed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper