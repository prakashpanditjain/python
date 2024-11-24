class instancetracker():
    instance_count = 0

    def __init__(self):
        instancetracker.instance_count += 1

    def count_instance(cls):
        # get the count of instance created
        return cls.instance_count



obj1  = instancetracker()
obj2  = instancetracker()
obj3  = instancetracker()
obj3  = instancetracker()
obj3  = instancetracker()
obj3  = instancetracker()


countofinstance = instancetracker.instance_count
print(countofinstance)