fruits = {"a" : "apple", "b" : "banana", "c" : "citrus", "d" : "dates"}

# to print only the keys of fruits:
for key in fruits.keys():
	print(key)

# to print only the values of fruits:
for value in fruits.values():
	print(value)

# to print key, value pairs:
print(fruits, "\n")

for key in fruits.keys():
	print(key, ":", value, "\n")

# And even better:
for key, value in fruits.items():
	print(key, ":",  value, "\n")
