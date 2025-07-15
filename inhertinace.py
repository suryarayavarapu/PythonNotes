class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __stri__(self):
        return f"my name is {self.name} and age is {self.age} ,received salary{self.salary}"
    def mymanager(self):
        return f"my manager is {self.name}"
class Manager(Employee):
    def mymanager(self):
        return f"my manager is {self.name}"
x1=Employee("hari",17,"1lakh")
print(x1.mymanager())
x2=Manager("surya",22,"2lakhs")
print(x2.mymanager())