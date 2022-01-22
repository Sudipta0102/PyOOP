from Item import Item
from Keyboard import Keyboard

class Laptop(Keyboard):
    def __init__(self, name: str, price: float, quantity=1, has_light=False):
        super().__init__(name, price, quantity=quantity, has_light=has_light)
