import pytz
from datetime import datetime as dt
from time import sleep
from sys import exit
from colorama import Fore, Back, Style
from colorama import init
init()
print(Style.BRIGHT)


def country_time():
	print("Здравствуйте! Начнём поиск!")
	sleep(1.5)
	print()
	country_code = input("Введите код интересующей страны в формате Alpha2(две буквы)\n: ")
	print()

	try:
		country_code = pytz.country_timezones[country_code]
	except KeyError:
		print(Fore.RED + "Код введён неправильно, либо не поддерживается.")
		print(Fore.RED + "Попытайтесь снова.")
		exit()

	for num, i in enumerate(country_code, 1):
		print(num, ")", i)
	print()
	print("Это весь список стран введённого кода.")
	print()
	sleep(1)
	print("Теперь из предложенных напишите страну, которая интересует,\nИли просто скопируйте название(полностью).")
	print()

	country = input(": ")
	print(Back.GREEN)
	print(Fore.WHITE)
	country = country.strip()
	if country in country_code:
		utc = pytz.timezone(country)
		time = dt.now(tz=utc).strftime("Today is %B %d, %Y.\n%X  %Z.")
		return time
	else:
		ending = Fore.RED + Back.BLACK + "Код введён неправильно!"
		return ending


print(country_time())
