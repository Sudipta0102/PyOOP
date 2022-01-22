class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # lets say my problem statement is: I want these vector to add, subtract.
    # then, operator overloading comes into picture:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return str((self.x, self.y))


v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
v4 = v1 - v2

print(v3)
print(v4)
