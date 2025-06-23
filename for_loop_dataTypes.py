#for loopn with data types
#printing each charachter in new line in a string
name = "naga durya kiran"
for c in name:
    print (c)
# i need all characters i single line
fame="hello world"
for j in fame:
    print(j,end=" ")
print ("\n")
#reverse of a string using for loop
content= "harikrishna"
for i in content[::-1]:
    print(i,end= ' ')
#without using for loop based on syntax
message="welcome"
print(message[::-1])
# accesing words using split
information="hi hello namastey how are you"
print (information.split(" ",2))
print (information.split(" "))
#default white space character
print (information.split())
#using for loop accesign each word and count
count=0
for m in information.split():
    print (m)
    count+=1
print(count)
print(F"count of a words in a string is {count}")
#for loop with list in python uisng iterative
list1=["abc", "def", "ghi", "jkl"]
print(len(list1))
for i in range(len(list1)):
    print(list1[i])
#for loop with list in python uisng without iterative
for list in list1:
    print ("\n" ,list)
#for loop with dictionaries
dict1={"name":"surya","roll_no":21, "place":"bangalore","course":"python","marks":21.500}
for key in dict1:
    print(key)
    print(dict1[key])
print('\ndone\n')
for key in dict1.values():
#simliraly keys, for key in dict1.keys():
    print(key)
for key,values in dict1.items():
    print(values)
    print(key," : ",values)
