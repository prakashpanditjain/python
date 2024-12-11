class MobilePhone():
    def __init__(self, model, type, sim) -> None:
        self.model = model
        self.type = type
        self.sim = sim
        self.switched_on: bool = False


    def switch_on(self) -> None:
        if self.switched_on:
            print(f"Mobile : {self.model} is already switched on")

        else:
            self.switched_on = True
            print(f'{self.model} Mobile has now switched on')

    def switch_off(self) -> None:
        if self.switched_on:
            self.switched_on = False
            print(f"{self.model} has now switched off")
        else:
            print(f"{self.model} is already switched off")

    def run_application(self, app_name) -> None:
        if self.switched_on:
            print(f"{app_name} application is running")
        else:
            print(f"A mystical force whispers: 'switch on your mobile phone' ")

    def __str__(self):
        return f"you have a {self.model} Mobile which is {self.type} and has {self.sim} SIM"

    def __add__(self, other):
        return f'{self.model} and {other.model}'

    def __mul__(self, other):
        return f"{self.sim} * {other.sim}"


samsung: MobilePhone = MobilePhone("Samsung", "smartPhone", "Dual")
Nokia: MobilePhone = MobilePhone("Nokia", "keypad", "Single")

print(samsung + Nokia)
print(samsung * Nokia)
print(samsung)

