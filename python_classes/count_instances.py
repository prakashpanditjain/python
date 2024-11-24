class instancetracker():
    # Class-level variable to track the number of instances created
    instance_count = 0

    def __init__(self):
        # Increment the instance count every time an object of this class is created
        instancetracker.instance_count += 1

    @classmethod
    def count_instance(cls):
        # Class method to get the current count of instances created
        return cls.instance_count


# Creating instances of the class. Each instantiation increments the instance_count.
obj1 = instancetracker()
obj2 = instancetracker()
obj3 = instancetracker()
obj3 = instancetracker()  # Reassigning obj3, the previous instance is garbage collected
obj3 = instancetracker()  # A new instance is created and assigned to obj3
obj3 = instancetracker()  # Another new instance is created and assigned to obj3

# Printing the total count of instances created using the class method
print("count of instances created", instancetracker.count_instance())
