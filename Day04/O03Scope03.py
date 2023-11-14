
def outerFun():
    gname = "Sachin"

    def innerFun():
        nonlocal gname             # local var can become nonlocal
        print("Hello World")
        gname = "Mr." + gname
        print(f"Greetings {gname}")

    innerFun()              # from outerFun
    print(f"Outer Function :{gname}")

outerFun()

