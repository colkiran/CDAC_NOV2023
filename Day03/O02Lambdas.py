
def add(x, y):
    return x + y

a = add

print(a(24, 74))
print("-" * 60)

res = lambda a, b: a + b
print(res(10, 20))

print("-" * 60)
# lambdas are best used with map, reduce and filters

def square(x):
    return x ** 2

l1 = list(range(1, 11))

res = list(map(square, l1))
print(f"res :{res}")

print("-" * 60)

res= list(map(lambda x: x ** 2, l1))
print(f"res :{res}")

print("-" * 60)
#filter

lst1 = list(range(1,26))
print(f"lst1 :{lst1}")
res = list(filter(lambda x: x % 3 == 0, lst1))
print(f"res :{res}")

# reduce - functools
from functools import reduce
l1 = (3, 1, 6, 2, 5, 8, 4, 10, 7, 9)
res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

