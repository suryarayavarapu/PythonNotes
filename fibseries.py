fib={}
fib[0]=0
fib[1]=1
fib[2]=1
for i in range (2,10):
    fib[i]=fib[i-1]+fib[i-2]
for i in range (0,10):    
    print (fib[i])