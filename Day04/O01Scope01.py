
Glbx = 100          #global variable

def fun(x):              # local Variable
    global Glbx          # do not assign any value to it here
    print(x)
    Glbx = 500
    print(f"Inside :{Glbx}")


print(f"Before :{Glbx}")

fun(10)

print(f"After :{Glbx}")

