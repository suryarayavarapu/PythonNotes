#random example
def recursion(x):
    if x>2:
        x-=1
        return recursion(x)
    else:
        return x
print(recursion(9))
print("\n")
#
def add_first(x):
    if (0<x<11):
        x+=add_first((x-1))
        print(x)
        return x
    elif x==0:
        return 0
    else:
        print("its not first 10 numbers sum")
add_first(-1)
#using recursion

