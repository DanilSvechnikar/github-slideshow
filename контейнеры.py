"""
print("Привет".upper())   # upper преобразует строки к верхнему регистру
print("Привет".replace("в", "V"))

fruit = ["Apple", "Orange", "Pear"]
print(fruit[2])
colors = ["синий", "зеленый"]
colors[1] = "красный"
print(colors)


colors = ["синий", "зеленый", "желтый"]
colors.pop()
print(colors)


colors1 = ["blue", "green", "red"]
colors2 = ["white", "magenta", "green"]
print(colors1 + colors2)
print("green" in colors1)
print("green" in colors2)
"""

"""
# Ниже пример списка на практике
colors = ["фиолетовый",
		  "оранжевый",
		  "зеленый"]
guess = input("Укажите цвет: ")
if guess in colors:
	print("Вы угадали!")
else:
	print("Неправильно! Попробуйте ещё.")
"""

"""
# Ниже кортежи
my_tuple = tuple("М. Джексон")         
print(my_tuple)
my_tuple = (195.8, "Азазель")
print(my_tuple)
print(my_tuple[1])
my_tuple = tuple("Джексон")
print(my_tuple[0])
my_tuple = ("self_taught",)
print(my_tuple)
"""

"""
dys = ("1984",
	   "Oh, why wonderful world")
print("1984" not in dys)

# А теперь - словари
my_dict = dict()
print(my_dict)
my_dict = {}
print(my_dict)
fruits = {"Яблоко": "красное",     # словарь
		  "Банан": "желтый",
		  1969: "Основание 'Advanced Micro Devices",
		  1968: "Основание Intel"}
print(fruits)
print(list(fruits))   # список
print(tuple(fruits))  # кортеж
del fruits
print()

facts = dict()
facts["код"] = "Смешной"   # add a value
print(facts["код"])   # look up a key
print("код" in facts)
facts["Основание"] = 1776
print(facts)
print()

bill = dict({"Билл Гейтс": "щедрый"})
print("Билл Гейтс" in bill)
bill[dys] = "else one values"    # кортеж в качестве ключа для словаря
print(bill)
books = {"Процесс": "Кафка"}
del books["Процесс"]
print("Процесс" in books)


rhymes = {"1": "смех",
		  "2": "синий",
		  "3": "я",
		  "4": "этаж",
		  "5": "жизнь"}
n = input("Введите число: ")
if n in rhymes:
	rhyme = rhymes[n]
	print(rhyme)
else:
	print("Не найдено.")


lists = []
rap = ["Баста", "Кравц"]
rock = ["Наутилус Помпилиус", "Кино"]
djs = ["Paul Oakenfold"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)
print(lists[1][0])

eights = ["Эдгар Алан По",
		  "Чарльз Диккенс"]
nines = ["Хемингуэй"]
authors = (eights, nines)      # списки внутри кортежа
print(authors)

bday = {"Хемингуэй": "21.07.1899",
	    "Фицджеральд": "24.09.1896"}
my_list = [bday]    # словарь внутри списка
print(my_list)
my_tuple = (bday,)  # словарь внутри кортежа
print(my_tuple)


ru = {"Расположение": (55.7522, 37.6155),
      "Знаменитости": ["Андрей Звягинцев", "Юрий Быков"],
      "Факты": {"город": "Москва",
      			"страна": "Россия"}
      }
print(ru)
print(ru["Расположение"][1])
print(ru["Знаменитости"][1])
print(ru["Факты"]["город"])
"""

"""
# множества
a = set()
print(a)
a = set("hello")
print(a)
a = {"a", "b", "c", "d"}
print(a)
a = {i ** 2 for i in range(2, 25, 3)}  # генератор множества
print(a)
# a = {} # это не множество, а словарь!
         # Нельзя создавать пустое множество с помощью литерала
words = {"hello", "how low", "hello", "Hello"}
set(words)
print(words)
u = set.union(words, a)
print(u)
print(len(a))
print(len(words))
print(set.intersection(a,words))

a = {"Meli", "Eliz", 69}
b = {"Meli", "eliz", 70,}
c = set()
set.add(a,"Esutarossa")
set.add(b, "Escanor")
a.add("esutarossa")
b.add("escanor")
print(a, b)
print(set.discard(a, "Esutarossa"))

print()
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
"""

"""
# frozenset - неизменяемый тип данных
a = frozenset("qwerty")
b = frozenset("qwerty")
print(a == b)
print(a is b)
try:
	print(a.add("ytrewq"))
except AttributeError:
	print("Ошибка!")
finally:
	print("Нельзя изменять frozenset.")
"""



"""
# словарь
squares = {1: 1, 
		   2: 4, 
		   3: "error", 
		   4: 16
		   }
squares[8] = 64
squares[3] = 9
print(squares)


primes = {1: 2, 
		  2: 3, 
		  4: 7, 
		  7: 17
		  }
print(primes[primes[4]])


nums = {1: "one",
		2: "two",
		3: "three"
		}
print(1 in nums)
print("three" in nums)


pairs = {1: "apple",
		 "orange": [2, 3, 4],
		 True: False,
		 None: "True"
		 }
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
print(pairs.get(True))
print(pairs.get(None))


fib = {1: 1,
	   2: 1,
	   3: 2,
	   4: 3
	   }
print(fib.get(4, 0) + fib.get(7, 5))


# кортежи 
my_tuple = "one", "two", "three"
print(my_tuple[1])
tup = tuple("Hello!",)
print(tup)
print(my_tuple[:2])


# zip
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(tuple(zip(t1, t2))[1][0])
"""

"""
# методы iter() и next()
my_tuple = ("яблоко", "банан", "вишня")
myit = iter(my_tuple)
print(next(myit))
print(next(myit))
print(next(myit))
try:
	print(next(myit))
except StopIteration:
	print("StopIteration.")
finally:
	print("Итерация завершена, элементов больше нет.")
"""




























