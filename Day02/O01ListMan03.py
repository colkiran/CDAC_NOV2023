
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1[3] = 3.5
print(f"l1 :{l1}")

print(len(l1))

del l1[3]
del l1[1]

print(f"l1 :{l1}")
print(len(l1))


print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])

print(f"l1 :{l1}")

print("extend".center(60, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")

l2.extend([6, 7, 8, 9, 10])
print(f"l2 :{l2}")

print("insert".center(60,"-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")

print("count".center(60, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 2, 1, 2, 2, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 2, 2, 2]

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print("index".center(60,"-"))
l1 = [1, 2, 3, 2, 2, 2,2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1]
print(f"l1 :{l1}")

print(f"3 :{l1.index(3)}")
print(f'3 :{l1.index(3, l1.index(3) + 1)}')
print(f'3 :{l1.index(3, l1.index(3, l1.index(3) + 1) + 1)}')

