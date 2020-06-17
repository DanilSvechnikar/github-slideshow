"""
words = ["hello", "world", "spam", "eggs"]
counter = 0
print(words)
max_index = len(words) - 1
print(max_index)
while counter <= max_index:
	word = words[counter]
	print(word + "!")
	counter = counter + 1
"""

"""
words = ["hello", "world", "spam", "eggs"]
for word in words:                   # та же программа, что и выше
	print(word + "!")
"""

"""
edibles = ["отбивные", "яйца","орехи"]
for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени!")
        break
    print("Отлично, вкусные " + food)

else:
    print("Хорошо, что не было пельменей!")
print("Ужин окончен.")
"""

"""
for i in range(5):
	print("hello!")
for i in range(0, 100, 2):
	print(i)
word = [5, 7 ,3 ,2]
print(word)
print(str(word))
print(list(word))


for letter in "Python":
	if letter is "h":
		pass
		print("This is pass block")
	print("Current Letter: ", letter)
"""

"""
# способ первый
tv = ["Секретные материалы",
      "Фарго",
      "Во все тяжкие"]
i = 0

for show in tv:
	new = tv[i]
	new = new.upper()
	tv[i] = new          # заменяет элемент 
	i += 1
print(tv)
"""


"""
# 2 способ(спец. синтаксис)
tv = ["Секретные материалы",
      "Фарго",
      "Во все тяжкие"]

for i, show in enumerate(tv):  # автоматически считает итерации цикла
	new = tv[i]
	new = new.lower()
	tv[i] = new
print(tv)
print(i)
print(show)
print(new)
print(tv[i])
"""


"""
my_list = ["Яблоко",
		   "Банан",
		   "Вишня",
		   "Персик"
		   ]

for c, value in enumerate(my_list, 1):   # необязательный параметр, не влияющий на итерации
	print(c, ")",  value)
"""

"""
tv = ["Meliodas"
	  "Esutarossa"
	  ]
coms = ["Теория взрыва",
		"Ривердейл"
		]
all_shows = []
i = 0
for show in tv:
	show = show.upper()
	all_shows.append(show)

for show in coms:
	show = show.upper()
	all_shows.append(show)

print(all_shows)
"""

"""
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
	for j in list2:
		added.append(i + j)

print(added)
"""


