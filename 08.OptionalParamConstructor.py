class Item:
    # now here, this way, quantity becomes the optional parameter with default value 1  
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

item2 = Item("laptop", 1000)
print(item2.name)
print(item2.price)
print(item2.quantity) # this will print 1 as default because no value was mentioned 
# in the created instance. 