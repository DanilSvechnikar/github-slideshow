# арифметическая прогрессия
from colorama import init
from colorama import Fore
from colorama import Back
from colorama import Style
init()
print(Style.BRIGHT)

def progression():
	print(Fore.GREEN)
	a1 = float(input("Enter a first number of progression.py: "))
	a2 = float(input("Enter a second number of progression: "))

	print(Fore.BLUE)
	d = a2 - a1
	print(d, "- difference.")
	if d > 0:
		print("The function is increasing.")
	else:
		print("The function is decreasing.")

	print(Fore.YELLOW)
	while True:
		try:
			n = int(input("Which member to find? "))
		except ValueError:
			print("'n' must be int!")
			continue
		if type(n) is int and n > 1:
			break
		else:
			print("Enter a int number greater then 1!")

	An = a1 + d * (n - 1)
	print(An, "- the value of the member progression.")

	print(Fore.MAGENTA)
	u = input("Enter to end the program...")
	return u

print(progression())

		





