class Connection:  # Define a class named `Connection`.
    __instance = None  # Class-level private variable to store the singleton instance.

    def __new__(cls, *args, **kwargs):
        # Override the `__new__` method to control instance creation.
        if cls.__instance is None:
            # If no instance exists, create a new one.
            cls.__instance = super().__new__(cls)
            # Call the parent class's `__new__` method to create an object.
            print("Connected to super class instance")
            return cls.__instance
            # Return the newly created instance.
        else:
            # If an instance already exists, return the same instance.
            print('There\'s already a Connection has been established')
            return cls.__instance  # Return the existing instance.

    def __init__(self):
        if not hasattr(self, '_initialized'):
            # The constructor is called every time the class is instantiated.
            print("Connected to the internet!")
            self._initialized = True
if __name__ == '__main__':

    # Create the first instance of the `Connection` class.
    conn1 = Connection()
    # Output:
    # "Connected to super class instance"
    # "Connected to the internet!"

    # Attempt to create another instance of the `Connection` class.
    conn2 = Connection()
    # Output:
    # "There's already a Connection has been established"
    # "Connected to the internet!"

    # Compare the two instances to confirm if they are the same.
    print(conn2 == conn1)  # Output: True