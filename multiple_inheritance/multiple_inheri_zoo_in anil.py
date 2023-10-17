class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Abstract method, to be overridden by subclasses

class Enclosure:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

class Aviary(Enclosure):
    def __init__(self, name, size, height):
        super().__init__(name, size)
        self.height = height

class Aquarium(Enclosure):
    def __init__(self, name, size, water_type):
        super().__init__(name, size)
        self.water_type = water_type

# Example usage
simba = Lion("Simba", "African Lion")
dumbo = Elephant("Dumbo", "African Elephant")
aviary1 = Aviary("Aviary 1", 100, 10)
aquarium1 = Aquarium("Aquarium 1", 200, "Saltwater")

print(f"{simba.name} the {simba.species} says: {simba.make_sound()}")
print(f"{dumbo.name} the {dumbo.species} says: {dumbo.make_sound()}")
print(f"{aviary1.name} has a height of {aviary1.height} meters.")
print(f"{aquarium1.name} contains {aquarium1.water_type} water.")
