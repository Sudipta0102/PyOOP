# 1. static methods use @staticmethod decorator
# 2. can't modify object instance state
# 3. can't modify class state 
# 4. takes no mandatory arguments.
# 5. This should be used when the required functionaty has a relationship 
# with the class but it's not unique for each instances.
# 6. These can be called from class level or instance level.
#
#
# In this context, we are going to determine that any number received as arguments 
# or any number is not integer or not.
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
    
    # I don't understand this method. Need to debug.
    # this method is not working.
    @staticmethod
    def is_integer(num=0):
        if isinstance(num, float):
            return Item.is_integer() # here is the error. It might have worked with 
            # older version. Here it needs an argument. Will need to get back to it.
        elif isinstance(num, int):
            return True
        else:
            return False    

    def __repr__(self) :
        return f"('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
# the whole object list
print(Item.all)
# the first element out of the list, item1 holding that instance

print(Item.is_integer(7.5))