rows=int(input("enter value for to print numeber of stars in rows"))
for row in range(1,(rows+1)):
    for space in range(1,rows-row+1):
        print(end=" ")
    for star in range(1,row):
        print("*",end=" ")
    print("\n")
        