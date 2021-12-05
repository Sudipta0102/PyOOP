# Note: At the end, the desired result could not be 
# achieved after making desired changes.   

class Item:
    def __init__(self, name, price, quantity=1): 
        #print(f"An instance created with:\n 1. Name: {name}\n 2. Price: {price}\n 3. Quantity = {quantity}\n")   
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# here in this class, the problem with constructor arguments 
# is their datatypes are not defined. So if i take the price 
# as string then calculate_total_price method will just concatenate 
# the price given as string instead of multiplying. Like below:
item1 = Item("phone", "100", 5)
print(item1.name)
print(item1.price)
print(item1.quantity)
item1.has_CreditCard = False 
print(item1.calculate_total_price()) # in this case redult is 100100100100100
print()

# to remedy this prolem we can set them as we want in the constructor arguments.
class Item1:
    # here I set name and price to str and float respectively. and quantity's
    # default value is 0 so, it's already an int  
    def __init__(self, name: str, price: float, quantity=0):

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity;

# but here, i still can pass price as String. it's neither converting 
# the value nor giving error. just printing the concatenation
# (100.02100.02100.02100.02100.02)
item = Item1("Phone", "100.02" , 5) 
print(item.calculate_total_price())