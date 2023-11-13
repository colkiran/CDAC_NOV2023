
a = int(input("Enter the first number :"))
print(a)
print(type(a))

b = int(input("Enter the second number :"))
print(b)
print(type(b))

c = int(input("Enter the third number :"))
print(c)
print(type(c))

if a < 10: print("'a' is a single digit number :", a)

if a >= b and a >= c:
    print(f"a is the greatest :{a}")
elif b >= a and b >= c:
    print(f"b is the greatest :{b}")
else:
    print(f"c is the greatest :{c}")

