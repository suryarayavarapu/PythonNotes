n=a=153
length=power=len(str(n))
sum=0
while(length>0):
    y=n%10
    sum=sum+(y**power)
    n=n//10
    length-=1
print(sum)
if(sum==a):
    print("given number  armstron number")
else:
    print("given number not an armstron number")

