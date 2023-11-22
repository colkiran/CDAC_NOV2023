
import sys

num = 10
div = 0
try:
    res = num / div
except:
    print("exception raised......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
else:
    print(f"res :{res}")
finally:
    print("Division of numbers completed.....")
