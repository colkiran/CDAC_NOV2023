
print("pop".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

res = l1.pop(3)                 # index
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(60, "-"))
l2 = [1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2]

print(f"l2 :{l2}")
l2.remove(3)

print(f"l2 :{l2}")
l2.remove(3)

print(f"l2 :{l2}")
l2.remove(3)

print(f"l2 :{l2}")
# l2.remove(3)


print("reverse".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")
