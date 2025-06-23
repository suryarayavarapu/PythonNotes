#recursive approach using function
def fact (n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
n=5
print(fact(n))
#single line code for fatorial (note disable above code=dacadd)
def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
n=6
print (fact(n))
#using math function
import math
def facts(d):
    if d<0:
        return None
    else:
        return math.factorial(d)
d=-1
print(facts(d))
#           