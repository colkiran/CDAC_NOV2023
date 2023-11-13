
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")

# gname is called non default argument, cty is called default arg
def greetGstCty(gname, cty="Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event.....")

greet()
print("-" * 60)
greetGst("Sachin")
greetGst("Rahul")
print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
def add(x, y):
    return x + y

i = 10
j = 20
print(f"The sum of {i} and {j} is {add(i, j)}")

print("-" * 60)

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

x = 5
print(f"The factorial of {x} is {fact(x)}")

print("-" * 60)

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# named Arguments

def admsn(name, age, gender, qlf, adr, mrts, exp):
    print(f"Name            :{name}")
    print(f"Age             :{age}")
    print(f"Gender          :{gender}")
    print(f"Qualification   :{qlf}")
    print(f"Address         :{adr}")
    print(f"Marital Status  :{mrts}")
    print(f"Experience      :{exp}")


admsn(gender="Male", qlf="B.E", adr='MG Road, Bangalore', mrts="Bachelor", name="Kevin", age=26, exp=None)


print("-" * 60)
# variable length arguments
# *agr - will accept more than one argument in the form of a tuple
# **kwarg - will accept data like a dictionary

def multipyMe(*numbers):
    x = 1
    print(numbers)
    print(*numbers)     #unpack

    for i in numbers:
        x *= i
    return x

res = multipyMe(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extractPlayer(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)


extractPlayer(name='Sachin', age=35, runs=120, oppn="Aus", venue="Perth")

print("-" * 60)

def fun():
    # this is a comment
    "this is a docstring"

    print("Hello World")


fun()

print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    -----------

    the function fun1 takes two arguments
    1. if both the arguments are numeric then it will return the sum of the two numbers
    2. if both the arguments are strings then it will return a concatenated string
    3. if the data types are different then it returns a error
    """
    return x + y


res = fun1(36, 83)
print(f"res :{res}")

print("-" * 60)
print("-" * 60)
help(fun1)
