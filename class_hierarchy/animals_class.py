class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f"This is a {self.species} named {self.name}"

class Mammal(Animal):
    def __init__(self, name, species, has_milk=False):
        super().__init__(name, species)
        self.has_milk = has_milk

    def describe(self):
        base_description = super().describe()
        return f"{base_description}. It is a mammal{' that can nurse its young' if self.has_milk else ''}"

class Bird(Animal):
    def __init__(self, name, species, can_fly=False):
        super().__init__(name, species)
        self.can_fly = can_fly

    def describe(self):
        base_description = super().describe()
        return f"{base_description}. It is a bird{' that can fly' if self.can_fly else ''}"

class Reptile(Animal):
    def __init__(self, name, species, cold_blooded=True):
        super().__init__(name, species)
        self.cold_blooded = cold_blooded

    def describe(self):
        base_description = super().describe()
        return f"{base_description}. It is a reptile{' that is cold-blooded' if self.cold_blooded else ''}"

# Usage examples:

mammal1 = Mammal("Lion", "African Lion", True)
print(mammal1.describe())

bird1 = Bird("Eagle", "Bald Eagle", True)
print(bird1.describe())

reptile1 = Reptile("Snake", "King Cobra")
print(reptile1.describe())


