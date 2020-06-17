"""
matrix = [[-1, 0, 1], [-1, 0, 1],
		  [0, 1, -1], [1, 1, -1]
		  ]
print(matrix)
print(*matrix)

# вывод матрицы
def printMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print("{:5d}".format(matrix[i][j]), end = "")
		print()
print(printMatrix(matrix))


# нахождение произведения элементов матрицы
matrix = [[1, 2, 3],
		  [2, 3, 4],
		  [3, 2, 1]
		  ]
multiple = 1
def multiplication(matrix):
	global multiple
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			multiple *= matrix[i][j]
	print(multiple, "- произведение элементов матрицы.")
	print()
multiplication(matrix)


# нахождение суммы элементов матрицы
def addition(matrix):
	add = 0
	for i in matrix:
		add += sum(i)
	print(add, "- сумма элементов матрицы.")
	print()
addition(matrix)
"""

# задание 1
from statistics import mean
from colorama import init
from colorama import Fore, Style

init()

matrix = [[-8, -14, -19, -18],
          [25, 28, 26, 20],
          [11, 18, 20, 24]
          ]


def decision(matrix):
    print(Fore.RED, Style.BRIGHT)
    print()
    print(matrix[1][3], "- температура на 2-й метеостанции за 4-й день.")
    print(matrix[2][0], "- температура на 3-й метеостанции за 1-й день.")
    print("\n" * 2)

    print(Fore.BLUE)
    print("Показания всех метеостанций за второй день: ")
    for i in range(len(matrix)):
        print("<", matrix[i][1], ">,", end="  ")
    print("\n" * 2)

    print(Fore.LIGHTYELLOW_EX)
    median = mean(matrix[2])
    print(median, "- средняя температура на 3-ей метеостанции.")
    print("\n" * 2)

    def index(matrix, t):
        for i in range(len(matrix)):
            for index, num in enumerate(matrix[i]):
                if num == t:
                    return index

    print(Fore.LIGHTMAGENTA_EX)
    k = 1
    for i in range(len(matrix)):
        for j in matrix[i]:
            if (j >= 24) and (j <= 26):
                ix = index(matrix, j)
                print(
                    "{3}) В день {0} на станции {1} температура была в диапазоне 24-26 градусов тепла: {2} градусов.".format(
                        ix, i, j, k))
                k += 1
                print()
    print()
    print(Fore.GREEN)

    def find(matrix, a=0, b=0):
        for i in matrix:
            if min(i) < a:
                a = min(i)
            if max(i) > b:
                b = max(i)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == a:
                    a_ix = i, j
                    print("<", a, ">", "- наименьший элемент матрицы. Его индексы:", a_ix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == b:
                    b_ix = i, j
                    end_this_func = print("<", b, ">", "- наибольший элемент матрицы. Его индексы:", b_ix)
                    return end_this_func

    find(matrix)

    print(Fore.LIGHTCYAN_EX)
    print("\n" * 2)
    amount = 0
    for i in matrix:
        if sum(i) > amount:
            amount = sum(i)
            ind = i
    print("Строка матрицы, сумма элементов которой максимальна:", ind)


decision(matrix)
