class Item:
    pay_rate = 0.8 # after 20% discount 
    # this list will list all the objects.    
    all = []
    def __init__(self, name: str, price: float, quantity=1):     
        # running validations
        assert price >= 0, f"Price is {price}, it can not be negative"
        assert quantity > 0, f"Quantity is {quantity}, it can not be zero or negative"

        # assigning to self object.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Appending the object to the list whenever a new one is being created.
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity;

    # applying class attribute to overwrite the old price
    def apply_discount(self):    
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5) 
#print(item1.calculate_total_price())
item1.apply_discount()
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000)
item2.pay_rate = 0.7
item2.apply_discount() 
print(item2.calculate_total_price())

print(Item.all)


for instance in Item.all:
    print(instance.name)