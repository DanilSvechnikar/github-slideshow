"""
a = input("Введите число: ")
b = input("Введите ещё одно: ")
a = int(a)
b = int(b)
try:                        # Предупреждение исключения
    print(a/b)
except ZeroDivisionError:
    print("b не может являться 0.")
"""


"""
while 1 == 1:             # программа будет запускаться снова и снова после end
    try:
        a = input("Число один: ")
        b = input("Число два: ")
        a = int(a)
        b = int(b)
        print(a/b)
    except(ZeroDivisionError, ValueError):
        print("Ошибка ввода.")
"""



"""
try:
    10/0                           # Здесь ошибка
    c = "Я никогда не определюсь."
except ZeroDivisionError:
    print(c)


try:
    print("Hello".upper())
    print(1 / 0)
except ZeroDivisionError:
    print("Devided by zero")
finally:
    print("This code will run\nno matter what")

try:
        print(1)
        print(10 / 0)
except ZeroDivisionError:
        print(unknown_var)
finally:
        print("This is executed code")


try:
        print(1 / 0)       # первая ошибка
except ZeroDivisionError:  
        raise ValueError   # вторая ошибка

try:
        num = 5 / 0
except:
        print("An error occured")
        raise ValueError


# утверждения
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3   # после ошибки код не выполняется
print(5)


print(0)
assert "h" != "w"
print(1)
assert False    # после False код не выполняется
print(2)
assert True
print(3)


temp = -10
assert (temp >= 0), "Colder than\
                     absolute zero!"


def asrt(x, y = 8):
        assert x != 0, "Error."
        return x ** y
x = int(input("Enter a number: "))
result = asrt(x)
print(result)
"""

























