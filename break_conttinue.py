print(list(range(1,10)))
numbers=list(range(2,40))
for i in numbers:
    if i%2==0:
        continue
    print (i)
# break
num=list(range(0,45))
for j in  num:
    if j==42:
        break
    print(j,end=" ")