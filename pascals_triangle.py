for i in range(1,6):
    c=1
    for j in range(0, 6-i,1):
        print(end= " ")
    for k in range (0,i):
        if (i==0 or k==0):
                c=1
        else:
             c = c * (i - k) // k
        print(c,end=" ")
    print("\n")