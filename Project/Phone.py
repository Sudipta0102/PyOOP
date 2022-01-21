from Item import Item

class Phone(Item):
    # you can add parameters to the child class.
    def __init__(self, name: str, price: float, quantity=1, isRefurbished=False):
        # super() function to access to parent level attributes/methods.
        super().__init__(name, price, quantity)
        self.isRefurbished = isRefurbished