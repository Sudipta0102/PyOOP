# 1. we define constructor by a magic method called __init__(self)
# 2. 'self' is also here for the same reason. (takes the first argument as the object
# itself).  

class Item:
    # 1. this is an empty coonstructor. 
    # 2. this is run implicitly when any class loads even if this is not here just
    # like java
    def __init__(self) -> None:
        pass

    def calculate_total_price(self, x, y):
        return x * y



item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5 
# Now with this class method we can calculate total price
print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 
print(item2.calculate_total_price(item2.price, item2.quantity))