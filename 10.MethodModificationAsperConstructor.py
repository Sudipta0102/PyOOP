class Item:
    def __init__(self, name, price, quantity=1): 
        #print(f"An instance created with:\n 1. Name: {name}\n 2. Price: {price}\n 3. Quantity = {quantity}\n")   
        self.name = name
        self.price = price
        self.quantity = quantity

    # this is the intial method: 
    #def calculate_total_price(self, x, y):
    #    return x * y
    # 1. but now that we use constructor to initialize our value dynamically,
    # we can also take advantage of that when writing the method
    # by taking those parameters directly
    # 2. One thing to note: not taking any parameters explicitly in this case because, 
    # we can use values from the constructor. 
    def calculate_total_price(self):
        return self.price * self.quantity




item1 = Item("phone", 100, 5)
print(item1.name)
print(item1.price)
print(item1.quantity)
# even after you create a constructor with default values and 
# create an instance out of it, you can have additional params 
# to that instance if you like. Like Below:
item1.has_CreditCard = False 
print(item1.calculate_total_price())
print()

item2 = Item("laptop", 1000)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())