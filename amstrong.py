n=a=1634
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
#using for loop getting armstrong number
value=54748
numbers=str(value)
print(numbers)
print(numbers[1])
count_digits=len(str(numbers))
print(count_digits)
sum=0
for number in numbers:
    print(number)
    sum+=((int(number))**count_digits)
    print(sum)
print(sum)