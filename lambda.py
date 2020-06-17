"""
x = lambda a, b: a * b
print(x(5, 6))

y = lambda a: a
print(y(5))

def myfunc(n):
	return lambda a: a * n
mydoubler = myfunc(5)
mytripler = myfunc(7)
print(mydoubler(11))
print(mytripler(15))
"""

"""
def my_func(f, arg):
	return f(arg)
print(my_func(lambda x: 2 * x * x, 5))

y = lambda x: 2 * x * x
print(y(5))

# named function
def polynomial(x):
	return x ** 2 + 5 * x + 4
print(polynomial(-4))

# lambda
print((lambda x: x ** 2 + 5 * x + 4) (-4))
print((lambda x, y, z: x ** y + y ** z + x ** z) (2, 4, 6))
a = (lambda x: x * x) (8)
print(a)
"""

# функция map
nums = [11, 22, 33, 44, 55]
result = tuple(map(lambda x: x + 5, nums))
print(result)


# функция filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)



