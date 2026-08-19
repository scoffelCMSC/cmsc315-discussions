"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

# Made to represent the potential preset pathings I have planned out for a model railway system, 
# where we'll store route data for each engine to access during an automated run
from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ModelTrainTest:
    railway = "Passenger" # Class variable

    def __init__(self, engine: str, car_total: int, passenger_count: int, eta_time: float, rail_ready: bool): # Constructor
        self.engine = engine # Instance variable
        self.car_total = car_total # Instance variable
        self.passenger_count = passenger_count # Instance variable
        self.eta_time = eta_time # Instance variable
        self.is_needed = False
        self.rail_ready = rail_ready # Student extension for showing the train is ready to run


    def display(self): # Method to display information on the object
        print(f"Current Engine: {self.engine}")
        print(f"Total Cars: {self.car_total}")
        print(f"Total Passengers: {self.passenger_count}")
        print(f"Estimated Duration: {self.eta_time} minutes")
        print(f"Ready for Rail: {self.rail_ready}")

    def maintenance(self, is_needed: bool): # Student extension to flag the train as needing maintenance before use
        if is_needed:
            self.rail_ready = False
        else:
            self.rail_ready = True



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class DetourRoute(ModelTrainTest): # Child class that inherets from ModelTrainTest
    detour = "South Rail"

    def __init__(self, engine: str, car_total: int, passenger_count: int, eta_time: float, rail_ready: bool, eta_delay: float, detour_count: int):
        super().__init__(engine, car_total, eta_time, passenger_count, rail_ready) # Inherit variables from parent class
        self.eta_delay = eta_delay # Instance variable
        self.detour_count = detour_count # Instance variable
        self.alt_stops = []

    def add_stops(self, stops: str): # New method, adds new stops to alt_stops
        self.alt_stops.append(stops)

    def display(self): # display() override for the ModelTrainTest parent class
        super().display()
        print(f"Estimated Delay: {self.eta_delay} minutes")
        print(f"Number of Detours: {self.detour_count}")
        print(f"New stops: {', '.join(self.alt_stops)}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # First object using child class
    detour1 = DetourRoute("Santa Fe", 4, 60, 12.5, True, 4.5, 3)
    detour1.add_stops("Mines")
    detour1.add_stops("Mountain Town")
    detour1.add_stops("Underground Station")

    # Second child class object
    detour2 = DetourRoute("Santa Fe", 4, 60, 12.5, True, 4.5, 3)
    detour2.add_stops("Railyard")
    detour2.add_stops("Meadow Town")
    detour2.emergency_stop = True # Adding an attribute to one of the objects

    # Display object namespace information
    print("Detour 1 Instance Namespace: ", detour1.__dict__)
    print("Detour 2 Instance Namespace: ", detour2.__dict__)

    # Display class namespace information
    print("DetourRoute Class Namespace: ", DetourRoute.__dict__)

    print("\n=== Access class variable through Class ===\n")
    print(DetourRoute.detour)

    print("\n=== Access class variable through Object ===\n")
    print("Detour 1: ", detour1.detour)
    print("Detour 2: ", detour2.detour)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    base = DetourRoute("Santa Fe", 4, 60, 12.5, True, 4.5, 3)
    base.add_stops("Maintenance Station")

    # Creating the copies
    shallow_copy = copy(base)
    deep_copy = deepcopy(base)

    base.add_stops("Mountain Town") # Modifying original data

    # Display object in its original state, then the copies
    print(f"Original detours: {base.alt_stops}")
    print(f"Shallow copy: {shallow_copy.alt_stops}")
    print(f"Deep copy: {deep_copy.alt_stops}")

"""
Shallow copies: Creates a new list with the same original contents, but editing an instance from one list can change the contents of the other.
Deep copies: References its own copy when creating modifications. Modifying the original list will not affect the deep copy.
"""


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent object test
    test1 = ModelTrainTest("Santa Fe", 4, 60, 12.5, True)
    test1.display()

    # Child object test
    detour1 = DetourRoute("Santa Fe", 4, 60, 12.5, True, 4.5, 3)
    detour1.add_stops("Train Yard")
    detour1.maintenance(False)
    detour1.display()


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()