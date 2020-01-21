from vehicle import Vehicle

class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        pass