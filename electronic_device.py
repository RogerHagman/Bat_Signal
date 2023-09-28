"""Abstract class Electronic Device"""

from __future__ import annotations
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    
    def __init__(self, max_battery_life: int, battery_life: int = None):
        self._max_battery_life = battery_life
        self._battery_life = battery_life if battery_life is not None \
            else max_battery_life

    @property
    def max_battery_life(self):
        return self._max_battery_life

    @max_battery_life.setter
    def battery_life(self, value):
        if not isinstance(value, int):
            raise ValueError("Max Battery life must be an integer")
        if value < 0:
            raise ValueError("Max Battery life cannot be negative")
        self._battery_life = value

    @property
    def battery_life(self):
        return self._battery_life

    @battery_life.setter
    def battery_life(self, value):
        if not isinstance(value, int):
            raise ValueError("Battery life must be an integer")
        if value < 0:
            raise ValueError("Battery life cannot be negative")
        self._battery_life = value

    @abstractmethod
    def get_battery_life(self):
        pass

class SmartPhone(ElectronicDevice):

    def __init__(self):
        super().__init__(max_battery_life = 10, battery_life = 10)

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."
    
class Laptop(ElectronicDevice):

    def __init__(self):
        super().__init__(max_battery_life = 5, battery_life = 5)

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."
    
class SmartWatch(ElectronicDevice):

    def __init__(self):
        super().__init__(max_battery_life = 24, battery_life = 24)

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."

    
