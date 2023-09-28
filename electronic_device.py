"""Abstract class Electronic Device"""

from __future__ import annotations
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    
    @abstractmethod
    def get_battery_life(self, battery_life):
        pass

class SmartPhone(ElectronicDevice):

    def __init__(self):
        self._battery_life = 10

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."
    
class Laptop(ElectronicDevice):

    def __init__(self):
        self._battery_life = 5

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."
    
class SmartWatch(ElectronicDevice):

    def __init__(self):
        self._battery_life = 24

    def get_battery_life(self, battery_life = None):
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} battery life: {self._battery_life} hours."

    
