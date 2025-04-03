#polymorphism - comes from the greek word "poly" meaning many and "morph" meaning form
# it is a programming concept that allows objects of different classes to be treated as objects of a common superclass
# 
# #1 method overriding
# 2. method overloading
# 3. operator overloading
# 4. duck typing
# 
#        1. method overriding

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
        def make_sound(self):
            return "Woof!"
        
class cat(Animal):
     def make_sound(self):
          return "Meow!"
     
          #2 method overloading
class mathOperations:
     def add(self, a, b,c=0):
          return a + b + c
op1 = mathOperations()
print(op1.add(2,4))
print(op1.add(2,4,6))

        #3 operator overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 - v2
print(v3)
print(v4)

        #4 duck typing
