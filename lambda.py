# lambda is used for short anonymous functions
# lambda can take any number of arguments but can only have one expression

# Example: function to add 5 to a number
add5 = lambda x : x + 5

print(add5(5))

# Function to multiply by 10:
mult10 = lambda x : x * 10

print(mult10(10))

# Function to replace all 4's in a string by 1:
repl = lambda given_string : given_string.replace('4', '1')
mytupple = ("40", "140")

print(list(map(repl, mytupple)))

# Add 2 numbers:
add = lambda x, y : x + y

print(add(2, 3))
print(add(5, 10))

# We can use lambda functions inside normal functions:
def myfn(n):
	return lambda a : a * n

print(myfn(2)(3))

# Let's create a double and triple function from `myfn`:
double = myfn(2)

print(double(5))

triple = myfn(3)

print(triple(5))

