array=[[1,2,3],[4,5,6]]
multiplication=[]
product=multiply=1
for first_second in array:
    for elements in first_second:
        product*=elements
print("product of all element:",product)
#multiplication.append (array[0]*array[1])
for i in range(len(array[0])):
    multiplication.append([array[0][i]*array[1][i]])
print(multiplication)