class Item:
    # when you create a function inside a class, then that's called method.
    # In java, everything is method, But in python, both function and method
    # exists. 
    def calculate_total_price(self, x, y):
        # the 'self' arguument means, python passes object itself as the 
        # first argument. An error occurs if not given.
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