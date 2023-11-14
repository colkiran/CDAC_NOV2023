
def callMe():
    print("apples from Ooty.......")

def fun(fnc):
    print("Hello...")
    fnc()
    print("Hi......")
    print("-" * 60)

    def defineMe():
        print("Oranges from Kanpur.........")

    return defineMe

def funCallBack(fnc):
    print("Mera Bharath Mahan......")
    fnc()
    print("India is great.....")

funCallBack(fun(callMe))
