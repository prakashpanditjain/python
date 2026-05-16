class temperature():
    def __init__(self, a, b, c,temp=0):
        self._temp = temp
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"temperature({self._temp}) C"

    def __repr__(self):
        return f"temperature({self._temp})"


t = temperature(2,3,5,22)
print()