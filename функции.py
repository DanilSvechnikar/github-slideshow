"""
def max(x, y):
	if x >= y:
		return x  # Возврат из функции
	else:
		return y
print(max(4, 7))
z = max(8, 5)
print(z)
"""

"""
def shortest_string(x, y):
	if len(x) <= len(y):
		print(x)
	else:
		print(y)
shortest_string("one", "two")


def add_numbers(one_str, two_str):
	total = one_str + two_str
	return total
	print("This won't be printed")   # После return функция не выполняется
print(add_numbers("Hello ", "world"))


def add(x, y):
	return y + x

def do_twice(func, x, y):
	return func(func(x, y), func(x, y))
a = 5
b = 10
print(do_twice(add, a, b))

def square(x):
	return x * x

def test(func, x):
	print(func(x))
test(square, 42)


def func(x):
	res = 0
	for i in range(x):
		res += i
	return res
print(func(4))
"""

"""
def apply_twice(func, arg):
	return func(func(arg))
def add_five(x):
	return x + 5
print(apply_twice(add_five, 10))
"""

"""
# пример чистой функции
def pure_function(x, y):
	temp = x + 2 * y
	return temp / (2 * x + y)
print(pure_function(10, 20))

# пример нечистой функции
some_list = []
def impure(arg):
	some_list.append(arg)
	return some_list
print(impure("Anything."))
"""

"""
# функция map
def add_five(x):
	return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)


# функция filter
def del_filt(x):
	return x % 2 == 0
nums = [11, 22, 33, 44, 55]
res = list(filter(del_filt, nums))
print(res)
"""


"""
def fun():
	for x in range(10):
		yield(x)
x = fun()
for a in range(5):
	next(x)
print(next(x))
"""

"""
# генератор
def countdown():
	i = 5
	while i > 0:
		yield i
		i -= 1

for i in countdown():
	print(i)

gener = set()
generate = list()

for i in countdown():
	generate.append(i)
print(generate)

for i in countdown():
	gener.add(i)
print(gener)
"""

"""
def infinite_sevens():
	while True:
		yield 7            # бесконечный генератор

k = 0
for i in infinite_sevens():
	print(i)
"""

"""
def numbers(x):
	for i in range(x):
		if i % 2 == 0:
			yield i
print(list(numbers(11)))


def numb(y):
	for i in range(y):
		yield i
print(tuple(numb(6)))
"""

"""
# функция zip
a = [1, 2, 3]
b = "xyz"
c = (None, True)
res = set(zip(a, b, c))
print(res)


names = ["Tom", "Dick", "Harry"]
ages = [50, 35, 60]
print(dict(zip(names, ages)))


a = "wyx"
b = [1, 2, 3, 4, 5]
c = ("Hello", "How low?")
res = list(zip(a, b, c))
print(res)
"""


"""
# декораторы
def decor(func):
	def wrap():
		print("===========")
		func()
		print("===========")
	return wrap

def print_text():
	print("Hello world!")
print_text()

# декорированная версия, если требуется
def v1():
	decorated = decor(print_text)
	decorated()
v1()
print()
print()

# версия, если нужна всегда декорированная
def v2():
	global print_text
	print_text = decor(print_text)
	print_text()
v2()
"""

"""
# несколько декораторов
def bread(func):
	def wrapper():
		print()
		func()
		print("<_____/>")
	return wrapper

def ingredients(func):
	def wrapper():
		print("#помидоры#")
		func()
		print("~салат~")
	return wrapper

# более быстрый и удобный способ
@ bread
@ ingredients
def sandwich(food = "--ветчина--"):
	print(food)
sandwich()

# способ 2
def v1():
	global sandwich
	sandwich = bread(ingredients(sandwich))
	sandwich()
"""

"""
def decorator_maker():
	print("Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")
	def my_decorator(func):
		def wrapped():
			print("Я - обёртка вокруг декорируемой функции.\n"
		          "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
		          "Я возвращаю результат работы декорируемой функции.")
			return func()
		return wrapped
	print("Я возвращаю декоратор.")
	return my_decorator

# Теперь декорируем функцию
def decorated_function():
    print("Я - декорируемая функция.")

decorated_function = decorator_maker()(decorated_function)
# Теперь наконец вызовем функцию:
decorated_function()
"""

"""
def gen():
	for i in range(10):
		x = yield i
		print(x)
G = gen()
next(G)
G.send(77)
G.send(None)
G.send(False)
next(G)
print()

print([x ** 2 for x in range(4)])
print((x ** 2 for x in range(4)))
G = (x ** 2 for x in range(4))
print(next(G))

for num in (x ** 2 for x in range(4)):
	print(num, num / 2.0, sep = ", ")

G = (c * 4 for c in "SPAM")
print(list(G))

def timefour(S):
	for c in S:
		yield c * 4
G = timefour("spam")
print(list(G))


G = (c * 4 for c in "spam")
I = iter(G)
print(next(I))
"""





