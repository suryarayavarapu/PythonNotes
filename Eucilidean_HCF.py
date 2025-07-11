x1=int(input("enter first vlaue"))
x2=int(input("enter second vlaue"))
if x1>x2:
    x3=x2
else: x3=x1
if x1>x2:
    x4=x1
else:x4=x2
print(x3,x4)
def hcf(x3,x4):
    x5=x4//x3
    print(x5)
    x6=x4%x3
    print(x6)
    if(x6==0):
        return x3
    else:
        return hcf (x6,x3)
x7=hcf(x3,x4)
print(x7)