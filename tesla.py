from vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        pass

    def drive(self):
        print(f'The {self.main_color} Tesla drives past. ZEEEEEOOOWW!!')