
def outerFun(greet):
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

# simple Curry
KanGreet = outerFun("Namaskara")
KanGreet("Rahul")
KanGreet("Kumble")

EngGreet = outerFun("Welcome")
EngGreet("Virat")

