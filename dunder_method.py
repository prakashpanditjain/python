class employee():
    increment_value = 7 / 100

    def __init__(self, name, sname, salary):
        # self._id = uuid4
        self.name = name
        self.sname = sname
        self.salary = salary

    def main(self):
        print(self.name, self.sname, "has salary", self.salary)

    def __str__(self):
        return self.name

    def same(self):
        return self.sname

    def __int__(self):
        return self.salary

    def increase(self):

        if self.increment_value < 1:
            self.salary = int(self.salary * self.increment_value) + self.salary
        else:
            self.salary = int(self.salary * self.increment_value)

    @classmethod
    def increment(cls, amount):
        cls.increment_value = amount


if __name__ == '__main__':
    # obj1 = fruit('prakash', 'pandit', 500000)
    # obj1.main()
    # print(obj1)
    # print(int(obj1))

    # Object creation of two employees
    prakash = employee('praksh', 'pandit', 200_000)
    varun = employee('varun', 'samsung', 500_000)

    """ check salary of prakash increment the increment_value by 3 
    from giving the variable from outside of the class
    though we have defined the variable inside tha class"""

    print(prakash.salary)
    # (prakash.increase())
    employee.increment(3)

    # increase the salary by passing it into increase method
    prakash.increase()

    #check the salary after increment
    print(prakash.salary)

    # dunder method printing the first name if passed in the __str__ method
    rana = employee('VeerRanaRanveer', "chittore", 238942340)
    print(str(rana))
