# 1. __repr__ magic method is used for object representation.
# 2. I think it's mostly euivalent to overring toString() method in java.
# 3. It's a good pratice because of reusability aspect.
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

    # this method is being overriden I suppose. I dunno. I am not sure.
    # this is returning a formatted string which has object representation. 
    def __repr__(self) :
        return f"('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5) 
#print(item1.calculate_total_price())
item1.apply_discount()
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000)
item2.pay_rate = 0.7
item2.apply_discount() 
print(item2.calculate_total_price())

# so this still uses the list to list all the objects and __repr__ method
# for formatting.
print(Item.all)