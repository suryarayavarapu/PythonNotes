number1=int(input( "take a number1 to find hcf"))
number2=int(input("enter second number"))
print(number1,number2)
print("factors of number1")
var1=[]
var2=[]
for i in range (1,number1+2):
    if number1%i==0:
        print(i)
        var1.append(i)
print(var1)
print("factors of number2")
for i in range (1,number2+2):
    if number2%i==0:
        print(i)
        var2.append(i)
print(var2)
count=len(var2)
print(count)
var3=[]
for i in var1:
    x=0
    max_hcf=0
    while(x<count):
        if i==var2[x]:
            var3.append(i)
           # if max_hcf<i:
            #    max_hcf=i
            # print(max_hcf)        
        x+=1
print(var3) 
var3.sort()
print(var3[-1])
#new method to find hcf
x1=int(input("enter first vlaue"))
x2=int(input("enter second vlaue"))
if x1>x2:
    x3=x2
else:x3=x1
x5=[]
for i in range(1,x3+1):
    if(x1%i==0 and x2%i==0):
        hcf=i
print(hcf)
