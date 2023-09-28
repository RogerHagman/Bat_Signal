"""Bat Signal The Battery Reader"""
from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from electronic_device import ElectronicDevice
from electronic_device import SmartPhone
from electronic_device import Laptop
from electronic_device import SmartWatch

VERSION = 0.03

def display_battery_life(device:ElectronicDevice):
    print(device.get_battery_life())

class BatteryWidget(ttk.Frame):
    def __init__(self, parent, device, **kwargs):
        super().__init__(parent, **kwargs)

        self.device = device
        self.grid(sticky=(tk.W + tk.E + tk.N + tk.S))

        self.battery_label = ttk.Label(self, text=self.device.get_battery_life())
        self.battery_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.canvas = tk.Canvas(self, width=100, height=30, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=3, pady=10)

        self.increase_button = ttk.Button(self, text="+1", 
                                          command=self.increase_battery)
        self.increase_button.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.decrease_button = ttk.Button(self, text="-1", 
                                          command=self.decrease_battery)
        self.decrease_button.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.charge_button = ttk.Button(self, text="Charge",
                                        command=self.charge_battery)
        self.charge_button.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.update_battery_graphics()

    def increase_battery(self):
        self.device.battery_life = min(self.device.battery_life + 1, self.device.max_battery_life)
        self.update_display()

    def decrease_battery(self):
        self.device.battery_life = max(self.device.battery_life - 1, 0)
        self.update_display()

    def charge_battery(self):
        self.device.battery_life = self.device.max_battery_life
        self.update_display()

    def update_display(self):
        self.battery_label["text"] = self.device.get_battery_life()
        self.update_battery_graphics()

    def update_battery_graphics(self):
        self.canvas.delete("all")
        fill_percent = self.device.battery_life / self.device.max_battery_life
        fill_width = int(fill_percent * 100)
        if 0 < fill_percent <= 0.20:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='red')
        elif .20 < fill_percent < 0.70:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='yellow')
        else:
            self.canvas.create_rectangle(0, 0, fill_width, 30, fill='green')

def main():
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