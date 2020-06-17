import math

from colorama import Fore, Style
from colorama import init

init()

print(Style.BRIGHT)
while True:
    print(Fore.BLUE)
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to quit")
    print("Enter 'factorial' to calculate the factorial of a number")
    print("Enter 'sqrt' to calculate the square root of x")
    print("Enter 'pow' to calculate the power of a number")
    print("Enter 'log' to calculate logarithm of number")
    print("Enter 'cos' to calculate cosine of number")
    print("Enter 'sin' to calculate sime of number")
    print("Enter 'tg' to calculate tangent of number")
    user_input = input("What operation should be performed?: ")
    print()

    print(Fore.MAGENTA)
    if user_input == "quit":
        print(Fore.GREEN + "The programm is over")
        break

    elif user_input == "add":
        try:
            num1 = float(input("Enter one number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 + num2)
            print("The answer is " + result)
        except ValueError:
            print(Fore.RED + "Error!")
        print()

    elif user_input == "subtract":
        try:
            num1 = float(input("Enter one number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 - num2)
            print("The answer is " + result)
        except ValueError:
            print(Fore.RED + "Error!")
        print()

    elif user_input == "multiply":
        try:
            num1 = float(input("Enter one number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 * num2)
            print("The answer is " + result)
        except ValueError:
            print(Fore.RED + "Error!")
        print()

    elif user_input == "divide":
        try:
            num1 = float(input("Enter one number: "))
            num2 = float(input("Enter another number: "))
            result = str(num1 / num2)
            print("The answer is " + result)
        except ValueError:
            print(Fore.RED + "Error!")
        except ZeroDivisionError:
            print(Fore.RED + "Error: ZeroDivision")
        print()

    elif user_input == "factorial":
        try:
            num1 = int(input("Enter one number: "))
            result = math.factorial(num1)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error: enter a int number!")
        print()

    elif user_input == "sqrt":
        try:
            num1 = float(input("Enter one number: "))
            result = math.sqrt(num1)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()

    elif user_input == "pow":
        try:
            num1 = float(input("Enter the number you want to raise to a power: "))
            num2 = float(input("Enter the degree of the number: "))
            result = math.pow(num1, num2)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()

    elif user_input == "log":
        try:
            num1 = float(input("Enter the number: "))
            num2 = float(input("Enter the base of the logarithm: "))
            result = math.log(num1, num2)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()

    elif user_input == "cos":
        try:
            num1 = float(input("Enter one number: "))
            result = math.cos(num1)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()

    elif user_input == "sin":
        try:
            num1 = float(input("Enter one number: "))
            result = math.sin(num1)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()

    elif user_input == "tg":
        try:
            num1 = float(input("Enter one number: "))
            result = math.tan(num1)
            print("The answer is " + str(result))
        except ValueError:
            print(Fore.RED + "Error")
        print()
