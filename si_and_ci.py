#simple interset
def simp_intr(p,t,r):
    return (p*t*r)/100
print (simp_intr(8,6,8))
#using lambda SI
si=lambda a,b,c :(a*b*c)/100
print(si(5,6,7))
#Compound intrest
def comp_intr(pri,peri,roi):
    amount=pri*((1+(roi/100))**peri)
    return (amount-pri)
print(comp_intr(1200, 2, 5.4))