#using while loop
list3=[5,2,3]
list4=[6,7,8]
m=0

print(len(list3))
print(len(list4))
while m <len(list3):
    n=0
    while n < len(list4):
        print(list3[m],list4[n])
        n+=1
    m+=1      
       
    