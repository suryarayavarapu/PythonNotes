#check element in list for duplicates if one found no need to check duplicte
while True:
    value=input("enter value")
    if value=='q':
        break
    print(value)
print("you exited loop")

#list of fruits while else
fruits=["apple","banana","kiwi","onion","potato"]
#fruits=["apple","banana","orange","kiwi","onion",,"potato"]
#fruits=["apple","banana","kiwi","orange","onion","orange","potato"]
i=0
while i<(len(fruits)):
    if fruits[i]=="orange":
        print("orange in the list")
        break
    i+=1
else:
    print("oranges not in the lsit")
#method2 with error note :if you are not using else block  like given below   
i=0
while i<(len(fruits)):
    if fruits[i]=="orange":
        print("orange in the list")
        break
    i+=1
print("oranges not in the lsit")
#even oranges are present not preset both are printed for that reason use else block
#Method3 using flag
#step1: assume initially item not present set flag=False with reasonable variable like fruit_found=False
i=0
fruit_found=False
while i<(len(fruits)):
    if fruits[i]=="orange":
        fruit_found==True #if fruit founds set flag to true
        print("orange in the list")
        break
    i+=1
#update based on flag status, if status true it wont print if it false then it print
if not fruit_found:
    print("oranges not in the lsit")
#using for loop
#input 1 >>>cars=["bmn","toyota","audi","benz"]
cars=["bmn","toyota","audi","benz","mahindra","jaguar","mahindra"]
car_found=False
for car in  cars:
    if car=="mahindra":
        car_found=True
        print("car mahindra is present ")
        break
if not car_found:
    print("car mahindra not found")