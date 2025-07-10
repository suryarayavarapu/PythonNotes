for i in range (5,1,-1):
    for space in range(0,5-i):
        print(end=" ")
    for j in range (1,i):
        print("*",end=" ")
    print("\n")  
for j in range (1,6):
    for space in range(1,6-j):
        print(end=" ")
    for j in range (1,j):
        print("*",end=" ")
    print("\n") 