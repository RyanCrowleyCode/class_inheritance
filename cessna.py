from vehicle import Vehicle

class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        pass

    def drive(self):
        print(f'The {self.main_color} Cessna flies past. BBBBRRRROOOOOOWWWWWMMMM!!!')