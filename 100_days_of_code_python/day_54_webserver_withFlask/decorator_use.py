class User():
    def __init__(self, username):
        self.username = username
        self.is_logged_in = False

def is_authenticated_decorators(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorators
def create_blog_post(user):
    print(f"this is {user.username}'s new blog post")


new_user  = User("prakash")

new_user.is_logged_in = True
create_blog_post(new_user)




# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
        return function(*args)
    return wrapper



# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)