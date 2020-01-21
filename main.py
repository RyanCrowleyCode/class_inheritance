from cessna import Cessna
from motorcycle import Zero
from ram import Ram
from tesla import Tesla
from hundai import Hundai

# Practice: Custom Colors and Sounds
# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.

# Create an instance of each vehicle.
fxs = Zero()
modelS = Tesla()
mx410 = Cessna()
bubba = Ram()
ryanmobile = Hundai()

# Define a different value for each vehicle's properties.
fxs.main_color = "yellow"
fxs.maximum_occupancy = 2

modelS.main_color = "silver"
modelS.maximum_occupancy = 5

mx410.main_color = "white"
mx410.maximum_occupancy = 4

bubba.main_color = "red"
bubba.maximum_occupancy = 5

ryanmobile.main_color = "blue"
ryanmobile.maximum_occupancy = 5

# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").

vehicles = [fxs, modelS, mx410, bubba, ryanmobile]

for vehicle in vehicles:
    vehicle.drive()
    print()

# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.

