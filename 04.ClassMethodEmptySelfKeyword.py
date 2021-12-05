class Item:
    # when you create a function inside a class, then that's called method.
    # In java, everything is method, But in python, both function and method
    # exists. 
    def calculate_total_price(self):
        # the 'self' arguument means, python passes object itself as the 
        # first argument. An error occurs if not given.
        pass


item1 = Item()

item1.name = "Phone"
item1.price = 100
item1.quantity = 5 

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3 