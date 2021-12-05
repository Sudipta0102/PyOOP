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

    # applying class attribute to overwrite the old price
    def apply_discount(self):
        # even though I am in the class defining the method 
        # using a class variable. Still I can't directly 
        # access that like below.
        # self.price = self.price * pay_rate       
        
        # One option is to access this as a class variable.
        self.price = self.price * Item.pay_rate


item1 = Item("Phone", 100, 5) 
#print(item1.calculate_total_price())
item1.apply_discount()
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000)
item2.pay_rate = 0.7
item2.apply_discount() 
print(item2.calculate_total_price()) # it still doesn't change.
# there is shortcoming. Refer next file.

