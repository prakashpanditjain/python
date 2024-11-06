import time

role = 'admin'


def require_access(*args, **kwargs):
    def wrapper(fun):
        if role == 'admin':
            fun(*args, **kwargs)
        if role == 'user':
            ...
        else:
            print(f"The user does not have the necessary permissions")

    return wrapper


def validate_args(fun):
    def wrapper(*args):

        # if fun.__name__ == 'fetch_product_info':
        #     a = args[0]
        #     if isinstance(a, int):
        #         fun(*args)
        #     else:
        #         print(f"Input value datatype is not correct")
        # if fun.__name__ == 'create_user':
        #     a, b = args[0], args[1]
        #     condition1 = isinstance(a, str)
        #     condition2 = isinstance(b, str)
        #     if condition1 and condition2:
        #         fun(*args)
        #     else:
        #         print(f"Input value datatype is not correct")

        """To make more generic we are optimizing above wrapper function"""
        annotation = fun.__annotations__

        """
        annotation give you a key value pair of variable/ return key/ any key with data type as value in dictionary 
        form
        """
        # print("this is annotation of function",annotation)
        # print(annotation)
        args_names = fun.__code__.co_varnames[:len(args)]
        """
        fun.__code__ attribute gives you  compiled function bytecode, variable names, constants, and other attributes 
        """
        # print("this is args names taken from fun.__code__.co_varnames", args_names)
        for arg, arg_name in zip(args, args_names):
            # print(arg, arg_name)
            expected_type = annotation.get(arg_name, None)
            print("expected_type", expected_type, isinstance(arg, expected_type))
            # isinstance is used to verify if the object is instance of the class
            if expected_type and not isinstance(arg, expected_type):
                print(f"argument '{arg_name}' is expected to be {expected_type} but got {type(arg)} ")

        return fun(*args)

    return wrapper


"""
This function can benefit from role-based access control, argument validation, retry mechanisms, and more.
"""


@validate_args
def create_user(username: str, role: str):
    print(f"Creating user: {username} with role: {role}")
    return {"username": username, "role": role}


def retry_on_failure(retries=4, delay=1, backoff=3):
    def decorator(fun):
        def wrapper(*args):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return fun(*args)
                except Exception as e:
                    attempt += 1
                    print(f"Attempt {attempt} is failed: \n {e}")
                    if attempt < retries:
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        raise

        return wrapper

    return decorator


@retry_on_failure(4, 1, 3)
@validate_args
def fetch_product_info(product_id: int):
    print(f"Fetching information for product: {product_id}")
    return {"product_id": product_id, "name": "Sample Product", "price": 100}


if __name__ == '__main__':
    user = create_user("Prakash", "Admin")
    # user.get("username", )

    product_infor = fetch_product_info('3')
