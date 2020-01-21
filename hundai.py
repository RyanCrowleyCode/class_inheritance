from vehicle import Vehicle

class Hundai(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        pass

    def drive(self):
        print(f'The {self.main_color} Hundai drives past. VROOOOM!!')
