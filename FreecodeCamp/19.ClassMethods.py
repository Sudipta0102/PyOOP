# 1. this uses @classmethod decorator.
# 2. can modify class state.
# 3. can't modify object instance state.
# 4. takes the class(cls) as the mandatory first argument
# 5. This should be used when the required functionality has a relationship
# with the class. But usually these are used to manipulate different structures 
# of data  to instantiate objects. Like from Json file or yaml file or csv file
# in this case.
#  6. These can be called from class level or instance level.   
#  
#
# In this context, we are going to use class method to read a
# csv file consists of inputs with which objects can be made.
# (a bunch of name, price and quantity) 

import csv

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

    # this class method is responsible for creating instances out of 
    # a csv.
    @classmethod
    def instantiate_from_csv(cls):
        with open('input.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self) :
        return f"('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
# the whole object list
print(Item.all)
# the first element out of the list, item1 holding that instance
item1=Item.all[0]
# the attribute of list of the 1st instance
print(item1.__dict__)
# individual attributes of the of the created instance
print(item1.name)
print(item1.price)
print(item1.quantity)