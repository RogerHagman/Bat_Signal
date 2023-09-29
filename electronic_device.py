"""Abstract class representing electronic devices."""

from __future__ import annotations
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    """An abstract base class representing an electronic device with a
    battery.
    
    Attributes:
        max_battery_life: The maximum life of the device's battery.
        battery_life: The current life of the device's battery.
    """
    def __init__(self, max_battery_life: int, battery_life: int = None):
        """Initialize an electronic device with the given battery life.

        Args:
            max_battery_life (int): Maximum battery life for the 
            device.
            battery_life (int, optional): Initial battery life for the
            device. Defaults to max_battery_life.
        """
        self._max_battery_life = battery_life
        self._battery_life = battery_life if battery_life is not None \
            else max_battery_life

    @property
    def max_battery_life(self) -> int:
        """Get the maximum battery life of the device.

        Returns:
            int: maximum battery life"""
        return self._max_battery_life

    @max_battery_life.setter
    def battery_life(self, value: int):
        """Set the maximum battery life of the device.

        Args:
            value (int): The maximum battery life to set.

        Raises:
            ValueError: If the value provided is not an integer or if 
                        it's in the negative.
        """
        if not isinstance(value, int):
            raise ValueError("Max Battery life must be an integer")
        if value < 0:
            raise ValueError("Max Battery life cannot be negative")
        self._battery_life = value

    @property
    def battery_life(self) -> int:
        """Get the current battery life of the device.

        Returns:
            int: current battery life"""
        return self._battery_life

    @battery_life.setter
    def battery_life(self, value: int):
        """Set the current battery life of the device.

        Args:
            value (int): The current battery life to set.

        Raises:
            ValueError: If the value provided is not an integer or if
                        it's in the negative.
        """
        if not isinstance(value, int):
            raise ValueError("Battery life must be an integer")
        if value < 0:
            raise ValueError("Battery life cannot be negative")
        self._battery_life = value

    @abstractmethod
    def get_battery_life(self) -> str:
        """Return a string representation of the device's current 
        battery life.

        This method should be overridden by all subclasses.

        Returns:
            str: A representation of the implemented device's current
                 battery life.
        """
        pass

class SmartPhone(ElectronicDevice):
    """A class representing a SmartPhone, a specific electronic device."""
    def __init__(self):
        """Initialize a SmartPhone with default battery life."""
        super().__init__(max_battery_life = 10, battery_life = 10)

    def get_battery_life(self, battery_life = None) -> str:
        """Return the SmartPhone's current battery life.

        Args:
            battery_life (int, optional): Battery life to set. 
            Defaults to None.

        Returns:
            str: A representation of the current battery life.
        """
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} " \
            f"battery life: {self._battery_life} hours."
    
class Laptop(ElectronicDevice):
    """A class representing a Laptop, a specific electronic device."""
    def __init__(self):
        """Initialize a SmartPhone with default battery life."""
        super().__init__(max_battery_life = 5, battery_life = 5)

    def get_battery_life(self, battery_life = None) -> str:
        """Return the Laptop's current battery life.

        Args:
            battery_life (int, optional): Battery life to set. 
            Defaults to None.

        Returns:
            str: A representation of the current battery life.
        """
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} "\
            f"battery life: {self._battery_life} hours."
    
class SmartWatch(ElectronicDevice):
    """A class representing a SmartWatch, a specific electronic device."""
    def __init__(self):
        """Initialize a SmartWatch with default battery life."""
        super().__init__(max_battery_life = 24, battery_life = 24)

    def get_battery_life(self, battery_life = None) -> str:
        """Return the SmartWatch's current battery life.

        Args:
            battery_life (int, optional): Battery life to set. 
            Defaults to None.

        Returns:
            str: A representation of the current battery life.
        """
        if battery_life is not None:
            self._battery_life = battery_life
        return f"{__class__.__name__} "\
            f"battery life: {self._battery_life} hours."