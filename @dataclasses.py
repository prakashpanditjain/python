from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    weight: int
    height: float
    job: str
    location: str
    city: str

    def bmi(self):
        # print(math.pow(self.height, 2))
        print(self.weight / (self.height * self.height))


Packy: Person = Person('Prakash', 29, 59, 4, 'SDE', 'Pune', 'Pune')
Packy.bmi()
