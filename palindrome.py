str_name="MadaM"
print(str_name)
str_name2=str_name[::-1]
if str_name2==str_name:
    print("its palindrome")
else:
    print("its not palindrome")
#using for loop temporary variable
temp=[]
count=len(str_name)
while count>0:
    #print(str_name[count-1])
    #count-=1
    temp.append(str_name[count-1]) 
    count-=1  
print (temp)
var1=''.join(temp)
print(var1)
if var1==str_name:
    print("its a  palindrome")
else:
    print("its not a palindrome") 
#with strng addition
var2=""
for i in temp:
    var2+=i
print("hi palindrome",var2)
#for loop
print(temp[0])
var3=""
for i in range(0,len(temp)): 
    var3+=temp[i]
print(var3)