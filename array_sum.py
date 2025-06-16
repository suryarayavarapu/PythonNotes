array1={2,4,3,5}
n=len (array1)
print(n)
add=0
for i in array1:
    add+=i
    i+=1
print(add)
#using while loop
array2=[22,24,23,25]
x=0
sum=0
while(x<n):
    sum=sum+array2[x]
    x+=1
print(sum) 