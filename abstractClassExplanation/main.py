from abc import ABC, abstractmethod


# abc is a buitlin module, we have to import ABC and abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def feed(self):
        pass


class Lion(Animal):
    def feed(self):
        print(f"Feeding {self.name} with raw meat!")


class Panda(Animal):
    def feed(self):
        print(f"Feeding {self.name} with some tasty bamboo!")


class Snake(Animal):
    def feed(self):
        print(f"Feeding {self.name} with mice!")


zoo = [Lion("leo"), Panda("po"), Snake("sam")]

for animal in zoo:
    animal.feed()
