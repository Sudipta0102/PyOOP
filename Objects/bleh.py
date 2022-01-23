import operator

a = 2
b = 4

# as of now, I know 4 straight forward ways to add two numbers.
print(a + b)
print(a.__add__(b))
print(operator.add(a, b))
print(operator.iadd(a, b))


class Kettle:
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False


amar = Kettle("Amar", 10)
tomar = Kettle("Tomar", 2)

# 1 way
Kettle.switch_on(amar)

# 2nd way
tomar.switch_on()


