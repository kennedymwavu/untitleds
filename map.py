# map in python: map(fn, iterables)
# Say you want to the length of each list in the tuple:
t1 = ('banana', 'apple', 'orange')

def length(x):
	return len(x)

x = map(length, t1)

print(x)

# Convert x to a list for readability:
print(list(x))

x = [[1, 2], [1, 2, 3]]
print(list(map(len, x)))

# Say we want to add two pairs of strings together:
def add(a, b):
	return a + b

print(list(map(add, ('apple', 'banana', 'orange'), ('lemon', 'grape', 'watermelon'))))
