def fibanoic(n):
    if n==1:
        return 0
    elif n<=2:
        return 1
    else:
        return fibanoic(n-1)+fibanoic(n-2)
print(fibanoic (10)) 
#pirnt fibanoic series of number
                                        