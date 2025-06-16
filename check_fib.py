fib={}
fib[0]=0
fib[1]=1
for i in range (2,10):
    fib[i]=fib[i-1]+fib[i-2]
if int(22) in fib.values():
    print ("fibnoic value present")
else:print ("fibnoic value not  present")