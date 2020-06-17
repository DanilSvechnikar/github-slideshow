"""
author = "Meliodas"
print(author[0])
print(author[7])
print(author[-1])
print(author[-4])
print("MELiodAs Is aLiVE.".lower())   # понижает регистр
print("melioDaS Is alivE.".upper())
print("meLoadaS.".capitalize())     # делает первую букву прописной
print("Mel {}".format("Eliz"))
last = "Liz"
print("Meli {}".format(last))

n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter a adjective: ")
n2 = input("Enter a noun: ")
r = '''Same us usual, {}
		and {},
		and {},
		and {}.
    '''.format(n1, v, adj, n2)
print(r)



print("Я прыгнул через голову...!fgfgf Это целых 2 метра!".split("."))   # разделяет строки
print("Я русский. Я француз. Я китаец. Я шучу!".split("Я француз"))
a = "Кто ты? А кто ты?".split("?")
print(a)

first_three = "abc"
result = "+".join(first_three)   # добавляет новые символы
print(result)					 # между всеми символами в строке
words = ["Рыжая",
		 "лисица",
		 "сделала",
		 "...",
		 "голову"]
one = " ".join(words)
print(one)

s = "   Moscow   "
s = s.strip()         # удаляет пробельные символы
print(s)

equ = "All animals are the same."
equ = equ.replace("a", "@")       # заменяет каждое вхождение строки другой строкой
print(equ)
uqe = "turTlet07"
print(uqe.replace("t", "  "))

print("животные".index("н"))   # индекс первого вхождения символа в строке
a = "животные".index("в")
print()
try:
	print(equ.index("t"))
except:
	print("Не обнаружено.")
finally:
	print("Наберешь, когда позвонишь.")

print("Cat" in "Cat in hat.")
print("hat" in "Cat in Hat")
print("cat " in "catin hat")
print("Cat" not in "Cat in hat.")
"""

"""
fict = ["Толстой",
		"Дик",
		"Оруэлл",
		"Остин"]
print(fict[0:2])                   # извлечение среза
ivan = "Иванович стал спрашивать"
print(ivan[5:17])
a = fict[:3]
print(a)
b = ivan[10:]
print(b)
squares = [0, 1, 4, 9, 16, 25, 36]
print(squares[::2])
print(squares[2:5:2])

squares1 = [0, 1, 4, 9, 16, 25, 36,]
print(squares[::-1])
sqs = [0, 1, 4, 9, 16, 25, 36, 49]
print(sqs[5:2:-1])
"""

"""
# форматирование строк
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(*nums)
print(msg)

a = "{x}, {y}".format(x = 5, y = 12)
print(a)

print("Hello ME".replace("ME", "world."))

print("This is a sentence".startswith("This"))		# подстрока в начале строки
print("It's not me, it's you!".startswith("It'"))

print("This is a sentence".endswith("e"))			# подстрока в конце строки

print("spam, eggs, ham".split(","))
print("spam", "eggsandcock".split("and"), "ham".split(","))

print(min("hel", "hello", "helloooo"))
print(max(1, 4, 7, 19))

print(abs(-99))
print(abs(42))

print(sum([1, 2, 3, 4, 5]))

a = min(sum([11, 22]), max(abs(-30), 2))
print(a)
"""


"""
# метод format
name = "Bobik"
errno = 50159747054
# примеры использования формата
print("Hey {name}, there is a 0x{errno:x} error!".format(name = name, errno = errno))
print("Hey {name}, there is a 0x{errno:X} error!".format(name = name, errno = errno))
print("Hey {name}, there is a 0x{errno:o} error!".format(name = name, errno = errno))
print("Hey {name}, there is a 0x{errno:d} error!".format(name = name, errno = errno))

# синтаксис "f-string"
print(f"Hello, {name}!")
a = 5
b = 10
print(f"{a + b} and {2 * (a + b)}.")
print("\n" * 2)

# выравнивание
a = "Python"
print("Hello, {:>20}".format("Python!"))
print("{:+>10}{a}".format("",a = a))
print("{:<50}".format("py"))
print("{:_<20}".format("Right aligned"))
print("{:^50}".format("center aligned"))
print("{:^^50}".format("center aligned"))
print("{:*^50}".format("center aligned"))
print("{:*^19}".format("center aligned"))
print("{:^=20}".format(50))
print("{:+F}; {:+F}".format(3.14, -3.14))
print("{:-}; {:-}".format(3.14, -3.14))
print("{:f}; {:f}".format(3.14, -3.14))
print("{:-}; {:-}".format(-3.14, -3.14))
# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
points = 19.5
total = 22
print("Correct answer: {:.2%}".format(points / total))
"""






# перевод в другие системы счисления
x = 758
y = 64
z = "386"
print(bin(y))
print(hex(y))
print(oct(y))
print(int("16", 8))
print(int(z, 36))
print(int("1010", 2))




