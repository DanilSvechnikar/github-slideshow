from random import randint
import requests

"""
class Orange:
	legs = 4
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Создано!")

orl = Orange(10, "темный")
print(orl)
print(orl.weight)
orl.weight = 100
print(orl.weight)

orl1 = Orange(4, "светлый")
orl2 = Orange(14, "жёлтый")
print(orl1.color)
print(orl2.color)
print(orl2.legs)
"""

"""
class Orange():
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		self.mold = 0
		print("Создано!")

	def rot(self, days, temp):
		self.mold = days * temp

orange = Orange(6, "апельсин")
print(orange.mold)
orange.rot(10, 33)
print(orange.mold)
"""

"""
class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def area(self):
		return self.width * self.len

	def change_size(self, w, l):
		self.width = w
		self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
"""

"""
class Data:
	def __init__(self):
		self.nums = [1, 2, 3, 4, 5]

	def change_data(self, index, n):
		self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 50)
print(data_two.nums)
"""

"""
class PublicPrivateExample:
	def __init__(self):
		self.public = "safe"
		self._unsafe = "unsafe"

	def public_method(self):
		# can be used
		pass

	def _unsafe_method(self):
		# cannot be used
		pass
		self.public = "safe"
		self._unsafe = "danger"
"""

"""
class Shape():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print("{} by {}".format(self.width,
								self.len))

class Square(Shape):
	pass  # this means that there is nothing else to do

a_square = Square(20, 20)
a_square.print_size()
"""

"""
class Shape():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print("{} by {}".format(self.width,
								self.len))

class Square(Shape):
	def area(self):
		return self.width * self.len

	def print_size(self):
		print(f"Я {self.width} на {self.len}")

a_square = Shape(20, 25)
a_square.print_size()
print()

b_square = Square(15, 20)
print(b_square.area())
b_square.print_size()
"""

"""
class A:
	def method(self):
		print("A - method")

class B(A):
	def another_method(self):
		print("B - method")

class C(B):
	def third_method(self):
		print("C - method")

c = C()
c.method()
c.another_method()
c.third_method()
"""

"""
class A:
	def spam(self):
		print(1)

class B(A):
	def spam(self):
		print(2)
		super().spam()

B().spam()
"""

"""
class Dog():
	def __init__(self,
				 name,
				 breed,
				 owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

mick = Person("Mick Jugger", 17)
stan = Dog("Stanly",
		   "Bulldog",
		   mick)
print(stan.owner.name)
print(stan.owner.age)
"""

"""
class Vector2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return Vector2D(self.x * other.x, self.y * other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
third = Vector2D(2, 11)
result = first + second
print(result.y)
result = first + second + third
print(result.y)
result = first * second * third
print(result.y)
"""

"""
class SpecialString:
	def __init__(self, cont):
		self.cont = cont

	def __truediv__(self, other):
		line = "=" * len(other.cont)
		return "\n".join([self.cont, line, other.cont])

	def __gt__(self, other):
		for index in range(len(other.cont) + 1):
			result = other.cont[:index] + ">" + self.cont
			result += ">" + other.cont[index:]
			print(result)

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
"""

"""
class VagueList:
	def __init__(self, cont):
		self.cont = cont

	def __getitem__(self, index):
		return self.cont[index + randint(-1, 1)]

	def __len__(self):
		return randint(0, len(self.cont) * 2)

vague_list = VagueList(["A", "B", "C", "D" ,"E",])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
"""

"""
class Queue:
	def __init__(self, contents):
		self._hiddenlist = list(contents)

	def push(self, value):
		self._hiddenlist.insert(0, value)

	def pop(self):
		return self._hiddenlist.pop(-1)

	def __repr__(self):
		return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


class Spam:
	__egg =7
	def print_egg(self):
		print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)
"""

"""
class Rectangle:
	def __init__(self, width, heigth):
		self.width = width
		self.heigth = heigth


	def calculate_area(self):
		return self.width * self.heigth

	@classmethod
	def new_square(cls, side_length):
		return cls(side_length, side_length)

square = Rectangle.new_square(6)
print(square.calculate_area())
print(square.width, square.heigth)
"""

"""
class DecoratorTest(object):
    def __init__(self):
        pass

    def doubler(self, x):
        return x*2

    @classmethod
    def class_tripler(klass, x):
        return x*3
    
    @staticmethod
    def static_quad(x):
        return x*4

decor = DecoratorTest()
print(decor.doubler(5))
print(decor.class_tripler(3))
print(DecoratorTest.class_tripler(3))
print(DecoratorTest.static_quad(2))
print(decor.static_quad(3))
"""

"""
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@staticmethod
	def validate_topping(topping):
		if topping == "pineapple":
			raise ValueError("No pineapples!")
		else:
			return True

ingredients = ["cheese", "onions", "spam",]
if all(Pizza.validate_topping(i) for i in ingredients):
	pizza = Pizza(ingredients)
"""

"""
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@property
	def pineapple_allowed(self):
		return False

pizza = Pizza(["cheese", "tomato",])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
"""

"""
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False

	@property
	def pineapple_allowed(self):
		return self._pineapple_allowed

	@pineapple_allowed.setter
	def set_password(self, value):
		if value:
			password = input("Enter the password: ")
			if password == "Sw0rdf1sh!":
				self._pineapple_allowed = value
			else:
				raise ValueError("Alert!Intruder!")

	@set_password.getter
	def get_password(self):
		return self.set_password

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.set_password = True
print(pizza.pineapple_allowed)
print(pizza.get_password)
"""

"""
class Rectangle():
	recs = []

	def __init__(self, w, l):
		self.width = w
		self.length = l
		self.recs.append((self.width,
						  self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
print(Rectangle.recs)
"""

"""
class Person:
	def __init__(self):
		pass

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)
"""


class Square:
    squares = []

    def __init__(self, s):
        self.square_list = s
        self.squares.append(s)
        print(
            f"Square {self.square_list} on {self.square_list} on {self.square_list} on {self.square_list} is created.")


square = Square(29)
square1 = square
square2 = Square(15)


def comparison(one, two):
    if one is two:
        return True
    else:
        return False


print(comparison(square, square1))
print(comparison(square, square2))
print(comparison(square1, square2))
