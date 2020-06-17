"""
series = ["Ходячие мертвецы",
		  "Красавцы",
		  "Клан Сопрано",
		  "Дневники вампира"
		  ]
for show, i in enumerate(series, 1):
	print(show, ")", i)


for i in range(25, 51):
	print(i, end = " ")
"""




"""
list_numbers = [1, 4, 6, 12, 24, 43, 31, 18, 53]
while True:
	number = input("Угадаете число? (X для выхода): ")
	if number == "X":
		break

	try:
		number = int(number)
	except ValueError:
		print("Неправильное значение.")

	if number in list_numbers:
		print("Вы угадали!")
		print()
	else:
		print("Можете попытаться ещё раз))")
		print()
"""




"""
from math import pi
from random import randint

print("Beginning...")
print()


class Apple():
	def __init__(self, we, co, ra):
		self.weight = we
		self.color = co
		self.radius = ra
		self.mold = 0
		print("Done!")

	def volume(self):
		return round((4/3 * pi * self.radius ** 3), 2)

	def rot(self, temp, days):
		self.mold = days * temp

	def change_tech_param(self, co):
		self.color = co

apple = Apple(5, "green", 2.5)
print(apple.volume())
apple.rot(25, 5)
print(apple.mold)
apple.change_tech_param("red")
print(apple.color)
print()


class TriangularPrism():
	def __init__(self, w, l, h):
		self.bh = w
		self.ab = l
		self.h1h = h
		print("Done!")

	def volume(self):
		return (int((self.bh * self.ab) / 2) * self.h1h)

trian_prism = TriangularPrism(6, 8, 15)
print(trian_prism.volume())
print()


class Hexagon():
	def __init__(self, s1, s2, s3, s4, s5, s6):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
		self.s5 = s5
		self.s6 = s6

	def calculate_perimeter(self):
		try:
			return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
		except TypeError:
			print("Wrong type of object!")

sides = list()
for i in range(6):
	sides.append(randint(1, 20))

hexagon1 = Hexagon(*sides)
print(hexagon1.calculate_perimeter())

hexagon2 = Hexagon(3, 5, 7, 8, 11, "error")
print(hexagon2.calculate_perimeter())
print()
print("Tasks are perfomed.")
"""


"""
class Shape():
	def what_am_i(self):
		print("I'm a shape.")


class Square(Shape):
	def __init__(self, a):
		self.a = a
		print("Done.")

	def change_size(self, a):
		self.a = a
		print("changed.")

	def calculate_perimeter(self):
		print(self.a * 4)


class Rectangle(Shape):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		print("Done.")

	def calculate_perimeter(self):
		print(self.a * self.b)

square = Square(5)
rectangle = Rectangle(3, 7)
square.change_size(8)
shapes = [square,
		  rectangle]
for i in shapes:
	i.calculate_perimeter()
	i.what_am_i()


class Horse():
	def __init__(self,
				 name,
				 owner):
		self.name = name
		self.owner = owner

class Rider():
	def __init__(self, name):
		self.name = name

rider = Rider("Kurt")
horse = Horse("Babyleh",
			  rider)
print(horse.owner.name)
"""



