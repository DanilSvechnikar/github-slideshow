numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep = ",")



fruits = ["lemon", "pear", "watermelon"]
print(*fruits)



def transpose_list(list_of_lists):
	return [list(row) for row in zip(*list_of_lists)]
print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))



date_info = {"year": "2020",
			 "month": "01",
			 "day": "01"
			 }
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)



date_info = {"year": "2020",
			 "month": "01",
			 "day": "01"
			 }
track_info = {"artist": "Beethoven",
			  "title": "Symphony No 5"
			  }
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info,
															  **track_info)
print(filename)



from random import randint
def roll(*dice):
	return sum(randint(1, die) for die in dice)
print(roll(5, 6, 7))



fruits = ["lemon", "pear", "melon", "cheery"]
first, *middle, last = fruits
((first_letter, *remaining), *other_fruits) = fruits
print(middle)
print(remaining)



def palindromify(sequence, sequence1):
	print([*sequence, *reversed(sequence)])
	return [*sequence1, *reversed(sequence1)]
sequence = ["Hello", "Python"]
sequence1 = "Python"
print(palindromify(sequence, sequence1))



fruits = ["lemon", "pear", "melon", "cheery"]
(*fruits[1:], fruits[0])
uppercase_fruits = (f.upper() for f in fruits)
new_fruits = {*fruits, *uppercase_fruits}
print(new_fruits)



date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
new_info = {**date_info, **track_info}
print(new_info)
