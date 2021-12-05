# 1. class attribute can be accessed from the class level primarily.
# 2. You need those mainly because there will always be some attributes
# which is common to the class. In this case common to all the items.
# 3. But this can also be accessed from the instance level.
# 
# Note: Just like static vaeriable in java I suppose


class Item:
    # this is a class level variable here. This can be accessed directly through class.
    # convention is to write them before defining constructor.
    pay_rate = 0.8 # after 20% discount  
    def __init__(self, name: str, price: float, quantity=1):     
        assert price >= 0, f"Price is {price}, it can not be negative"
        assert quantity > 0, f"Quantity is {quantity}, it can not be zero or negative"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity;


item1 = Item("Phone", 100, 5) 
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000) 
print(item2.calculate_total_price())

# here I am access pay_rate via class itself
print("Pay Rate via class:",  Item.pay_rate)

# but you can also access them via instances
print("Pay Rate via instance:", item1.pay_rate)
print("Pay Rate via instance:", item2.pay_rate)