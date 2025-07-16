#polymorphism
class Car():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def mov(self):
        print("driving")
class Boat():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def mov(self):
        print("padling")
class Plane():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def mov(self):
        print("flying")
cars=Car("ford","mustang")
boats=Boat("Titanic","1980")
planes=Plane("jet","xlv")
for vehicle in (cars,boats,planes):
    vehicle.mov()