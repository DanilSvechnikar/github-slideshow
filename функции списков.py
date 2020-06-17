"""
from colorama import init
from colorama import Fore, Back, Style
print(Fore.WHITE)
print(Back.MAGENTA)
print(Style.BRIGHT)

words = ["hello"]
words.append("world")
letters = ["a", "b", "c"]
letters.append("d")
x = (len(letters))
print(x, "- количество элементов в списке \"letters\"")
print(words[0], words[1])
print()


import time
time.sleep(2)

print(Back.RED)
del words
words = ["Python", "is"]
variable = 2
variable1 = input("Что нужно добавить в список(слово)? ")
words.insert(variable, variable1)               # для insert нужно указывать место, поэтому используется переменная index
print(words)
print()

print("Проверка элементов в списке. Начало: ")
listik = ["p", "q", "r", "s", "p", "u",]
print(listik.index("r"))
b = listik.index("p")
print(b)

  # обработка исключения
try:
    print(listik.index("z"))
except ValueError:
    print("\"z\" is not in listik") 
print("Окончание проверки.")


other_list = [000, 111, 112, 238, 399, 457, 666, 000]
two_list = ["Hello", "friend", "!"]

print(Back.CYAN)
def entertainment():
    global x
    x = input("Введи 5(если не 5, то получится другое))!  : ")  
    print("\n" * 2)
    try:
        if int(x) == 5:
            print(other_list.count(000), "- Cтолько раз встречается элемент 0")       # возвращает кол. упоминаний элемента в списке
        else:
            print(two_list[0], two_list[1], two_list[2])
    except ValueError:
        print("Аргумент неправильного типа!")
        entertainment()              # повтор

entertainment() 
print(Back.GREEN)            
print("\n" * 1)        
print(max(other_list), "- Наибольше значение в списке")         # макс. элемент
print(min(other_list), "- Наименьшее значение в списке")        # мин. элемент
other_list.remove(112)                                          # удаление элемента             
print(not 112 in other_list, "- Элемента 112 нет")
other_list.reverse()                                            # расположение эл. в обратном порядке
print(other_list)

input("Нажмите, чтобы завершить: ")
"""


nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5.")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even.")
for v in enumerate(nums, 1):
    print(v)
    











