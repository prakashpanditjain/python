class Transactions():
    """A class to represent transactions."""
    def __init__(self):
        self.__repr__()
        self.__module__ = "class_module"
        self.__str__()
        # self.__dir__()

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"Instance of {self.__class__.__name__}() class"

    def __dir__(self):
        """Return a list of attributes and methods of the class."""
        return ["__repr__", "__str__", "__dir__"] + list(super().__dir__())


if __name__ == "__main__":
    # This block is for testing purposes only
    transactions = Transactions()
    print(transactions)

