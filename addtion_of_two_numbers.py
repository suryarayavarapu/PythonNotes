#method1
x=20
y=30
print(x+y)
#method 2
a=input("take first number")
b=input("take second number to add")
c=int(a)+int(b)
#u can use float 
print(c)
#method 3 using functions
def sumof2 (d,e):
    f=int(d)+int(e)
    print(f)
sumof2(105,95);
#method 4 using sum function
print(sum([10, 5]))
#method 5 using .add operator
import operator
print(operator.add(46,58))
#method 6 using lambda operator
sumof= lambda a, b: a+b
print(sumof (10,20))
