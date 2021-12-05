class Item:
    def __init__(self, name, price, quantity=1): 
        #print(f"An instance created with:\n 1. Name: {name}\n 2. Price: {price}\n 3. Quantity = {quantity}\n")   
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("phone", 100, 5)
print(item1.name)
print(item1.price)
print(item1.quantity)
# even after you create a constructor with default values and 
# create an instance out of it, you can have additional params 
# to that instance if you like. Like Below:
item1.has_CreditCard = False 

item2 = Item("laptop", 1000)
print(item2.name)
print(item2.price)
print(item2.quantity)