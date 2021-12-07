# encapsulation 
# @Property decorator - Read only attribute
# @attribute.setter
# @attribute.getter

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        assert price>=1, f"Price {price} is too small"
        assert quantity>=0, f"Quantity {quantity} is less than expected"    

        self.__name = name 
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    # 1. With @property I can make this attribute read only.
    # 2. Now without a setter I can not change the value of this attribute.
    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        # 1. here what I can do is, I can write my own logic to restrict or enhance 
        # the capability of this attribute.
        # 2. Let's say, in this case, I can only reset the the value if the reset value
        # lenghth is less than 10 chars
        if len(newName)>10:
            raise Exception("Name too long!!")
        else:
            self.__name = newName    

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"('{self.name}, {self.price}, {self.quantity}')"        


item1 = Item("item1", 100, 20)
item2 = Item("item2", 100, 20)        
# 1. with the pre existing class, I am able to do this means, I can set any attribute of a
# particular instance outside the class directly.
#item1.name = 'newName'
# 2. what if I want to make this value read only. Only with the constructor One can set the
# value and that's it. Here comes @property
# 3. If anybody tries to overwrite that, they should come across an error.
# 4. This particular thing is called Encapsulation.
# 4. In the real world, we might need to that for any critical attributes.
print(Item.all)

item1.name = "BBBBBBB" # 1. here it gives error when i made it read only without the setter
                    # 2. changes the value after i write the setter.
#item1.__name = "BBBBB" # now here It doesn't give the error for some unknown reason
                       # but also it doesn't set the new value.(This is before writing 
                       # a setter)     

print(Item.all)