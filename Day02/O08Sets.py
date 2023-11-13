
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s1 = {1, 2, 3, 4, 5, 6.4, 7.3, 8.5, 9, 'ten', 'eleven', 'twelve', 13+2j, 14-0j, True, False}

print(f"s1 :{s1}")

print("-" * 60)

s1 = {1, 2, 3}
print(f"s1 :{s1}")

s1.add(2)
s1.add(4)
s1.add(1)
s1.add(5)
print(f"s1 :{s1}")

s1.update([2, 3, 4])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([7, 8, 9])

print(f"s1 :{s1}")
print("-" * 60)

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")
s1.remove(5)
s1.remove(8)
# s1.remove(1)

print(f"s1 :{s1}")
print("-" * 60)

s1.discard(4)
s1.discard(7)
s1.discard(1)

print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("A union B :", A|B)
print("B union A :", B.union(A))
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))
print("A difference B :", A - B)
print("B difference A :", B.difference(A))
print("A symmetric_difference B :", A ^ B)
print("B symmetric_difference A :", B.symmetric_difference(A))

print("-" * 60)
# frozenset
# frozensets are immutable

x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
print(type(x))

