
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy l1 to l2
l2 = l1         # shallow copy - copies the data along with the address

print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")

l4 = l3.copy()              #Deep copy - copies only the data
print(f"l4 before :{l4}")

l4.extend([60, 70, 80])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
l5 = [1, 2, 3, [5, 10, 15, 20], 4, 5]
print(f"l5 before :{l5}")

l6 = l5.copy()
print(f"l6 before :{l6}")

l6[3].append(25)
l6[3].append(30)
l6[3].append(35)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
from copy import deepcopy
l7 = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(f"l7 before :{l7}")

l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].append("d")
l8[4].append("e")

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(60, "-"))

l1 = [9, 5, 8, 1, 6, 10, 2, 4, 7, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")
print("=" * 60)

l1 = [9,'zebra', 'yellow', 5, 'apple', 'blue', 8, 'white', 'violet', 1, 'green', 'orange', 6, 'purple', 'dog', 10, 'cat', 'egg', 2, 'hen', 4, 'mango', 7, 'king',3, 190, 1634, 27, 250, 2034]

print(f"l1 :{l1}")
print("=" * 60)

res = sorted(l1, key=ascii)
print(f"res :{res}")

print(res[:res.index("zebra")+1] + sorted(res[res.index('zebra')+1:]))

print("clear".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")


