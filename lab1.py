"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and manipulate Car objects in Python to understand 
  basic concepts of Object-Oriented Programming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.is_engine_on = False
        self.odometer = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"The engine of the {self.color} {self.brand} is now on.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"The engine of the {self.color} {self.brand} is now off.")
        
    def drive(self, distance):
        if (self.is_engine_on):
            print(f"The {self.brand} has driven {distance}KM")
            self.odometer += distance
        else:
            print(f"{self.brand} Cannot Drive, engine is not on")

# Add another property to the Car class called "odometer".
# This property should be initialised to 0.
# Create two Car objects. One should be a red Toyota and the other a blue Ford.

Toyota = Car("Red", "Toyota")
Miata = Car("Blue", "Mazda")


# Start the engine of the red Toyota.
Toyota.start_engine()


# Create a method called "drive" that takes a distance as a parameter.
# The car can only be driven if the engine is on.

# Attempt to drive both cars 100Km.

Toyota.drive(100)
Miata.drive(100)

# Print the brand, odometer and colour of both cars.
print()
print(f"The Car is a {Toyota.brand}, it is {Toyota.color}")
print(f"The Car is a {Miata.brand}, it is {Miata.color}")
