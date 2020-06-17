""""
# мемоизация(memoization)
_fib_cache = {1: 1, 2: 1}
def mem_fib(n):
	result = _fib_cache.get(n)  # по умолчанию None
	if result is None:
		result = mem_fib(n - 2) + mem_fib(n - 1)
		_fib_cache[n] = result 
	return result
n = int(input("Введите n: "))
print("{", n, "}", "=" , mem_fib(n))
"""

"""
# карринг или каррирование(currying)
def greet_curried(greeting):
	def greet(name):
		print(greeting + ', ' + name, ".", sep = "")
	return greet

greet_hello = greet_curried("Hello")
greet_hello("German")
greet_hello("Ivan")

# или напрямую greet_curried
greet_curried("Hello")("Dan")              # так удобнее
"""

"""
def greet_deeply_curried(greeting):
	def w_separator(separator):
		def w_emphasis(emphasis):
			def w_name(name):
				print(greeting + separator + name + emphasis)
			return w_name
		return w_emphasis
	return w_separator

greet_deeply_curried("Hello")(", ")("!")("Meliodas")
"""

# вариант с lambda
greet_deeply_curried = lambda greeting: lambda separator: lambda name: lambda emphasis: \
	print(greeting + separator + name + emphasis)
greet_deeply_curried("Hello")(", ")("Meliodas")("!")






