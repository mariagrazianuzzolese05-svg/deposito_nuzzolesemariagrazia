#abc
from abc import ABC, abstractmethod
class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass
class Cane(Animale):
    def muovi(self):
        return super().muovi()
class Pesce(Animale):
    def muovi(self):
        return super().muovi()