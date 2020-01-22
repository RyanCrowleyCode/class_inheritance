class Vehicle:
    def __init__(self):
        self.main_color = ''
        self.maximum_occupancy = ''

    def drive(self):
        print("VROOOM!!")

    def turn(self, direction):
        print(f"The vehicle turns to the {direction}!")

    def stop(self):
        print("The vehicle stops safely.")