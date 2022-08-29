# Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    model_name = "hayabusa"
    color = "white"

    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"the capacity of {self.model_name} is {capacity}"

    def fare(self):
        return self.capacity * 100


harry = Vehicle(234, 45, 40)


# Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass


# Exercise 3: Create a child class Bus that will inherit all of the variables and
# methods of the Vehicle class
# Create a Bus object that will inherit all of the variables and
# methods of the Vehicle class and display it.

# class Bus(Vehicle):
#     pass
#
#
# wheel = Bus(235, 46, 50)
# print(wheel.max_speed, wheel.mileage)
# print(wheel.model_name)

# Exercise4.  Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

# class Bus(Vehicle):
#     pass
#
#
# abhi = Bus(234, 35, 50)
# print(abhi.seating_capacity(45))

# Exercise 5: Define property that should have the same value for every class instance
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white

# class Car(Vehicle):
#     pass
#
#
# car = Car(235, 43, 50)
# print(car.color, car.model_name, car.mileage, car.max_speed)

# Exercise 6: Class Inheritance
# Given:-----
#
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle
# is seating capacity * 100. If Vehicle is Bus instance,
# we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note:----

# The bus seating capacity is 50. so the final fare amount should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount
#
#
# School_bus = Bus(235, 45, 40)
# print("Total school bus fare is ", School_bus.fare())

# Exercise 7: Determine which class a given Bus object belongs to (Check type of an object)

# class Bus(Vehicle):
#     pass
#
#
# abhi = Bus(234, 45, 50)
# print(type(abhi))

# Exercise 8: Determine if School_bus is also an instance of the Vehicle class

# class Bus(Vehicle):
#     pass
#
#
# abhi = Bus(234, 45, 50)
# print(isinstance(abhi, Vehicle))
# print(isinstance(abhi, Bus))


# NOTE:--------------------------------------------------------------------------
# WHICHEVER EXERCISE CODE YOU WANT TO RUN UNCOMMENT ONLY THAT EXERCISE'S BELOW
# CODE NOT ANY OTHER EXERCISE'S
# -------------------------------------------------------------------------------


