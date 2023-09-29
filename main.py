"""Bat Signal The Battery Reader.

This module provides a graphical representation of the battery status of 
various electronic devices.
"""

from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from electronic_device import ElectronicDevice
from electronic_device import SmartPhone
from electronic_device import Laptop
from electronic_device import SmartWatch

VERSION = 0.04


def display_battery_life(device:ElectronicDevice):
    """Display the current battery life for the given device."""
    print(device.get_battery_life())

class BatteryWidget(ttk.Frame):
    """A widget responsible for graphically represent and manipulate 
    the battery status of a given device."""

    def __init__(self, parent, device, **kwargs):
        """Initializes a widget for a given device."""
        super().__init__(parent, **kwargs)
        self.device = device

        self.grid(sticky=(tk.W + tk.E + tk.N + tk.S))

        self.battery_label = ttk.Label(self, 
                                       text=self.device.get_battery_life())
        self.battery_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.canvas = tk.Canvas(self, width=100, height=30, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=3, pady=10)

        self.increase_button = ttk.Button(self, text="+1hr", 
                                          command=self.increase_battery)
        self.increase_button.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.decrease_button = ttk.Button(self, text="-1hr", 
                                          command=self.decrease_battery)
        self.decrease_button.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.charge_button = ttk.Button(self, text="Super Charge",
                                        command=self.charge_battery)
        self.charge_button.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.update_battery_graphics()

    def increase_battery(self):
        """Increase the battery life of the device by one hour."""
        self.device.battery_life = min(self.device.battery_life + 1,
                                       self.device.max_battery_life)
        self.update_display()

    def decrease_battery(self):
        """Decrease the battery life of the device by one hour."""
        self.device.battery_life = max(self.device.battery_life - 1, 0)
        self.update_display()

    def charge_battery(self):
        """Instantly Supercharges the device's battery, bringing 
        the battery life up to the device's maximum."""
        self.device.battery_life = self.device.max_battery_life
        self.update_display()

    def update_display(self):
        """Updates the displayed batterys status."""
        self.battery_label["text"] = self.device.get_battery_life()
        self.update_battery_graphics()

    def update_battery_graphics(self):
        """Updates graphical representation of a battery's charge 
        level."""
        self.canvas.delete("all")
        fill_percent = self.device.battery_life / self.device.max_battery_life
        fill_width = int(fill_percent * 100)
        if fill_percent == 0:
            # In the case of the depleated battery we need to override 
            # the fill_width calculation in order to fill the entire 
            # battery life rectangle in with black color.
            self.canvas.create_rectangle(0, 0, 100, 30, fill='black')
        elif 0 < fill_percent <= 0.20:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='red')
        elif .20 < fill_percent < 0.70:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='yellow')
        else:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='green')

def main():
    """Initialized the devices and runs the main application."""
    root = tk.Tk()
    root.geometry("250x400")
    root.title("Bat Signal: The Battery Reader")

    smartphone = SmartPhone()
    laptop = Laptop()
    smartwatch = SmartWatch()

    devices = [smartphone, laptop, smartwatch]
    for idx, device in enumerate(devices):
        widget = BatteryWidget(root, device)
        widget.grid(row=idx, pady=10)
        widget.update_battery_graphics()
    root.mainloop()

if __name__ == "__main__":
    main()