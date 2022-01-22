# 1. abstraction in this context generally means hiding unnecessary details from the user.
# 2. And By user, I mean people who are going to use this class to implement something else.
# 3. In this case, 
#    a. let's say I want to write a method that sends mail whenever a new object
# of Item is created or modified. (send_email())
#    b. So i need to have a bunch of helper method like create_smtp_connection(), 
# create_body() etc.
#    c. This helper functions are useless to the users who just like send mail and be done 
# with it. So making them abstract would do the trick.
# 
#      
#    

class Item:

    pay_rate = 0.8 
    all = []
    def __init__(self, name:str, price:float, quantity=1):
        
        assert price>=1, f"{price} is too low of a price"
        assert quantity>=1, f"{quantity} is too low of a quantity"

        self.__name = name
        self.__price = price
        self.__quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name    

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @price.setter
    def setNewPrice(self, newPrice):
        self.__price = newPrice

    @quantity.setter
    def setNewQuantity(self, newQuantity):
        self.__quantity = newQuantity        

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def calculate_total_price(self):
        return self.__price * self.__quantity                

    def apply_increment(self, incrementRate):
        self.__price = self.__price * incrementRate

    # Now here abstraction comes into picture
    # making these 3 heper methods private to achieve abstraction
    def __create_smtp_con(self, serverInfo):
        pass

    def __create_mail_body(self):
        pass

    def __send(self):
        pass

    def send_email(self):
        self.__create_smtp_con()
        self.__create_mail_body()
        self.__send()

    def __repr__(self):
        return f"('{self.__name}', {self.__price}, {self.__quantity})"

        

item1 = Item("item1", 100, 5)
item2 = Item("item1", 1000, 2)
print(Item.all)