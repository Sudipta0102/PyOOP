from Item import Item

class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity=1, has_light=False):
        super().__init__(name, price, quantity=quantity)
        self.has_light = has_light    