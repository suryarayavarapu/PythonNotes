#random example
def recursion(x):
    if x>2:
        x-=1
        return recursion(x)
    else:
        return x
print(recursion(9))
print("\n")
#if key value pair passing arguments "**" required 
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
print("\n\n\n")
#if not key value pair single "*" enough
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
print("\n\n\n")
#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#recursion sum of ten numbers in recursion mode
def add_first(x):
    if (0<x<11):
        x+=add_first((x-1))
        print(x)
        return x
    elif x==0:
        return 0
    else:
        print("its not first 10 numbers sum")
add_first(-1)

