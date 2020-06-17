"""
import os
x = os.path.join("Users",
			 "danil",
			 "Documents",
			 "st.txt")
print(x)

my_list = list()
with open("st.txt") as f:
	my_list.append(f.read())
print(my_list)
help("modules")
"""

"""
import csv
with open("st.csv", "w") as f:
	w = csv.writer(f, delimiter = ",")
	w.writerow(["один",
				"два",
				"три"])
	w.writerow(["четыре",
				"пять",
				"шесть"])

	v = csv.writer(f, delimiter = "|")
	v.writerow([2, 4, 8, 16])
	v.writerow([32, 64, 128, 256])
"""

"""
import csv
with open("st.csv", "r") as f:
	r = csv.reader(f, delimiter = "|")
	for row in r:
		print(",".join(row))
"""

"""
with open("test.txt", "w") as f:
	a = input("Hello, how low? ")
	f.write(a)
"""

"""
my_list = [["Звёздные войны",
	 		" Терминатор",
	 		" Искусственный интеллект"],
	 	   ["Дурак",
	 		" Матильда",
	 		" Левиафан"],
	 	   ["Люди в чёрном",
	 	    " Я - робот",
	 		" Эволюция"]
	 	   ]

import csv
with open("st.csv", "a") as f:
	 a = csv.writer(f, delimiter = ",")
	 a.writerow(my_list[0])
	 a.writerow(my_list[1])
	 a.writerow(my_list[2])
"""

"""
import csv
with open("st.csv") as f:
	r = csv.reader(f, delimiter = ",")
	for row in r:
		print(",".join(row))
"""










