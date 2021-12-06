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

# that's how you inherit. You can pass the Parent as an argument of the child class. 
class Phone(Item):
    pass

# naturally you can do everything you did with Item class.
phone1 = Phone("PhoneName", 100, 2)
print(phone1.all)