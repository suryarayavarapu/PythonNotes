#recursive approach using function
def fact (n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
n=5
print(fact(n))
#single line code for fatorial
1 if n==0 or n==1 else n*fact(n-1)
n=6
print (fact(n))
