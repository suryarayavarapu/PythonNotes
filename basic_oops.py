#OOPS=object oriented programing
#basic class 
class Myclass():
    x1=6
#basic object created
z=Myclass()
print(z.x1)
#-----------
class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #without def __str__ check result error
    def __str__(self):
       return f"my name is {self.name} and my age is {self.age}"
    def myfunc(self):
        print(f"hello world {self.name}")
x=Person("surya",26)
y=Person("kiran",22)
print(x.name)
print(x.age)
print(x)
print(y)
x.myfunc()