
def fun(*args):
    print(args)
    print(*args)        # unpack

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4, 5)

print("-" * 60)

def sum(x, y):
    print("sum fucntion called.....")
    return x + y

def diff(x, y):
    print("diff function called.....")
    return x - y

def log_details(fnc):
    loginfo = "Logging in the service......"

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))           # call back
        print("-" * 60)

    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(25, 85)
diff_logger(85, 25)


