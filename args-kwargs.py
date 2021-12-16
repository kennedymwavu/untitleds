# consider the function below designed to add 2 numbers  together:
def add(a, b):
	return a + b

# It works fine:
print(add(1, 2))

# But what if you needed a function that unlimited number of integers / numerics and sums them up?

# Well, you could pass a list or a tuple of integers as below:
def add2(list_or_tuple):
	return sum(list_or_tuple)

# And it would work fine:
print(add2([1, 2, 3]))
print(add2((1, 2, 3)))

# But now whenever you call that function you have to create a list or tuple of arguments to pass to it
# *args allows you to pass a varying number of positional arguments. 
# For example:
def add_args(*args):
	return sum(args)

print(add_args(1, 2, 3))
print(add_args(1, 2, 3, 4, 5))


# To input a list directly into `f()` put a `*` before the list:
print(add_args(*[1, 2, 3]))

list1 = [10, 20, 30]
print(add_args(*list1))

# The same goes for a tuple:
print(add_args(*(1, 2, 3)))

# **kwargs is usually used for key word arguments:
def kwargs1(**kwargs):
	print(kwargs)

kwargs1(**{"1" : 2, "2" : 3})

def print_vals(**kwargs):
	for key in kwargs:
		print(kwargs[key])

print_vals(**{"1" : 2, "2" : 3})

