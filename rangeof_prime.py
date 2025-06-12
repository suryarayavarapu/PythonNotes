for n in range(2,101):
    flag=True
    for i in range(2 ,n):
        if (n%i==0):
            flag=False
            break
    if flag:
        print( n)
        
        
        
        