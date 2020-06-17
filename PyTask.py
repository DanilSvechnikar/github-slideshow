# високосный год или нет
"""
def is_year_leap(year):
	x = year % 2
	if x == 0:
		return True
	else:
		return False
year = int(input("year: "))
print(is_year_leap(year))
"""


# модуль random
"""
import random
list1 = []
list2 = []                         # создание списков
list3 = list()
for i in range(11):
	x = random.randint(1, 100)     # числа для первого списка
	list1.append(x)

for i in range(11):
	x = random.randint(1, 100)     # числа для второго списка
	list2.append(x)

for i, add in enumerate(list1):
	first = list1[i]
	second = list2[i] 
	third = first + second
	list3.append(third)            # добавление в третий список

print(list1)
print(list2)
print(list3)
"""


# линейное уравнение
"""
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))
if(a == 0 and b + c == 0):
	print("Бесконечное количество решений.")
if(a == 0 and b + c != 0):
	print("Решений нет.")
if a != 0:
	print((b+c) / a)
"""


"""
from math import sqrt
a = float(input("Число a: "))
b = float(input("Число b: "))
c = float(input("Число c: "))
D = b ** 2 - 4 * a * c
print(D, "- Дискриминант.")

if D > 0:
	x1 = (-b - sqrt(D))/ (2 * a)
	x2 = (-b + sqrt(D))/ (2 * a)
	print(x1, "- Первый корень.","\n", x2, "- Второй корень.", sep = "")
elif D == 0:
	x1 = -b / (2 * a)
	print(x1, "- Корень уравнения.")
else:
	print("Корней нет.")
"""


"""
print(True or False and False)
print((True or False) and False)
print(False and False or True)
print(True or False)
print(True and False)
"""







