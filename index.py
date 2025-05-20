
# Assignment 1: Design Your Own Class! 🏗️
# Base class
class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # Encapsulated (protected)

    def show_identity(self):
        print(f"I am {self.name}, with power level {self._power_level}.")

    def use_power(self):
        print(f"{self.name} uses a generic power!")

# Subclass with polymorphic method
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the skies! 🦸‍♂️")

class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.name} lifts a building with ease! 💪")

# Create objects
hero1 = FlyingHero("SkyMan", 95)
hero2 = StrongHero("Bulk", 90)

# Demonstrate behavior
hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()

# Activity 2: Polymorphism Challenge! 🎭
# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves in its own way.")

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water. 🚤")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
