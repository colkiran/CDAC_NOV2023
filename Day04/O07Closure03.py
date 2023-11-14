
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
KanGrtTiger = KanGrt("lion")
KanGrtTiger("Prabhakar")



"""

EngGrt = outerFun("Welcome")
EngGrtSngArw = EngGrt("------>")
EngGrtDblArw = EngGrt("=====>>")

EngGrtSngArw("Messi")
EngGrtDblArw("Sachin")
"""