
Assignment 1: Design Your Own Class – Superhero 

# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I'm {self.name}, my power is {self.power}, and I protect {self.city}!")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

# Create objects
flash = Superhero("SuperSpeed", "SuperThinking", "Metroville")
featherWitch = FlyingHero("SkyBlazer", "Wind Control", "Skytown", 600)

# Test methods
flash.introduce()
featherWitch.use_power()
print("---")
flash.introduce()
featherWitch.use_power()

