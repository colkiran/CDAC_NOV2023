
def doubleMesh(fnc):
    def  helper(*args):
        print("=" * 60)
        fnc(*args)
        print("#" * 60)

    return helper

def startSingle(fnc):
    def helper(*args):
        print("*" * 60)
        fnc(*args)
        print("_" * 60)

    return helper


@startSingle
@doubleMesh
def fun1(x, y):
    print("Fun1 called.....", x, y)

@startSingle
@doubleMesh
def fun2(x, y, z):
    print("Fun2 called.....",x, y, z)

@startSingle
@doubleMesh
def fun():
    print("Fun called.....")

fun()
# fun1(10, 20)
# fun2(10, 20, 30)



