a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]

# To concatenate the two lists into one:
c = a + b
print(c)

# You can also use `*` to unlist the lists then make another list:
d = [*a, *b]
print(d)

# You can also use the extend() method:
e = [6, 7, 8]
f = ["f", "g", "h"]

e.extend(f)
print(e)
