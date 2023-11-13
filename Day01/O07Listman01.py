
l1 = list()
print(f"l1 :{l1}")
print("-" * 60)

l2 = list(range(1, 11))
print(f"l2 :{l2}")
print("-" * 60)

l3 = [1, 2, 3, 'four', 'five', 'six', 7.4, 8.1, 9.5, 10+3j, 11-5j, True, False]
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
values = list(range(10, 31, 10))
print(f"values :{values}")

# upack the list
print("-" * 60)
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print(f"l1 :{l1}")
print(f"l2 :{l2}")

l3 = [l1, l2]
print(len(l3))
print(f"l3 :{l3}")

l4 = [*l1, *l2]
print(len(l4))
print(f"l4 :{l4}")
