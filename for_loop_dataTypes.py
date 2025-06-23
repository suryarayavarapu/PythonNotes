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
