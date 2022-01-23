class Kettle:

    power_source = "electricity"

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

print(amar.__dict__)
print(tomar.__dict__)

print(amar.power_source)
print(Kettle.power_source)

amar.power_source = "atomic"
print(amar.power_source)
print(Kettle.power_source)

print(Kettle.__dict__)