
try:
    num = 10
    div = 0
    res = num / div
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
except Exception as e:
    print(e)
else:
    print(f"The results are :{res}")

finally:
    print("Finally block code.....")