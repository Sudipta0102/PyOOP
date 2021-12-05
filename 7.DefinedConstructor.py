# 1. up until now, all the values are hardcoded for every instance like name, price etc
# for each instance like item1 and item2
# 2. Now there is a way to minimize that overhead. When creating the object itself, 
# we can pass on the required values for that instance. These are called constructor.
# 3. we define constructor by a magic method called __init__(self)
# 4. 'self' is also here for the same reason. (takes the first argument as the object
# itself).  

class Item:
    def __init__(self, name, price, quantity): 
        print(f"An instance created with:\n 1. Name: {name}\n 2. Price: {price}\n 3. Quantity = {quantity}\n")
        # helps assigning these attibutes to a particular instance dynamically
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("phone", 100, 5)
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5 
# Now with this class method we can calculate total price
#print(item1.calculate_total_price(item1.price, item1.quantity))
#print(item1.name)

item2 = Item("laptop", 1000, 3)
#item2.name = "Laptop"
#item2.price = 1000
#item2.quantity = 3 
#print(item2.calculate_total_price(item2.price, item2.quantity))
#print(item2.name)