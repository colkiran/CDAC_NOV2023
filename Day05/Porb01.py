
def timeCalc(fnc):

    def helper(secs):
        from datetime import  datetime
        print("Calling the Function.......")
        st = datetime.now()
        fnc(secs)
        et = datetime.now()
        print("function executed successfully......")

        print(et - st)

    return helper

@timeCalc
def fun(x):
    lst = []
    for i in range(x):
        for j in range(1, i+1):
            lst.append(j ** 2)
    # print("hello world")



# fun = timeCalc(fun)

fun(8000)