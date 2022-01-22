# assert keyword

class Item:
    # here I set name and price to str and float respectively. and quantity's
    # default value is 0 so, it's already an int.
    # 
    #   
    def __init__(self, name: str, price: float, quantity=1):
        # 1. validaing using assert keyword. 
        # 2. Also you can have a comme separated string messege or
        # formatted string in this case. 
        assert price >= 0, f"Price is {price}, it can not be negative"
        assert quantity > 0, f"Quantity is {quantity}, it can not be zero or negative"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity;


item1 = Item("Phone", -100, 0) 
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000) 
print(item2.calculate_total_price())