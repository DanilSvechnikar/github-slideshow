# n -ый член последовательности Фибоначчи


def fib(n):
	if n >= 2:
		print(n, end=" ")
		return fib(n - 1) + fib(n - 2)
	else:
		return 1


print("\n", fib(int(input("Число больше 1: "))), " - результат.", sep="")


"""
# последовательность Фибоначчи
n = int(input("Число больше 2: "))
if n <= 2:
	quit()

fib1, fib2 = 1, 1
print(fib1, fib2, end = " ")

for i in range(2, n):
	fib1, fib2 = fib2, fib1 + fib2
	print(fib2, end = " ")
"""

"""
print()
a = 5.3
if type(a) is  int:
	pass
else:
	print("Error.")
print(type(a))
a = "Hey"
print(type(a))
"""

"""
a = int(input(": "))
if type(a) is not str:
	print("The program will end now.")
	quit()                    # первый способ завершение программы
	print("That's all.")	  # второй способ - raiseSystemExit
else:
	print("python".upper())
"""

"""
import sys
for i in range(25):
	if i < 19:
		print(i, end = "  ")
	else:
		sys.exit               # наиболее подходящий способ завершения программы
"""

"""
# n - ное число трибоначчи
def trib(n):
	if n > 3:
		print(n, end = " ")
		return trib(n - 1) + trib(n - 2) + trib(n - 3)
	elif n == 3 or n == 2:
		return 1
	else:
		return 0
n = int(input(": "))
print(trib(n))
print("Последнее число есть результат.")
"""

"""
# последовательность трибоначчи
def trib(n):
	if n > 3:
		return trib(n - 1) + trib(n - 2) + trib(n - 3)
	elif n == 3 or n == 2: 
		return 1
	else:
		return 0

def tribo(n):
	result = list()
	for i in range(1, n):
		result.append(trib(i))
	print(result)

n = int(input(": "))
tribo(n)
"""

"""
# последовательность трибоначчи другим способом
import sys
n = int(input(": "))
if n <= 3:
	sys.exit

trib1 = 0
trib2 = trib3 = 1
print(trib1, trib2, trib3, end = " ")

for i in range(3, n, 3):
	trib1 = trib1 + trib2 + trib3
	trib2 = trib1 + trib2 + trib3
	trib3 = trib1 + trib2 + trib3
	print(trib1, trib2, trib3, end = " ")
"""
