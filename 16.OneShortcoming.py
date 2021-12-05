# But let's say, For a particular item, i need to change the pay_rate.
# So the natural instinct is to overwrite the pay_rate at the instance level.
# If I do that, then according to the previous file, the pay_rate still 
# doesn't change because in the apply_discount() method, price was overwritten
# using class level pay_rate (Item_pay_rate). So no matter what i give at the
# instance level, it takes the class level value. 

# to remedy that, if I overwrite the price using instance level pay_rate
# i.e. self.pay_rate, then a particular item like laptop(an instance) will
# take last value it gets which is overwritten instance pay_rate which user 
# provides. 

class Item:
    # this is a class level variable here. This can be accessed directly through class.
    # convention is to write them before defining constructor.
    pay_rate = 0.8 # after 20% discount 
  
    def __init__(self, name: str, price: float, quantity=1):     
        # running validations
        assert price >= 0, f"Price is {price}, it can not be negative"
        assert quantity > 0, f"Quantity is {quantity}, it can not be zero or negative"

        # assigning to self object.
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity;

    # applying class attribute to overwrite the old price
    def apply_discount(self):
        # even though I am in the class defining the method 
        # using a class variable. Still I can't directly 
        # access that like below.

        # self.price = self.price * pay_rate       
        

        # One option is to access this as a class variable.
        # but this will not be flexible enough in case instance 
        # wants to change that, it won't change.

        # self.price = self.price * Item.pay_rate


        # this will solve the problem.
        # this is the best practice. self.pay_rate
        # that way if instance has the last value at the class level
        # it will use that. Else, it will be overwritten by instance 
        # level value.
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5) 
#print(item1.calculate_total_price())
item1.apply_discount()
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000)
item2.pay_rate = 0.7
item2.apply_discount() 
print(item2.calculate_total_price())