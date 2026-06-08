from tkinter import *

ABS_ZERO_FAFRENHEIT = -459.67
ABS_ZERO_CELSIUS = -273.15

class TemperatureCoverter:

    def __init__(self, root):
        self.root = root
        root.title("Temperature Converter")
        root.geometry("400x180")

