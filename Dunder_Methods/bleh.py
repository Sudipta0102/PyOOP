import operator

a = 2
b = 4

print(a + b)
print(a.__add__(b))
print(operator.add(a, b))
print(operator.iadd(a, b))

