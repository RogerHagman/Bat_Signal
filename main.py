"""Bat Signal The Battery Reader"""

from __future__ import annotations
from abc import ABC, abstractmethod
from electronic_device import ElectronicDevice
from electronic_device import SmartPhone
from electronic_device import Laptop
from electronic_device import SmartWatch

VERSION = 0.02

def display_battery_life(device:ElectronicDevice):
    print(device.get_battery_life())

def main():

    devices = {
    "smartphone": SmartPhone(),
    "laptop": Laptop(),
    "smartwatch": SmartWatch()
    }
    
    for device in devices:
        display_battery_life(devices.get(device))

if __name__ == '__main__':
    main()