# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

#closure
# HOF   - Higher Order Function
def outerFun(info):
    inf = "Mr." + info
    def innerFun():
        print(info)
        print(inf)

    return innerFun

inref = outerFun("Rahul")
inref()         # already closed the outerFun
print("-" * 60)

outerFun("Rohit")()         # call the innerFun
